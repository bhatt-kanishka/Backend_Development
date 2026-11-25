-- Assignment 2 — PostgreSQL as SQL + NoSQL (JSONB)
-- Practical work. Run these statements in psql against a practice database.

-- ---------------------------------------------------------------------------
-- Task 1 & 2 — Schema and seed data
-- ---------------------------------------------------------------------------
CREATE TABLE products (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  category VARCHAR(50) NOT NULL,
  price NUMERIC(10,2) NOT NULL,
  attributes JSONB
);

INSERT INTO products (name, category, price, attributes) VALUES
('Clean Code', 'Books', 499.00, '{"author":"Robert C. Martin","pages":464}'),
('Atomic Habits', 'Books', 399.00, '{"author":"James Clear","pages":320}'),
('Wireless Mouse', 'Electronics', 799.00, '{"wireless":true,"dpi":1600}'),
('USB Keyboard', 'Electronics', 999.00, '{"wireless":false,"keys":104}'),
('Cotton T-Shirt', 'Clothing', 599.00, '{"size":"M","color":"Blue"}');

-- ---------------------------------------------------------------------------
-- Task 3 — Query one specific attribute in each category
-- ---------------------------------------------------------------------------
SELECT name, attributes->>'author' AS author
FROM products
WHERE category = 'Books' AND attributes->>'author' = 'James Clear';
-- Atomic Habits

SELECT name, attributes->>'dpi' AS dpi
FROM products
WHERE category = 'Electronics' AND (attributes->>'dpi')::integer >= 1600;
-- Wireless Mouse

SELECT name, attributes->>'size' AS size
FROM products
WHERE category = 'Clothing' AND attributes->>'size' = 'M';
-- Cotton T-Shirt

-- ---------------------------------------------------------------------------
-- Task 4 — JSONB containment
-- ---------------------------------------------------------------------------
SELECT name FROM products
WHERE attributes @> '{"wireless":true}'::jsonb;
-- Wireless Mouse

-- ---------------------------------------------------------------------------
-- Task 5 — Add a property without replacing other attributes
-- ---------------------------------------------------------------------------
UPDATE products
SET attributes = attributes || '{"discount_pct":10}'::jsonb
WHERE name = 'Wireless Mouse';

SELECT name, attributes FROM products WHERE name = 'Wireless Mouse';
-- wireless, dpi and discount_pct are present together

-- ---------------------------------------------------------------------------
-- Task 6 — Compare query plans before and after indexing
-- Run the first four EXPLAIN ANALYZE statements before creating the index,
-- then create the index and rerun the same statements.
-- ---------------------------------------------------------------------------
EXPLAIN ANALYZE SELECT name FROM products
WHERE category = 'Books' AND attributes->>'author' = 'James Clear';
EXPLAIN ANALYZE SELECT name FROM products
WHERE category = 'Electronics' AND (attributes->>'dpi')::integer >= 1600;
EXPLAIN ANALYZE SELECT name FROM products
WHERE category = 'Clothing' AND attributes->>'size' = 'M';
EXPLAIN ANALYZE SELECT name FROM products
WHERE attributes @> '{"wireless":true}'::jsonb;

CREATE INDEX idx_products_attributes ON products USING GIN (attributes);

EXPLAIN ANALYZE SELECT name FROM products
WHERE category = 'Books' AND attributes->>'author' = 'James Clear';
EXPLAIN ANALYZE SELECT name FROM products
WHERE category = 'Electronics' AND (attributes->>'dpi')::integer >= 1600;
EXPLAIN ANALYZE SELECT name FROM products
WHERE category = 'Clothing' AND attributes->>'size' = 'M';
EXPLAIN ANALYZE SELECT name FROM products
WHERE attributes @> '{"wireless":true}'::jsonb;
