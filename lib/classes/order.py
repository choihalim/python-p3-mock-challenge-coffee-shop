
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price

        self.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("Price must be an integer between 1 and 10.")

    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer must be of type Customer.")

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee

    def set_coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Coffee must be of type Coffee.")

    coffee = property(get_coffee, set_coffee)
