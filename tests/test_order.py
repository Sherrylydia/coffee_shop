import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization_and_validation():
    cust = Customer("Njeri")
    coffee = Coffee("Americano")

    with pytest.raises(TypeError):
        Order("not a customer", coffee, 3.0)

    with pytest.raises(TypeError):
        Order(cust, "not a coffee", 3.0)

    with pytest.raises(TypeError):
        Order(cust, coffee, "3.0")

    with pytest.raises(ValueError):
        Order(cust, coffee, 0.5)

    with pytest.raises(ValueError):
        Order(cust, coffee, 11.0)

    order = Order(cust, coffee, 3.5)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 3.5
