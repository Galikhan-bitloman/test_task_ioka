from typing import Any, List, Optional

import pydantic
from pydantic import BaseModel


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


# class GetOrders(BaseModel):
#     __root__: List[GetOrdersInner]

a = [
    {
        "created_at": "2023-10-09T13:33:29.396357",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_ov1EUj9P7k",
        "status": "UNPAID",
        "amount": 111111,
        "currency": "KZT",
        "capture_method": "MANUAL",
        "external_id": "35ccda1d-46ec-42ba-af22-bc2e08fd13fa",
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_ov1EUj9P7k"
    },
    {
        "created_at": "2023-10-09T13:28:38.289478",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_92JyWbctxZ",
        "status": "UNPAID",
        "amount": 10000,
        "currency": "KZT",
        "capture_method": "MANUAL",
        "external_id": "d0465c01-ab96-4781-be1f-e741e13314eb",
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_92JyWbctxZ"
    },
    {
        "created_at": "2023-10-09T05:57:37.802738",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_A5tj04MOrC",
        "status": "UNPAID",
        "amount": 300000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_A5tj04MOrC"
    },
    {
        "created_at": "2023-10-09T05:39:21.941294",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_s2jhsODe8s",
        "status": "UNPAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_s2jhsODe8s"
    },
    {
        "created_at": "2023-10-09T05:36:28.556574",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_bV7VRsdGDe",
        "status": "PAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 9,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_bV7VRsdGDe"
    },
    {
        "created_at": "2023-10-09T05:33:12.454575",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_dNAz7zw7Bo",
        "status": "PAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 9,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_dNAz7zw7Bo"
    },
    {
        "created_at": "2023-10-09T05:29:52.294936",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_vSA9AYkYBw",
        "status": "UNPAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": "8G56Pu7W0z",
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_vSA9AYkYBw"
    },
    {
        "created_at": "2023-10-08T18:03:30.941065",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_1osqc3XQte",
        "status": "UNPAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_1osqc3XQte"
    },
    {
        "created_at": "2023-10-08T17:57:23.970843",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_PTrRRrR0sV",
        "status": "UNPAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_PTrRRrR0sV"
    },
    {
        "created_at": "2023-10-08T17:55:37.660578",
        "shop_id": "shp_UYNBFVLNQJ",
        "id": "ord_96pCpUlMmC",
        "status": "UNPAID",
        "amount": 50000,
        "currency": "KZT",
        "capture_method": "AUTO",
        "external_id": None,
        "description": None,
        "extra_info": None,
        "mcc": None,
        "acquirer": None,
        "customer_id": None,
        "card_id": None,
        "attempts": 10,
        "due_date": None,
        "checkout_url": "https://stage-checkout.ioka.kz/orders/ord_96pCpUlMmC"
    }
]

from pydantic import  ValidationError, TypeAdapter
# aa = RootModel[List[GetOrdersInner]]

m = TypeAdapter(List[GetOrdersInner])
t = m.validate_python(a)
print(t[0].amount)

