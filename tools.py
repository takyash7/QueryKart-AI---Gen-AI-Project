from sqlalchemy import text

from langchain_helper import engine

# ==========================================
# SQL EXECUTION FUNCTION
# ==========================================

def execute_sql_query(query):

    """
    Execute SQL query on MySQL database.
    """

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text(query)
            )

            rows = result.fetchall()

            # Convert Row objects to tuples

            clean_rows = [
                tuple(row)
                for row in rows
            ]

        return clean_rows

    except Exception as e:

        return f"SQL Error: {str(e)}"