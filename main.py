from framework.order import Order
from framework.customer import Customer

# make an instance of Order class
baseOrder = Order()

# use createOrder method of Order class
createOrder = baseOrder.createOrder(amount=100000, capture_method="MANUAL")

# get anything you want from mapped pydantic model  according to response json
print(createOrder.order.amount) #amount = 111111


# get all orders
getOrders = baseOrder.getOrders()
# all the orders in list so you can get dict by index
print(getOrders[1].amount)


baseCustomer = Customer()

getCustomers = baseCustomer.getCustomers(limit=4, page=1)

print("getCustomers", getCustomers[0].email)

createCustomers = baseCustomer.createCustomer(email="a@gmail.com", phone="77777777")

print("createCustomers", createCustomers)







