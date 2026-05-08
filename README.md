# 🛒 QueryKart AI: Talk to Your Retail Database

QueryKart AI is an end-to-end Generative AI project that allows users to interact with a retail MySQL database using natural language.

The system converts English questions into SQL queries using Large Language Models (LLMs), executes them on the database, and returns accurate business insights in real time.

Users can ask questions related to:

* Sales
* Inventory
* Customers
* Revenue
* Payments
* Orders
* Product Analytics

without writing SQL manually.

---

# 🚀 Project Highlights

* QueryKart AI is an AI-powered retail database assistant
* Retail data is stored in a MySQL database
* Users can ask questions in natural language
* The system automatically generates SQL queries
* Queries are executed on the database in real time
* Supports business analytics and database intelligence

---

# 🧠 Technologies Used

* Groq Llama 3.3 70B
* Python
* LangChain
* Streamlit
* SQLAlchemy
* MySQL
* Few Shot Learning
* Prompt Engineering

---

# 💡 Sample Questions

* Which category sells the most products?
* Which brand generates highest revenue?
* Show top 5 customers by total spending
* Which products have lowest stock quantity?
* Which payment method is used most frequently?
* What is total inventory value?
* Which city generates highest revenue?

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/takyash7/QueryKart-AI---Gen-AI-Project.git
```

---

## 2. Navigate to Project Folder

```bash
cd QueryKartAI
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

MYSQLHOST=your_host
MYSQLPORT=your_port
MYSQLUSER=your_user
MYSQLPASSWORD=your_password
MYSQLDATABASE=your_database
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📂 Project Structure

* `app.py` → Landing page
* `langchain_helper.py` → AI query generation logic
* `few_shots.py` → Few-shot training examples
* `requirements.txt` → Required packages
* `database/schema.sql` → Database schema
* `database/generate_data.py` → Dataset generation script
* `database/database.sql` → Full database export
* `pages/` → Multi-page Streamlit UI

---

# 🎯 Project Objective

The objective of QueryKart AI is to simplify database interaction using Generative AI and enable users to retrieve business insights using natural language queries.

---

# 👨‍💻 Developer

Created by Yash Tak
