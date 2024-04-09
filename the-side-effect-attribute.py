from unittest.mock import Mock
from random import randint
import traceback


def generate_number():
    return randint(1, 11)


mock = Mock()

print(mock.side_effect)


mock.side_effect = generate_number

print(mock())


mock = Mock(return_value=100, side_effect=generate_number)

# side_effect has more preference than return_value
print(mock())


three_item_pop = Mock()
three_item_pop.pop.side_effect = [3, 2, 1, IndexError("Pop from Empty List")]
print(three_item_pop.pop())
print(three_item_pop.pop())
print(three_item_pop.pop())
try:
    print(three_item_pop.pop())
except Exception:
    traceback.print_exc()


three_item_pop.pop.side_effect = None
print(three_item_pop.pop())
