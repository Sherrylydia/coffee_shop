import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("Mo")
    
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_orders_and_customers():
    coffee = Coffee("Latte")
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")

    cust1.create_order(coffee, 4.0)
    cust2.create_order(coffee, 5.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {cust1, cust2}

def test_coffee_num_orders_and_average_price():
    coffee = Coffee("Cappuccino")
    cust = Customer("Njeri")

    cust.create_order(coffee, 4.0)
    cust.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
