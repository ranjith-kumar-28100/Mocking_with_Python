from unittest.mock import Mock

mock = Mock(return_value=25)

print(mock)

# mock.return_value = 25
print(mock())
print(mock.return_value)

stuntman = Mock()
print(stuntman.perform_jump_from_building())
print(stuntman.escape_from_fire())

stuntman.perform_jump_from_building.return_value = (
    "Oh god, managed to do this without any injury"
)


stuntman.escape_from_fire.return_value = "Ahh, It hurts"

print(stuntman.perform_jump_from_building())
print(stuntman.escape_from_fire())
