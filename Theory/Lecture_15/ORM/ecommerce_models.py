"""
Lecture 15 - PBL Activity & Lab Exercise Task 1:
E-Commerce System Data Modeling and Implementation using SQLAlchemy ORM.
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

# ------------------------------------------------------------------------------
# E-Commerce Models
# ------------------------------------------------------------------------------

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)

    cart = relationship("Cart", back_populates="customer", uselist=False, cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer: {self.name}>"


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

    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"<Product: {self.name} (${self.price:.2f})>"


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="cart")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cart of Customer {self.customer_id}>"


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


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(30), default="PENDING")
    total_amount = Column(Float, default=0.0)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order #{self.id}: {self.status} (${self.total_amount:.2f})>"


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("E-Commerce database tables created successfully.")


def run_ecommerce():
    # 1. Seed Products
    p1 = Product(name="MacBook Air M3", category="Electronics", price=1149.00, stock=10)
    p2 = Product(name="Wireless Noise-Canceling Headphones", category="Audio", price=199.99, stock=25)
    p3 = Product(name="Mechanical Keyboard", category="Accessories", price=89.50, stock=40)
    session.add_all([p1, p2, p3])
    session.commit()
    print("Added products: MacBook Air M3, Wireless Headphones, Mechanical Keyboard successfully.")

    # 2. Register Customer with an empty cart
    customer = Customer(
        name="Rohit Verma",
        email="rohit.verma@example.com",
        phone="+91-9876543210",
        address="221B Baker Street, Dehradun"
    )
    customer.cart = Cart()
    session.add(customer)
    session.commit()
    print(f"Registered customer: {customer.name} with an active cart successfully.")

    # 3. Add Items to Cart
    cart_item1 = CartItem(cart_id=customer.cart.id, product_id=p1.id, quantity=1)
    cart_item2 = CartItem(cart_id=customer.cart.id, product_id=p3.id, quantity=2)
    session.add_all([cart_item1, cart_item2])
    session.commit()
    print(f"Added items to {customer.name}'s cart successfully:")
    for item in customer.cart.items:
        print(f"  - {item.product.name} (Qty: {item.quantity}, Price: ${item.product.price:.2f})")

    # 4. Checkout: Convert Cart to Order
    total = sum(item.quantity * item.product.price for item in customer.cart.items)
    new_order = Order(customer_id=customer.id, status="PAID", total_amount=total)
    session.add(new_order)
    session.flush()

    for item in customer.cart.items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_purchase=item.product.price
        )
        session.add(order_item)
        item.product.stock -= item.quantity

    session.query(CartItem).filter_by(cart_id=customer.cart.id).delete()
    session.commit()
    print(f"Order #{new_order.id} placed successfully. Total: ${new_order.total_amount:.2f}")
    print(f"Inventory stock updated successfully: {p1.name} = {p1.stock}, {p3.name} = {p3.stock}")

    # 5. Query Customer Orders
    orders = session.query(Order).filter_by(customer_id=customer.id).all()
    print(f"Retrieved order history for {customer.name} successfully:")
    for o in orders:
        items_desc = ", ".join([f"{oi.product.name} x{oi.quantity}" for oi in o.order_items])
        print(f"  - Order #{o.id} [{o.status}]: {items_desc}")


if __name__ == "__main__":
    init_db()
    run_ecommerce()
