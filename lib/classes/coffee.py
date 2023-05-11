class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._customers = []

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders

    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer not in self._customers and isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return self._customers

    def num_orders(self):
        num = 0
        for _ in self._orders:
            num += 1
        return num

    def average_price(self):
        total = 0
        for order in self._orders:
            total += order.price
        return total / len(self._orders)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if hasattr(self, "name"):
            raise Exception("Cannot change the name of the coffee")

    name = property(get_name, set_name)
