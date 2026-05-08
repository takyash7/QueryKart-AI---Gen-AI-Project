import streamlit as st
import pandas as pd

from langchain_helper import run_query

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="QueryKart AI",
    page_icon="🛒",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.stButton button {
    width: 100%;
    height: 3em;
    font-size: 18px;
    border-radius: 10px;
}

.result-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    font-size: 24px;
    font-weight: bold;
    color: #22c55e;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.title("🛒 QueryKart AI")

st.subheader(
    "AI Powered Retail Database Assistant"
)

st.markdown("---")

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 Features")

st.sidebar.info("""

✅ Natural Language to SQL

✅ Sales Analytics

✅ Inventory Tracking

✅ Customer Insights

✅ Revenue Intelligence

✅ Payment Analysis

✅ AI Generated SQL Queries

""")

st.sidebar.markdown("---")

st.sidebar.caption(
    "Built with Groq + Llama3 + MySQL"
)

# =====================================
# SAMPLE QUESTIONS
# =====================================

with st.expander("💡 Sample Questions"):

    st.markdown("""

### 🛍️ Sales Queries

- Which category sells the most products?

- Which brand has highest total sales revenue?

- Which payment method is used most frequently?

---

### 👥 Customer Analytics

- Show top 5 customers by total spending

- Which customer placed the highest number of orders?

---

### 📦 Inventory Analytics

- Which products have lowest stock quantity?

- How many black XL products are in stock?

---

### 💰 Revenue Analytics

- Which city generates highest revenue?

- What is total inventory value?

""")

# =====================================
# INPUT SECTION
# =====================================

question = st.text_input(
    "Ask your business question:"
)

submit = st.button(
    "🚀 Generate Answer"
)

# =====================================
# PROCESS QUERY
# =====================================

if submit and question:

    try:

        with st.spinner(
            "Generating SQL and fetching results..."
        ):

            response = run_query(question)

            query = response["query"]

            result = response["result"]

            st.success(
                "✅ Query Executed Successfully"
            )

            # =================================
            # SQL QUERY DISPLAY
            # =================================

            st.markdown("## 🧠 Generated SQL")

            st.code(
                query,
                language="sql"
            )

            # =================================
            # RESULT DISPLAY
            # =================================

            st.markdown("## 📊 Result")

            if len(result) == 0:

                st.warning(
                    "No data found."
                )

            elif len(result) == 1 and len(result[0]) == 1:

                st.markdown(
                    f"""
                    <div class="result-box">
                        {result[0][0]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                df = pd.DataFrame(result)

                st.dataframe(
                    df,
                    use_container_width=True
                )

    except Exception as e:

        st.error(
            "❌ Error while processing query"
        )

        st.exception(e)

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "QueryKart AI • Final Year GenAI Project"
)