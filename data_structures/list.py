from copy import deepcopy


size: int = 3

""" list comprehension """
values: list[int] = [number for number in range(size)]
numbers: list[int] = list([10, 20])

values += numbers * 2
other_values: list[int] = values.copy()

""" referenced object """
print(values)
print(other_values)

values[0] = 99

print(values)
print(other_values)
print()

""" matrix """
matrix_2d: list[list[int]] = [[1, 2, 3], [4, 5, 6]]
other_matrix_2d: list[list[int]] = deepcopy(matrix_2d)

print(matrix_2d)
print(other_matrix_2d)

other_matrix_2d[0][0] = 100

print(matrix_2d)
print(other_matrix_2d)
print()

""" function for list """
chars: list[str] = [
    "I",
    " ",
    "this element",
    "will be removed",
    "a",
    "m",
    " ",
    ",",
    " ",
    "h",
    "e",
    "l",
    "l",
    "o",
    " ",
]
print(chars)

name: str = "John"
string_to_remove: str = "will be removed"
insert_index: int = 5
pop_index: int = 2

chars.pop(pop_index)
print(chars)

chars.remove(string_to_remove)
print(chars)

chars.extend(["w", "o", "r", "l", "d"])
print(chars)

chars.append("!")
print(chars)

chars.append("!")
print(chars)

chars.append("!")
print(chars)

chars.insert(insert_index, name)
print(chars)
