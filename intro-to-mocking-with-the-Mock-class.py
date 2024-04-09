from unittest.mock import Mock


pizza = Mock()
print(pizza)
print(type(pizza))

# pizza.size = "Large"
# pizza.cost = 56.23
# pizza.toppings = ["Pepperoni", "Sausage"]

pizza.configure_mock(size="Large", cost=56.23, toppings=["Pepperoni", "Sausage"])


print(pizza.size)
print(pizza.cost)
print(pizza.toppings)

print(pizza.maker)
print(pizza.maker)


print(pizza.is_veg())
print(pizza.is_veg())
