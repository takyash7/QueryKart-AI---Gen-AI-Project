from dotenv import load_dotenv

import os

from langchain_groq import ChatGroq

from retriever import retriever

from tools import execute_sql_query

from few_shots import few_shots

from langchain_core.prompts import (

    PromptTemplate,
    FewShotPromptTemplate
)

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# LLM
# ==========================================

llm = ChatGroq(

    groq_api_key=os.environ["GROQ_API_KEY"],

    model_name="llama-3.3-70b-versatile",

    temperature=0.1
)

# ==========================================
# QUESTION VALIDATOR
# ==========================================

def is_valid_business_question(question):

    validation_prompt = f"""

You are a strict AI security classifier.

Your task:
Determine whether the user question is specifically asking about:

- retail analytics
- SQL queries
- sales reports
- customer analytics
- inventory analysis
- payment analysis
- product analytics
- supplier analytics
- database information

IMPORTANT:

Reject:
- jokes
- trivia
- cricket
- IPL
- capitals
- movies
- songs
- coding theory
- general knowledge
- casual chat
- unrelated questions

Examples:

Question: Top selling products
Answer: VALID

Question: Revenue by category
Answer: VALID

Question: Tell me a joke
Answer: INVALID

Question: Who won IPL 2010?
Answer: INVALID

Question: What is capital of India?
Answer: INVALID

Question: List low stock products
Answer: VALID

Return ONLY one word:

VALID

OR

INVALID

Question:
{question}

"""

    validation_response = llm.invoke(
        validation_prompt
    )

    result = validation_response.content.strip()

    return result == "VALID"

# ==========================================
# EXAMPLE PROMPT
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
# FEW SHOT PROMPT
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
# MAIN AGENT FUNCTION
# ==========================================

def ask_agent(question):

    # ======================================
    # VALIDATE QUESTION
    # ======================================

    if not is_valid_business_question(question):

        return {

            "query": "No SQL Generated",

            "result": "Please ask retail database related questions only."
        }

    # ======================================
    # RETRIEVE RELEVANT CONTEXT
    # ======================================

    retrieved_docs = retriever.invoke(
        question
    )

    retrieved_context = "\n\n".join(

        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

    # ======================================
    # CREATE FINAL PROMPT
    # ======================================

    final_prompt = few_shot_prompt.format(

        input=question,

        retrieved_context=retrieved_context
    )

    # ======================================
    # GENERATE SQL
    # ======================================

    response = llm.invoke(
        final_prompt
    )

    sql_query = response.content.strip()

    # ======================================
    # CLEAN SQL
    # ======================================

    sql_query = sql_query.replace(
        "```sql",
        ""
    )

    sql_query = sql_query.replace(
        "```",
        ""
    )

    sql_query = sql_query.strip()

    # ======================================
    # EXECUTE SQL QUERY
    # ======================================

    result = execute_sql_query(
        sql_query
    )

    # ======================================
    # FINAL RESPONSE
    # ======================================

    return {

        "query": sql_query,

        "result": result
    }