BLOCKED_KEYWORDS = [
    "DELETE",
    "DROP",
    "UPDATE",
    "ALTER",
    "TRUNCATE",
    "INSERT",
    "CREATE"
]


def validate_sql_query(query):

    query_upper = query.upper()

    for keyword in BLOCKED_KEYWORDS:

        if keyword in query_upper:
            return False

    return True