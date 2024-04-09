from unittest.mock import Mock, MagicMock

mock = Mock()

magic_mock = MagicMock()

print(mock)
print(magic_mock)

# print(len(mock))
print(len(magic_mock))

# print(mock[2])
print(magic_mock[2])

magic_mock.__len__.return_value = 10
print(len(magic_mock))

if magic_mock:
    print("Hello")

magic_mock.__bool__.return_value = False

if magic_mock:
    print("Hello")

magic_mock.__getitem__.return_value = -1

print(magic_mock[0])
print(magic_mock[1])


magic_mock.__getitem__.side_effect = lambda x: (
    [
        10,
        20,
        30,
    ][x]
    if x in [-1, -2, -3, 0, 1, 2]
    else None
)
print(magic_mock[0])
print(magic_mock[1])
print(magic_mock[2])
print(magic_mock[-1])
print(magic_mock[-2])
print(magic_mock[-3])
print(magic_mock[4])
