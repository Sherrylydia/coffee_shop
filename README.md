# Coffee Shop Domain Model

This project models a Coffee Shop using Object-Oriented Programming principles in Python.

# Project structure
coffee_shop/
│
├── customer.py # Customer class
├── coffee.py # Coffee class
├── order.py # Order class
├── debug.py # (Optional) Script for manual testing
├── tests/ # Unit tests
│ ├── test_customer.py
│ ├── test_coffee.py
│ └── test_order.py
├── README.md # Project instructions and details


## Features

- Customers can place many orders.
- Coffees can be ordered by many customers.
- Orders connect Customers and Coffees with a price.

## Classes

- `Customer`: name, orders, coffees, most_aficionado
- `Coffee`: name, orders, customers, average_price
- `Order`: customer, coffee, price

## Setup

```bash
pipenv install
pipenv shell
