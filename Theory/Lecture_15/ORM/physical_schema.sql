-- =============================================================================
-- Lecture 15: Physical Data Model (PostgreSQL / Relational DBMS)
-- Topic: Concrete Table Definitions, Constraints, Indexes & Optimizations
-- =============================================================================

-- Clean up existing tables
DROP TABLE IF EXISTS enrollments CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS faculties CASCADE;
DROP TABLE IF EXISTS departments CASCADE;

-- -----------------------------------------------------------------------------
-- 1. Departments Table
-- -----------------------------------------------------------------------------
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    building VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 2. Faculty Table
-- -----------------------------------------------------------------------------
CREATE TABLE faculties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    designation VARCHAR(50),
    department_id INTEGER NOT NULL REFERENCES departments(id) ON DELETE RESTRICT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 3. Students Table (Lecture 15 Slide 4 Example Extended)
-- -----------------------------------------------------------------------------
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    branch VARCHAR(50) NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    department_id INTEGER REFERENCES departments(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Constraint: enrollment date cannot be in the future
    CONSTRAINT chk_enrollment_date CHECK (enrollment_date <= CURRENT_DATE)
);

-- B-Tree Index on frequently queried branch column (Slide 4)
CREATE INDEX idx_students_branch ON students(branch);
CREATE INDEX idx_students_email ON students(email);

-- -----------------------------------------------------------------------------
-- 4. Courses Table
-- -----------------------------------------------------------------------------
CREATE TABLE courses (
    id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    credits INTEGER NOT NULL,
    department_id INTEGER REFERENCES departments(id) ON DELETE CASCADE,
    faculty_id INTEGER REFERENCES faculties(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Constraint: credits must be between 1 and 6 (Slide 5)
    CONSTRAINT chk_course_credits CHECK (credits BETWEEN 1 AND 6)
);

CREATE INDEX idx_courses_dept ON courses(department_id);

-- -----------------------------------------------------------------------------
-- 5. Enrollments Table (Association Table for Student M:N Courses)
-- -----------------------------------------------------------------------------
CREATE TABLE enrollments (
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    course_id VARCHAR(10) NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    semester VARCHAR(20) NOT NULL,
    grade VARCHAR(2),
    enrolled_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (student_id, course_id),
    
    -- Constraint: Valid letter grades only (Slide 5)
    CONSTRAINT chk_valid_grade CHECK (
        grade IS NULL OR grade IN ('A+', 'A', 'B+', 'B', 'C+', 'C', 'D', 'F')
    )
);

CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);

-- =============================================================================
-- E-COMMERCE PHYSICAL DATA MODEL (PBL Activity & Lab Exercise 1)
-- =============================================================================

DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS cart_items CASCADE;
DROP TABLE IF EXISTS carts CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS customers CASCADE;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_category ON products(category);

CREATE TABLE carts (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL UNIQUE REFERENCES customers(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cart_items (
    id SERIAL PRIMARY KEY,
    cart_id INTEGER NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK (quantity > 0),
    UNIQUE(cart_id, product_id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE RESTRICT,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'PAID', 'SHIPPED', 'DELIVERED', 'CANCELLED')),
    total_amount NUMERIC(10, 2) NOT NULL DEFAULT 0.00 CHECK (total_amount >= 0)
);

CREATE INDEX idx_orders_customer ON orders(customer_id);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price_at_purchase NUMERIC(10, 2) NOT NULL CHECK (price_at_purchase >= 0)
);
