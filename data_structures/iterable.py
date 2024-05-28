from typing import Generator


# generator expression
iterable: Generator[int, None, None] = (number for number in range(5))
sum_iterable: Generator[int, None, None] = (number for number in range(5))
max_iterable: Generator[int, None, None] = (number for number in range(5))
min_iterable: Generator[int, None, None] = (number for number in range(5))
sort_list: list[int] = [5, 2, 8, 7, 3]

init_value: int = 3
default_output: object = "not found"

# cannot get value in tuple
print(iterable)
# access each element
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
# iterable: out of range
print(next(iterable, "unknown"), end="\n\n")

sum: int = sum(sum_iterable, init_value)
max: object = max(max_iterable, default=default_output)
min: object = min(min_iterable, default=default_output)
sorted_list: list[int] = sorted(sort_list)
reverse_sorted_list: list[int] = sorted(sort_list,reverse=True)

print(f"Start value  : {init_value}")
print(f"Sum          : {sum}")
print(f"Max          : {max}")
print(f"Min          : {min}")
print(f"Soted        : {sorted_list}")
print(f"Reverse soted: {reverse_sorted_list}", end="\n\n")
