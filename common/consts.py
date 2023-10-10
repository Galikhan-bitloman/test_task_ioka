from enum import Enum
import os

class URL(Enum):
    API_HOST = os.getenv('API_HOST')
    CREATE_ORDER = os.getenv('CREATE_ORDER')
    GET_ORDERS = os.getenv('GET_ORDERS')


class HTTP_METHOD(Enum):
    GET = "GET"
    POST = "POST"


class HEADERS(Enum):
    API_KEY = os.getenv('API_KEY')


