from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy import text

from langchain_groq import ChatGroq

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# DATABASE CONFIG
# ==========================================

DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "querykart_ai"

# ==========================================
# DATABASE ENGINE
# ==========================================

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
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
# MAIN FUNCTION
# ==========================================

def run_query(question):

    prompt = f"""

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

==================================================
DATABASE SCHEMA
==================================================

Table: brands
Columns:
- brand_id
- brand_name

Table: categories
Columns:
- category_id
- category_name

Table: products
Columns:
- product_id
- product_name
- brand_id
- category_id
- description
- launch_date

Table: product_variants
Columns:
- variant_id
- product_id
- size
- color
- price

Table: inventory
Columns:
- inventory_id
- variant_id
- stock_quantity
- warehouse_location
- last_updated

Table: discounts
Columns:
- discount_id
- variant_id
- discount_percent
- start_date
- end_date

Table: customers
Columns:
- customer_id
- first_name
- last_name
- gender
- email
- city
- state
- country
- registration_date

Table: orders
Columns:
- order_id
- customer_id
- order_date
- total_amount
- order_status

Table: order_items
Columns:
- order_item_id
- order_id
- variant_id
- quantity
- item_price

Table: payments
Columns:
- payment_id
- order_id
- payment_method
- payment_status
- payment_date

Table: suppliers
Columns:
- supplier_id
- supplier_name
- contact_email
- city
- country

Table: product_suppliers
Columns:
- product_supplier_id
- product_id
- supplier_id

==================================================
TABLE RELATIONSHIPS
==================================================

products.brand_id = brands.brand_id

products.category_id = categories.category_id

product_variants.product_id = products.product_id

inventory.variant_id = product_variants.variant_id

discounts.variant_id = product_variants.variant_id

orders.customer_id = customers.customer_id

order_items.order_id = orders.order_id

order_items.variant_id = product_variants.variant_id

payments.order_id = orders.order_id

product_suppliers.product_id = products.product_id

product_suppliers.supplier_id = suppliers.supplier_id

==================================================
IMPORTANT JOIN RULES
==================================================

order_items.variant_id joins with product_variants.variant_id

product_variants.product_id joins with products.product_id

Never join order_items directly with products

==================================================

Question:
{question}

SQL Query:

"""

    # ==========================================
    # GENERATE SQL
    # ==========================================

    response = llm.invoke(prompt)

    sql_query = response.content.strip()

    # ==========================================
    # CLEAN OUTPUT
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
    # EXECUTE QUERY
    # ==========================================

    with engine.connect() as connection:

        result = connection.execute(
            text(sql_query)
        )

        rows = result.fetchall()

    # ==========================================
    # RETURN RESULT
    # ==========================================

    return {
        "query": sql_query,
        "result": rows
    }