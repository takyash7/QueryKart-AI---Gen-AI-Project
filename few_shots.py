few_shots = [

# ==========================================
# BRAND SALES ANALYSIS
# ==========================================

{
    'Question': 'Which brand has highest total sales revenue?',

    'SQLQuery': """
    SELECT
        b.brand_name,
        SUM(oi.quantity * oi.item_price) AS total_sales
        

    FROM order_items oi

    JOIN product_variants pv
        ON oi.variant_id = pv.variant_id

    JOIN products p
        ON pv.product_id = p.product_id

    JOIN brands b
        ON p.brand_id = b.brand_id

    GROUP BY b.brand_name

    ORDER BY total_sales DESC

    LIMIT 1;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Top selling brand displayed.'
},

# ==========================================
# CUSTOMER ANALYTICS
# ==========================================

{
    'Question': 'Show top 5 customers by total spending.',

    'SQLQuery': """
    SELECT
        c.first_name,
        c.last_name,
        SUM(o.total_amount) AS total_spending

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    GROUP BY c.customer_id

    ORDER BY total_spending DESC

    LIMIT 5;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Top customers displayed.'
},

# ==========================================
# INVENTORY ANALYSIS
# ==========================================

{
    'Question': 'How many black XL products are currently in stock?',

    'SQLQuery': """
    SELECT
        SUM(i.stock_quantity) AS total_stock

    FROM inventory i

    JOIN product_variants pv
        ON i.variant_id = pv.variant_id

    WHERE pv.color = 'Black'
    AND pv.size = 'XL';
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Current stock calculated.'
},

# ==========================================
# LOW STOCK PRODUCTS
# ==========================================

{
    'Question': 'Which products have lowest stock quantity?',

    'SQLQuery': """
    SELECT
        p.product_name,
        SUM(i.stock_quantity) AS total_stock

    FROM inventory i

    JOIN product_variants pv
        ON i.variant_id = pv.variant_id

    JOIN products p
        ON pv.product_id = p.product_id

    GROUP BY p.product_name

    ORDER BY total_stock ASC

    LIMIT 10;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Lowest stock products displayed.'
},

# ==========================================
# PAYMENT ANALYTICS
# ==========================================

{
    'Question': 'Which payment method is used most frequently?',

    'SQLQuery': """
    SELECT
        payment_method,
        COUNT(*) AS total_usage

    FROM payments

    GROUP BY payment_method

    ORDER BY total_usage DESC

    LIMIT 1;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Most used payment method displayed.'
},

# ==========================================
# CITY REVENUE ANALYSIS
# ==========================================

{
    'Question': 'Which city generates highest revenue?',

    'SQLQuery': """
    SELECT
        c.city,
        SUM(o.total_amount) AS total_revenue

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    GROUP BY c.city

    ORDER BY total_revenue DESC

    LIMIT 1;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Top revenue city displayed.'
},

# ==========================================
# DISCOUNT ANALYSIS
# ==========================================

{
    'Question': 'Which products have highest discount percentage?',

    'SQLQuery': """
    SELECT
        p.product_name,
        MAX(d.discount_percent) AS highest_discount

    FROM discounts d

    JOIN product_variants pv
        ON d.variant_id = pv.variant_id

    JOIN products p
        ON pv.product_id = p.product_id

    GROUP BY p.product_name

    ORDER BY highest_discount DESC

    LIMIT 10;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Highest discounted products displayed.'
},

# ==========================================
# MONTHLY SALES TREND
# ==========================================

{
    'Question': 'Show monthly sales revenue trend.',

    'SQLQuery': """
    SELECT
        MONTH(order_date) AS month,
        SUM(total_amount) AS monthly_sales

    FROM orders

    GROUP BY MONTH(order_date)

    ORDER BY month;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Monthly sales trend displayed.'
},

# ==========================================
# CATEGORY ANALYTICS
# ==========================================

{
    'Question': 'Which category sells the most products?',

    'SQLQuery': """
    SELECT
        c.category_name,
        SUM(oi.quantity) AS total_quantity

    FROM order_items oi

    JOIN product_variants pv
        ON oi.variant_id = pv.variant_id

    JOIN products p
        ON pv.product_id = p.product_id

    JOIN categories c
        ON p.category_id = c.category_id

    GROUP BY c.category_name

    ORDER BY total_quantity DESC

    LIMIT 1;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Best selling category displayed.'
},

# ==========================================
# CUSTOMER ORDER FREQUENCY
# ==========================================

{
    'Question': 'Which customer placed the highest number of orders?',

    'SQLQuery': """
    SELECT
        c.first_name,
        c.last_name,
        COUNT(o.order_id) AS total_orders

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    GROUP BY c.customer_id

    ORDER BY total_orders DESC

    LIMIT 1;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Customer with highest orders displayed.'
},

# ==========================================
# INVENTORY VALUE
# ==========================================

{
    'Question': 'What is total inventory value of all products?',

    'SQLQuery': """
    SELECT
        SUM(i.stock_quantity * pv.price)
        AS total_inventory_value

    FROM inventory i

    JOIN product_variants pv
        ON i.variant_id = pv.variant_id;
    """,

    'SQLResult': 'Result of SQL query',

    'Answer': 'Total inventory value calculated.'
}

]