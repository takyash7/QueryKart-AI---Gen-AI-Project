from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy import text

from langchain_groq import ChatGroq

from langchain_core.prompts import (
    PromptTemplate,
    FewShotPromptTemplate
)

from validator import validate_sql_query

from few_shots import few_shots

from retriever import retriever

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# DATABASE CONFIG
# ==========================================

DB_HOST = os.getenv("MYSQLHOST")
DB_PORT = os.getenv("MYSQLPORT")
DB_USER = os.getenv("MYSQLUSER")
DB_PASSWORD = os.getenv("MYSQLPASSWORD")
DB_NAME = os.getenv("MYSQLDATABASE")

# ==========================================
# DATABASE ENGINE
# ==========================================

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================
# GROQ MODEL
# ==========================================

llm = ChatGroq(

    groq_api_key=os.environ["GROQ_API_KEY"],

    model_name="llama-3.3-70b-versatile",

    temperature=0.1
)

# ==========================================
# FEW SHOT FORMAT
# ==========================================

example_prompt = PromptTemplate(

    input_variables=[
        "Question",
        "SQLQuery"
    ],

    template="""

Question:
{Question}

SQL Query:
{SQLQuery}

"""
)

# ==========================================
# MAIN PROMPT TEMPLATE
# ==========================================

few_shot_prompt = FewShotPromptTemplate(

    examples=few_shots,

    example_prompt=example_prompt,

    prefix="""

You are an expert MySQL assistant.

Convert user question into ONLY pure SQL query.

STRICT RULES:

- Return ONLY SQL query
- No explanation
- No markdown
- No comments
- Output must start directly with SELECT
- Use valid MySQL syntax only
- Never hallucinate columns
- Use ONLY schema provided below
- Use proper JOIN relationships
- Never generate dangerous SQL queries

==================================================
DATABASE CONTEXT
==================================================

{retrieved_context}

==================================================
IMPORTANT JOIN RULES
==================================================

- order_items.variant_id joins product_variants.variant_id

- product_variants.product_id joins products.product_id

- Never join order_items directly with products

==================================================

Below are some example questions and SQL queries.

""",

    suffix="""

Question:
{input}

SQL Query:

""",

    input_variables=[
        "input",
        "retrieved_context"
    ]
)

# ==========================================
# MAIN FUNCTION
# ==========================================

def run_query(question):

    # ==========================================
    # RETRIEVE RELEVANT SCHEMA CONTEXT
    # ==========================================

    retrieved_docs = retriever.invoke(question)

    retrieved_context = "\n\n".join(

        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

    # ==========================================
    # GENERATE FINAL PROMPT
    # ==========================================

    final_prompt = few_shot_prompt.format(

        input=question,

        retrieved_context=retrieved_context
    )

    # ==========================================
    # GENERATE SQL
    # ==========================================

    response = llm.invoke(final_prompt)

    sql_query = response.content.strip()

    # ==========================================
    # CLEAN SQL OUTPUT
    # ==========================================

    sql_query = sql_query.replace(
        "```sql",
        ""
    )

    sql_query = sql_query.replace(
        "```",
        ""
    )

    sql_query = sql_query.strip()

    # ==========================================
    # VALIDATE SQL
    # ==========================================

    if not validate_sql_query(sql_query):

        return {

            "query": sql_query,

            "result": "❌ Dangerous SQL query blocked."
        }

    # ==========================================
    # EXECUTE QUERY
    # ==========================================

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text(sql_query)
            )

            rows = result.fetchall()

        return {

            "query": sql_query,

            "result": rows
        }

    # ==========================================
    # HANDLE ERRORS
    # ==========================================

    except Exception as e:

        return {

            "query": sql_query,

            "result": f"❌ SQL Error: {str(e)}"
        }