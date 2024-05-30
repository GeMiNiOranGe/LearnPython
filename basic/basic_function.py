from functools import reduce
from typing import Any, Callable, Generator


def calculate_square(number_list: list[int]) -> Generator[int, Any, None]:
    for number in number_list:
        yield number**2


for element in calculate_square([1, 2, 3]):
    print(element)
print()


# ------------------------
def gen():
    for i in range(4):
        x = yield i
        print("Value sent:", x)


g = gen()
print(next(g))
print(g.send("first message"))
print(g.send("second message"))
print(g.send("third message"))
print()

# lambda------------------
length, width = 2, 9

calculate_perimeter: Callable[[int, int], int] = (
    lambda length, width: (length + width) * 2
)
print(f"Peri = {calculate_perimeter(length, width)}")

# recommended
print(f"Area = {(lambda length, width: length * width)(length, width)}", end="\n\n")

# functional tools--------
# map: case 1
size: int = 5
values: list[int] = [number for number in range(size)]

new_values: map = map(lambda number: number + 2, values)

print(new_values)
print(list(new_values))

# map: case 2
list_1: list[int] = [1, 2, 3, 4]
list_2: list[int] = [5, 6, 7, 8]

map_result: map = map(lambda x, y: x + y, list_1, list_2)

print(list(map_result), end="\n\n")

# filter
filter_list = [1, -3, 5, 0, 2, 6, -4, -9]

filtered_list: filter = filter(lambda x: x > 0, filter_list)

print(filtered_list)
print(list(filtered_list), end="\n\n")

# reduce
reduce_list: list[int] = [number for number in range(size)]
initial_value: int = 3

reduced_list: int = reduce(lambda x, y: x + y, reduce_list, initial_value)

print(reduced_list)
