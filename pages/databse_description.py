
import streamlit as st

st.set_page_config(
    page_title="Database Description",
    page_icon="🗂️",
    layout="wide"
)

st.title("🗂️ Database Description")

st.markdown("---")

st.markdown("""

# 🛒 Retail Database Overview

The QueryKart AI database is designed for a retail
e-commerce environment.

It stores information related to:

- Products
- Brands
- Categories
- Customers
- Orders
- Inventory
- Suppliers
- Payments
- Discounts

The database is relational and normalized with
multiple interconnected tables.

""")

st.markdown("---")

# =====================================
# TABLE DETAILS
# =====================================

st.markdown("## 📦 Product Management")

st.markdown("""

### Products Table
Stores product information such as:

- Product Name
- Brand
- Category
- Description
- Launch Date

### Product Variants Table
Stores product variations including:

- Size
- Color
- Price

""")

st.markdown("---")

st.markdown("## 🏷️ Brand & Category Management")

st.markdown("""

### Brands Table
Contains brand names such as:

- Nike
- Adidas
- Puma
- Zara
- Levi's

### Categories Table
Contains categories such as:

- T-Shirts
- Hoodies
- Shoes
- Jackets
- Jeans

""")

st.markdown("---")

st.markdown("## 📦 Inventory Management")

st.markdown("""

Inventory table tracks:

- Stock quantity
- Warehouse location
- Last updated records

This helps in stock monitoring
and low inventory detection.

""")

st.markdown("---")

st.markdown("## 👥 Customer Management")

st.markdown("""

Customer table stores:

- Customer names
- Gender
- Email
- City
- State
- Country
- Registration dates

Used for customer analytics
and purchasing behavior analysis.

""")

st.markdown("---")

st.markdown("## 🛒 Order Management")

st.markdown("""

Orders and Order Items tables store:

- Order history
- Purchased products
- Product quantity
- Order amount
- Order status

Used for revenue and sales analytics.

""")

st.markdown("---")

st.markdown("## 💳 Payment Management")

st.markdown("""

Payment table stores:

- Payment methods
- Payment status
- Payment dates

Supported methods:

- UPI
- Credit Card
- Debit Card
- Cash on Delivery

""")

st.markdown("---")

st.markdown("## 🚚 Supplier Management")

st.markdown("""

Supplier tables manage:

- Supplier information
- Product suppliers
- Supplier locations

Useful for supply chain analytics.

""")

st.markdown("---")

st.markdown("## 🧠 AI Capabilities")

st.markdown("""

QueryKart AI supports:

✅ Natural Language to SQL

✅ Business Analytics

✅ Inventory Analysis

✅ Revenue Intelligence

✅ Customer Insights

✅ AI Generated SQL Queries

✅ Schema Aware Query Generation

""")

st.markdown("---")

st.success("✅ Database Connected Successfully")

