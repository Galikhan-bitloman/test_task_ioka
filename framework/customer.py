from pydantic import TypeAdapter, ValidationError
from typing import List
from enum import Enum
import uuid

from framework.schema import GetCustomers, CreateCustomers
from common.make_requests import Requesting
from common.consts import URL, HTTP_METHOD
from common.utils import make_dict



class Customer:
    def __init__(self):
        pass

    def getCustomers(self, to_dt: str = None, from_dt: str = None, date_category: str = None, status: Enum = None,
                     limit: int = 10, page: int = 1):

        try:
            if isinstance(limit, int) is not True or limit < 1 or limit > 10:
                return TypeError(
                    "entered value is wrong in limit (check data type of limit (must be int) or must be between 1 and 10)")
            if isinstance(page, int) is not True or page < 1:
                return TypeError(
                    "entered value is wrong in page (check data type of page (must be int) or can't be below zero")

            params = make_dict(to_dt=to_dt, from_dt=from_dt, date_category=date_category, status=status, limit=limit, page=page)
            print("params", params)

            r = Requesting(base_url=URL.API_HOST.value)

            res = r.make_requests(method=HTTP_METHOD.GET.value, path=URL.GET_CUSTOMERS.value, params=params)

            ta = TypeAdapter(List[GetCustomers])
            m = ta.validate_python(res)
            print("m", m)
            return m

        except Exception as e:
            print("cust get", e)
            return e

    def createCustomer(self, email: str, phone: str):
        try:
            params = {"email": email, "phone": phone, "external_id": str(uuid.uuid4())}

            r = Requesting(base_url=URL.API_HOST.value)

            res = r.make_requests(method=HTTP_METHOD.POST.value, path=URL.CREATE_CUSTOMERS.value, params=params)

            mapping = CreateCustomers(**res)

            return mapping

        except Exception as e:
            print("e", e)
            return e
        except ValidationError as inval:
            return inval

