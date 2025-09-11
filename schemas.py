from pydantic import BaseModel
from typing import Optional

# === USER SCHEMAS ===
class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True  # Pydantic v2


# === CATEGORY SCHEMAS ===
class CategoryBase(BaseModel):
    name: str

class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# === OFFER SCHEMAS ===
class OfferBase(BaseModel):
    title: str
    discount: float

class OfferOut(OfferBase):
    id: int

    class Config:
        from_attributes = True


# === PRODUCT SCHEMAS ===
class ProductBase(BaseModel):
    title: str
    price: float
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: int
    offer_id: Optional[int] = None

class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True


# === ORDER SCHEMAS ===
class OrderBase(BaseModel):
    product_id: int
    quantity: int
    user: str
    status: str

class OrderOut(OrderBase):
    id: int

    class Config:
        from_attributes = True
