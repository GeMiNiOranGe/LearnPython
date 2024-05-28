width: int = 16
size: int = 10

""" set comprehension """
values: set[int] = {number for number in range(size)}
print(values, end="\n\n")

""" other functions """
repeat_value_set: set[int] = {1, 1, 5, 5, 3, 2, 4}
number: int = 5
is_include: bool = number in repeat_value_set

pop_out_number: int = repeat_value_set.pop()

print(f"Pop out number: {pop_out_number}")
print(f"{number} in {repeat_value_set}: {is_include}", end="\n\n")

# create "set" from string
message: str = "Hello world"
char_set: set[str] = set(message)
print(f"Char set (from '{message}'): {char_set}")

""" set operations """
# use []
data_set_1: set[int] = set([1, 2, 3, 4, 5])
# use {}
data_set_2: set[int] = set({3, 4, 5, 6, 7})

union_set: set[int] = data_set_1.union(data_set_2)
# or: union: set[int] = data_set_1 | data_set_2

intersection_set: set[int] = data_set_1.intersection(data_set_2)
# or: intersection: set[int] = data_set_1 & data_set_2

difference_set: set[int] = data_set_1.difference(data_set_2)
# or: difference: set[int] = data_set_1 - data_set_2

symmetric_difference_set: set[int] = data_set_1.symmetric_difference(data_set_2)
# or: symmetric_difference: set[int] = data_set_1 ^ data_set_2

set_output: str = f"""
Data set 1          : {data_set_1}
Data set 2          : {data_set_2}
---------------------
Union               : {union_set}
Intersection        : {intersection_set}
Difference          : {difference_set}
Symmetric difference: {symmetric_difference_set}
"""
print(set_output)
