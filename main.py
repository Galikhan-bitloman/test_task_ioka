
from framework.order import Order
# make an instance of Order class
base = Order()
# use createOrder method of Order class
create = base.createOrder(amount=100000, capture_method="MANUAL")

# get anything you want from mapped pydantic model  according to response json
print(create.order.amount)


# get all orders
get = base.getOrders()
# all orders in list so you can get dict by index
print(get[1].amount)



