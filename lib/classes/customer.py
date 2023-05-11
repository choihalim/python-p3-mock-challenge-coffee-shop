class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._coffees = []

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        # else:
        #     raise Exception("New Order must be of type Order")
        return self._orders

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee not in self._coffees and isinstance(new_coffee, Coffee):
            self._coffees.append(new_coffee)
        # else:
        #     raise Exception("New Coffee must be of type Coffee")
        return self._coffees

    def create_order(self, coffee, price):
        from classes.order import Order
        Order(self, coffee, price)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters.")

    name = property(get_name, set_name)
