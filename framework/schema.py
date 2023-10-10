from typing import Any, List, Optional
from pydantic import BaseModel, TypeAdapter


class Order(BaseModel):
    id: str
    shop_id: str
    status: str
    created_at: str
    amount: int
    display_amount: int
    currency: str
    mcc: Any
    acquirer: Any
    capture_method: str
    external_id: str
    description: Any
    extra_info: Any
    attempts: int
    due_date: Any
    split: Any
    customer_id: Any
    card_id: Any
    back_url: Any
    success_url: Any
    failure_url: Any
    template: Any
    access_token: str
    checkout_url: str
    payment_link_url: Any
    payments: List


class CreateOrder(BaseModel):
    order: Optional[Order] = None
    order_access_token: Optional[str] = None


class GetOrdersInner(BaseModel):
    created_at: str
    shop_id: str
    id: str
    status: str
    amount: int
    currency: str
    capture_method: str
    external_id: Any
    description: Any
    extra_info: Any
    mcc: Any
    acquirer: Any
    customer_id: Any
    card_id: Any
    attempts: int
    due_date: Any
    checkout_url: str



class Resource(BaseModel):
    id: Optional[str]
    is_default: Optional[bool]
    created_at: Optional[str]
    status: Optional[str]


class Account(BaseModel):
    id: Optional[str]
    shop_id: Optional[str]
    status: Optional[str]
    amount: Optional[int]
    created_at: Optional[str]
    resources: List[Resource]


class GetCustomers(BaseModel):
    id: Optional[str]
    status: Optional[str]
    created_at: Optional[str]
    external_id: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    accounts: Optional[List[Account]]
    access_token: Optional[str]
    checkout_url: Optional[str]


class Resource(BaseModel):
    id: str
    is_default: bool
    created_at: str
    status: str


class Account(BaseModel):
    id: str
    shop_id: str
    status: str
    amount: int
    created_at: str
    resources: List[Resource]


class Customer(BaseModel):
    id: str
    status: str
    created_at: str
    external_id: str
    email: str
    phone: str
    accounts: List[Account]
    access_token: str
    checkout_url: str


class CreateCustomers(BaseModel):
    customer: Optional[Customer] = None
    customer_access_token: Optional[str] = None