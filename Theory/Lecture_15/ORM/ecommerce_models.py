"""
Lecture 15 - PBL Activity & Lab Exercise Task 1:
E-Commerce System Data Modeling and Implementation using SQLAlchemy ORM.

Entities:
  - Customer: The user/buyer in the system
  - Product: Catalog item with price, stock, category
  - Cart & CartItem: 1:1 with Customer, contains active shopping items
  - Order & OrderItem: 1:M with Customer, snapshots placed orders and purchase prices
"""

from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///ecommerce.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# ==============================================================================
# 1. E-Commerce ORM Models
# ==============================================================================

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships:
    # 1:1 Customer to Cart
    cart = relationship("Cart", back_populates="customer", uselist=False, cascade="all, delete-orphan")
    # 1:M Customer to Orders
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0, nullable=False)

    __table_args__ = (
        CheckConstraint("price >= 0", name="check_positive_price"),
        CheckConstraint("stock >= 0", name="check_non_negative_stock"),
    )

    # Relationships
    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})>"


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="cart")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cart(id={self.id}, customer_id={self.customer_id}, total_items={len(self.items)})>"


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)

    __table_args__ = (
        CheckConstraint("quantity > 0", name="check_positive_quantity"),
    )

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product", back_populates="cart_items")

    def __repr__(self):
        return f"<CartItem(id={self.id}, product='{self.product.name if self.product else self.product_id}', qty={self.quantity})>"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(30), default="PENDING")  # PENDING, PAID, SHIPPED, DELIVERED, CANCELLED
    total_amount = Column(Float, default=0.0)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, status='{self.status}', total={self.total_amount})>"


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem(id={self.id}, product='{self.product.name if self.product else self.product_id}', qty={self.quantity}, price={self.price_at_purchase})>"


# ==============================================================================
# 2. Database Initialization
# ==============================================================================
def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("[OK] E-Commerce Database schema created successfully.")


# ==============================================================================
# 3. Demonstration: Shopping Cart & Order Lifecycle
# ==============================================================================
def run_ecommerce_demo():
    print("=" * 70)
    print("PBL ACTIVITY: E-COMMERCE DATA MODEL & WORKFLOW DEMONSTRATION")
    print("=" * 70)

    # 1. Create Products
    print("\n--- 1. Seed Products ---")
    p1 = Product(name="MacBook Air M3", category="Electronics", price=1149.00, stock=10)
    p2 = Product(name="Wireless Noise-Canceling Headphones", category="Audio", price=199.99, stock=25)
    p3 = Product(name="Mechanical Keyboard", category="Accessories", price=89.50, stock=40)
    session.add_all([p1, p2, p3])
    session.commit()
    print(f"Added products: {p1.name}, {p2.name}, {p3.name}")

    # 2. Create Customer with an Empty Cart
    print("\n--- 2. Create Customer & Active Cart ---")
    customer = Customer(
        name="Rohit Verma",
        email="rohit.verma@example.com",
        phone="+91-9876543210",
        address="221B Baker Street, Dehradun"
    )
    customer.cart = Cart()  # 1:1 relationship
    session.add(customer)
    session.commit()
    print(f"Customer registered: {customer}")
    print(f"Active Cart created: {customer.cart}")

    # 3. Add Items to Customer's Cart
    print("\n--- 3. Customer Adds Items to Cart ---")
    cart_item1 = CartItem(cart_id=customer.cart.id, product_id=p1.id, quantity=1)
    cart_item2 = CartItem(cart_id=customer.cart.id, product_id=p3.id, quantity=2)
    session.add_all([cart_item1, cart_item2])
    session.commit()
    
    session.refresh(customer.cart)
    print(f"Cart contents for {customer.name}:")
    for item in customer.cart.items:
        print(f"  - {item.product.name} x {item.quantity} @ ${item.product.price:.2f}")

    # 4. Checkout: Convert Cart to Order
    print("\n--- 4. Checkout Workflow: Placing Order ---")
    total = sum(item.quantity * item.product.price for item in customer.cart.items)
    new_order = Order(customer_id=customer.id, status="PAID", total_amount=total)
    session.add(new_order)
    session.flush()  # Generate new_order.id

    for item in customer.cart.items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_purchase=item.product.price
        )
        session.add(order_item)
        # Deduct inventory stock
        item.product.stock -= item.quantity

    # Clear shopping cart after successful checkout
    session.query(CartItem).filter_by(cart_id=customer.cart.id).delete()
    session.commit()
    print(f"Order #{new_order.id} placed successfully! Total: ${new_order.total_amount:.2f}")
    print(f"Updated Stock: {p1.name} = {p1.stock}, {p3.name} = {p3.stock}")

    # 5. Read Customer Orders with Items
    print("\n--- 5. Query Customer Order History ---")
    orders = session.query(Order).filter_by(customer_id=customer.id).all()
    for o in orders:
        print(f"Order #{o.id} - Date: {o.order_date.strftime('%Y-%m-%d %H:%M:%S')} - Status: {o.status}")
        for oi in o.order_items:
            print(f"  Item: {oi.product.name} | Qty: {oi.quantity} | Unit Price: ${oi.price_at_purchase:.2f}")

    print("\n" + "=" * 70)
    print("E-COMMERCE DATA MODEL DEMONSTRATION COMPLETE")
   


if __name__ == "__main__":
    init_db()
    run_ecommerce_demo()
