import random
from faker import Faker
import mysql.connector

fake = Faker()

# =========================
# DATABASE CONNECTION
# =========================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="querykart_ai"
)

cursor = conn.cursor()

# =========================
# BRANDS
# =========================

brands = [
    "Nike",
    "Adidas",
    "Puma",
    "Levi's",
    "Under Armour",
    "Zara",
    "H&M",
    "Uniqlo",
    "Reebok",
    "Van Heusen"
]

for brand in brands:
    cursor.execute(
        "INSERT INTO brands (brand_name) VALUES (%s)",
        (brand,)
    )

# =========================
# CATEGORIES
# =========================

categories = [
    "T-Shirts",
    "Hoodies",
    "Jeans",
    "Shirts",
    "Sneakers",
    "Jackets"
]

for category in categories:
    cursor.execute(
        "INSERT INTO categories (category_name) VALUES (%s)",
        (category,)
    )

# =========================
# PRODUCTS + VARIANTS
# =========================

colors = [
    "Black",
    "White",
    "Blue",
    "Red",
    "Green"
]

sizes = [
    "XS",
    "S",
    "M",
    "L",
    "XL"
]

for i in range(200):

    product_name = (
        fake.word().capitalize()
        + " Fashion"
    )

    brand_id = random.randint(1, 10)

    category_id = random.randint(1, 6)

    description = fake.text(max_nb_chars=100)

    launch_date = fake.date_between(
        start_date='-2y',
        end_date='today'
    )

    cursor.execute("""
        INSERT INTO products
        (
            product_name,
            brand_id,
            category_id,
            description,
            launch_date
        )
        VALUES (%s,%s,%s,%s,%s)
    """, (
        product_name,
        brand_id,
        category_id,
        description,
        launch_date
    ))

    product_id = cursor.lastrowid

    # VARIANTS

    for color in colors:
        for size in sizes:

            price = random.randint(
                500,
                5000
            )

            cursor.execute("""
                INSERT INTO product_variants
                (
                    product_id,
                    size,
                    color,
                    price
                )
                VALUES (%s,%s,%s,%s)
            """, (
                product_id,
                size,
                color,
                price
            ))

            variant_id = cursor.lastrowid

            # INVENTORY

            stock = random.randint(0, 300)

            cursor.execute("""
                INSERT INTO inventory
                (
                    variant_id,
                    stock_quantity,
                    warehouse_location
                )
                VALUES (%s,%s,%s)
            """, (
                variant_id,
                stock,
                fake.city()
            ))

            # DISCOUNTS

            discount = random.choice([
                5,
                10,
                15,
                20,
                25,
                30
            ])

            cursor.execute("""
                INSERT INTO discounts
                (
                    variant_id,
                    discount_percent,
                    start_date,
                    end_date
                )
                VALUES (%s,%s,%s,%s)
            """, (
                variant_id,
                discount,
                fake.date_this_year(),
                fake.date_this_year()
            ))

# =========================
# CUSTOMERS
# =========================

for i in range(500):

    gender = random.choice([
        "Male",
        "Female",
        "Other"
    ])

    cursor.execute("""
        INSERT INTO customers
        (
            first_name,
            last_name,
            gender,
            email,
            city,
            state,
            country,
            registration_date
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        fake.first_name(),
        fake.last_name(),
        gender,
        fake.unique.email(),
        fake.city(),
        fake.state(),
        "India",
        fake.date_between(
            start_date='-3y',
            end_date='today'
        )
    ))

# =========================
# ORDERS
# =========================

for i in range(1000):

    customer_id = random.randint(
        1,
        500
    )

    total_amount = random.randint(
        1000,
        20000
    )

    status = random.choice([
        "Pending",
        "Shipped",
        "Delivered",
        "Cancelled"
    ])

    order_date = fake.date_time_between(
        start_date='-1y',
        end_date='now'
    )

    cursor.execute("""
        INSERT INTO orders
        (
            customer_id,
            order_date,
            total_amount,
            order_status
        )
        VALUES (%s,%s,%s,%s)
    """, (
        customer_id,
        order_date,
        total_amount,
        status
    ))

    order_id = cursor.lastrowid

    # ORDER ITEMS

    for j in range(random.randint(1,5)):

        variant_id = random.randint(
            1,
            5000
        )

        quantity = random.randint(
            1,
            4
        )

        item_price = random.randint(
            500,
            5000
        )

        cursor.execute("""
            INSERT INTO order_items
            (
                order_id,
                variant_id,
                quantity,
                item_price
            )
            VALUES (%s,%s,%s,%s)
        """, (
            order_id,
            variant_id,
            quantity,
            item_price
        ))

    # PAYMENTS

    payment_method = random.choice([
        "UPI",
        "Credit Card",
        "Debit Card",
        "Cash On Delivery",
        "Net Banking"
    ])

    payment_status = random.choice([
        "Paid",
        "Pending",
        "Failed"
    ])

    cursor.execute("""
        INSERT INTO payments
        (
            order_id,
            payment_method,
            payment_status,
            payment_date
        )
        VALUES (%s,%s,%s,%s)
    """, (
        order_id,
        payment_method,
        payment_status,
        order_date
    ))

# =========================
# SAVE
# =========================

conn.commit()

print("🔥 QueryKart AI dataset generated successfully!")

cursor.close()
conn.close()