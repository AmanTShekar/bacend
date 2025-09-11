from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # ✅ import Base only

# --- USER MODEL ---
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")


# --- CATEGORY MODEL ---
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


# --- OFFER MODEL ---
class Offer(Base):
    __tablename__ = "offers"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    discount = Column(Float, nullable=False)


# --- PRODUCT MODEL ---
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
    image = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    offer_id = Column(Integer, ForeignKey("offers.id"), nullable=True)

    # Relationships
    category = relationship("Category", backref="products")
    offer = relationship("Offer", backref="products")


# --- ORDER MODEL ---
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    user = Column(String, nullable=False)
    status = Column(String, default="Pending")

    # Relationship
    product = relationship("Product", backref="orders")
