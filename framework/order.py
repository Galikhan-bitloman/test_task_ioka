import uuid
from pydantic import  ValidationError, TypeAdapter
from typing import List

from framework.schema import CreateOrder, GetOrdersInner
from make_requests import Requesting
from common.consts import URL, HTTP_METHOD




class Order:
    def __init__(self):
        pass

    def createOrder(self, amount: float, capture_method: str):
        try:
            if isinstance(amount, (float, int)) is not True:
                return TypeError(f"Amount is not instance of float or int, it is {type(amount)}")

            if isinstance(capture_method, (str)) is not True:
                return TypeError(f"Capture method must be instance of string, it is {type(capture_method)}")

            # make request body here
            params = {"amount": amount, "capture_method": capture_method, "external_id": str(uuid.uuid4())}

            initialize_req = Requesting(base_url=URL.API_HOST.value)
            res = initialize_req.make_requests(method=HTTP_METHOD.POST.value,params=params, path=URL.CREATE_ORDER.value)

            mapping_dict = CreateOrder(**res)

            return mapping_dict

        except Exception as e:
            print("e", e)
            return e
        except ValidationError as inval:
            return inval

    def getOrders(self):
        try:
            initialize_req = Requesting(base_url=URL.API_HOST.value)
            res = initialize_req.make_requests(method=HTTP_METHOD.GET.value, path=URL.GET_ORDERS.value)

            # here need to map all list with data
            ta = TypeAdapter(List[GetOrdersInner])
            make = ta.validate_python(res)

            return make

        except Exception as e:
            print("e", e)
            return e
        except ValidationError as inval:
            return inval


