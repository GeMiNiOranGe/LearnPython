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
print(f"Area = {(lambda length, width: length * width)(length, width)}")
