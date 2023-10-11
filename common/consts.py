from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()

class URL(Enum):
    API_HOST = os.getenv('API_HOST')
    CREATE_ORDER = os.getenv('CREATE_ORDER')
    GET_ORDERS = os.getenv('GET_ORDERS')
    GET_CUSTOMERS = os.getenv('GET_CUSTOMERS')
    CREATE_CUSTOMERS = os.getenv('CREATE_CUSTOMERS')



class HTTP_METHOD(Enum):
    GET = "GET"
    POST = "POST"


class HEADERS(Enum):
    API_KEY = os.getenv('API_KEY')


class Status(Enum):
    PENDING = "PENDING"
    READY = "READY"

class DateCategory(Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    YEARLY = "YEARLY"
    MANUAL = "MANUAL"

