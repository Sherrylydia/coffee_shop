# customer.py
from order import Order  # Import here to avoid circular import issues later


class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        # Return unique coffee instances from this customer's orders
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        spending = {}
        for order in coffee.orders():
            cust = order.customer
            spending[cust] = spending.get(cust, 0) + order.price
        max_spender = max(spending, key=spending.get)
        return max_spender

    def __repr__(self):
        return f"<Customer: {self.name}>"
