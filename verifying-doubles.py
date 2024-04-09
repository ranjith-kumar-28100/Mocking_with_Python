from unittest.mock import MagicMock


class BurritoBowl:
    restaurant_name = "Codeman Food Spot"

    @classmethod
    def steak_special(cls):
        return cls("Chicken", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guacamole_portions(self):
        self.guacamole_portions += 1


steak_special = BurritoBowl.steak_special()
print(steak_special.protein)
steak_special.add_guacamole_portions()
print(steak_special.guacamole_portions)

mock = MagicMock(spec=BurritoBowl)
print(mock.restaurant_name)
mock.add_guacamole_portions()
# print(mock.protein) # Raises Error
# mock.change_protein() # Raises Error

mock = MagicMock(spec=BurritoBowl.steak_special())
print(mock.protein)
print(mock.restaurant_name)
mock.add_guacamole_portions()
print(mock.guacamole_portions)
# mock.change_protein() # Raises Error
mock.sauce = "Tomato"
print(mock.sauce)

mock = MagicMock(spec_set=BurritoBowl.steak_special())
print(mock.protein)
print(mock.restaurant_name)
mock.add_guacamole_portions()
print(mock.guacamole_portions)
# mock.change_protein() # Raises Error
# mock.sauce = "Tomato" # Raises Error as spec_set is strict version of spec
# print(mock.sauce)
