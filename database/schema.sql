CREATE DATABASE querykart_ai;

USE querykart_ai;

-- =========================
-- BRANDS TABLE
-- =========================

CREATE TABLE brands (
    brand_id INT PRIMARY KEY AUTO_INCREMENT,
    brand_name VARCHAR(100) UNIQUE NOT NULL
);

-- =========================
-- CATEGORIES TABLE
-- =========================

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

-- =========================
-- PRODUCTS TABLE
-- =========================

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    brand_id INT,
    category_id INT,
    description TEXT,
    launch_date DATE,

    FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- =========================
-- PRODUCT VARIANTS
-- =========================

CREATE TABLE product_variants (
    variant_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    size ENUM('XS','S','M','L','XL','XXL'),
    color VARCHAR(50),
    price DECIMAL(10,2),

    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);

-- =========================
-- INVENTORY TABLE
-- =========================

CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT,
    stock_quantity INT DEFAULT 0,
    warehouse_location VARCHAR(100),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (variant_id)
    REFERENCES product_variants(variant_id)
);

-- =========================
-- DISCOUNTS TABLE
-- =========================

CREATE TABLE discounts (
    discount_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT,
    discount_percent DECIMAL(5,2),
    start_date DATE,
    end_date DATE,

    FOREIGN KEY (variant_id)
    REFERENCES product_variants(variant_id)
);

-- =========================
-- CUSTOMERS TABLE
-- =========================

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender ENUM('Male','Female','Other'),
    email VARCHAR(255) UNIQUE,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    registration_date DATE
);

-- =========================
-- ORDERS TABLE
-- =========================

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATETIME,
    total_amount DECIMAL(10,2),
    order_status ENUM(
        'Pending',
        'Shipped',
        'Delivered',
        'Cancelled'
    ),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

-- =========================
-- ORDER ITEMS
-- =========================

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    variant_id INT,
    quantity INT,
    item_price DECIMAL(10,2),

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    FOREIGN KEY (variant_id)
    REFERENCES product_variants(variant_id)
);

-- =========================
-- PAYMENTS TABLE
-- =========================

CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    payment_method ENUM(
        'UPI',
        'Credit Card',
        'Debit Card',
        'Cash On Delivery',
        'Net Banking'
    ),

    payment_status ENUM(
        'Paid',
        'Pending',
        'Failed'
    ),

    payment_date DATETIME,

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);

-- =========================
-- SUPPLIERS TABLE
-- =========================

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(255),
    contact_email VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);

-- =========================
-- PRODUCT SUPPLIERS TABLE
-- =========================

CREATE TABLE product_suppliers (
    product_supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    supplier_id INT,

    FOREIGN KEY (product_id)
    REFERENCES products(product_id),

    FOREIGN KEY (supplier_id)
    REFERENCES suppliers(supplier_id)
);