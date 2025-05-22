import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(TypeError):
        Customer(123)

    cust = Customer("Lydia")
    assert cust.name == "Lydia"

def test_create_order_adds_to_orders():
    cust = Customer("Lydia")
    coffee = Coffee("Latte")
    cust.create_order(coffee, 4.5)

    assert len(cust.orders()) == 1
    assert cust.orders()[0].coffee == coffee
