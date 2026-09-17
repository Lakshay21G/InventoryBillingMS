# InventoryBillingMS

Console app for inventory and billing. Python + MySQL (`mysql.connector`).

## Features

- Add product
- View inventory
- Search product by ID
- Update product (quantity, price, name)
- Delete product
- Generate bill (multi-item, auto quantity deduction)

## Requirements

- Python 3
- MySQL server running
- `mysql-connector-python` package

```bash
pip install mysql-connector-python
```

## Database Setup

Create database `InventoryBillingMS`, then tables:

```sql
CREATE DATABASE InventoryBillingMS;
USE InventoryBillingMS;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    product_quantity INT
);

CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    bill_date DATE,
    total_bill DECIMAL(10,2)
);

CREATE TABLE bill_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT,
    product_id INT,
    product_quantity INT,
    product_price DECIMAL(10,2)
);
```

## Config

Edit connection block in `InvertoryBillingCODE.py`:

```python
mycon=my.connect(host='localhost',
                 user='root',
                 passwd='YOUR_PASSWORD',
                 database='InventoryBillingMS')
```

## Run

```bash
python InvertoryBillingCODE.py
```

Follow on-screen menu (1-7).

## Notes

- Credentials hardcoded in script now, move to env vars before sharing/deploying.
- `DELETE_PRODUCT` asks two IDs (bill item id, product id) — check prompts carefully.