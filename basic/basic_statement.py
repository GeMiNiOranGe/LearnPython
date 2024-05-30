import calendar
from typing import Iterator


message: str = "Hello world"
size: int = 5

# "is" operator
iterable: Iterator[int] = iter(range(size))
it = iterable
print(it is iterable, end="\n\n")

# syntaxnic sugar
number: int = 3
if 0 < number < 5:
    print(message)

if number in (2, 3, 4):
    print(message, end="\n\n")

# if statement
number_of_days: int
month: int = 2
year: int = 2024

if month == 2:
    number_of_days = 29 if calendar.isleap(year) else 28
elif month in (4, 6, 9, 11):
    number_of_days = 30
else:
    number_of_days = 31

print(f"Number of days in {calendar.month_name[month]} {year}: {number_of_days}")
print(calendar.month(year, month))

# match case statement
input: str = "Error"
status: str = input.lower()
match status:
    case "success":
        print("Status is success")
    case "failure" | "error":
        print("Status is failure or error")
    case _:
        print("Unknown status")
print()

# loop statement
message_length: int = len(message)
index: int = 0

while index < message_length:
    print(f"Char at {index}: {message[index]}")
    index += 1
else:
    print("Index isn't less than the message length", end="\n\n")

# ------------------------
number_it: Iterator[int] = iter(range(size))
while True:
    try:
        print(next(number_it), end=" ")
    except StopIteration:
        break
print(end="\n\n")

# ------------------------
number_list: list[int] = [number for number in range(size)]
for number in number_list:
    print("->", number, end=" ")
print(end="\n\n")

# ------------------------
person: dict[str, object] = {
    "id": 4,
    "name": "Mike",
    "age": 30,
    "phone_number": "9999999999",
}

for key, value in person.items():
    print(f"{key} => {value}")
else:
    print("Out of range: Dict person")
print()

# ------------------------
print(list(range(2, 5)))
# (start, stop -= step, step)
print(list(range(4, 1, -1)))
print(list(range(2, -3, -1)))

ls_int: list[int] = [5, 1, 2, 3, 4]
print(f"List old: {ls_int}")
for i in range(len(ls_int)):
    ls_int[i] += 1
print(f"List new: {ls_int}", end="\n\n")

# ------------------------
student_list: list[str] = [
    "Jessica",
    "Michael",
    "Irene",
    "Zelda",
    "John",
    "Abby",
    "Bob",
    "Tom",
]
student_list_with_index: enumerate[str] = enumerate(student_list)

uppercase_student_list: list[str] = [
    value.upper() for value in student_list if len(value) > 4
]
odd_numbers: dict[int, str] = {
    key: "Hello " + value if key % 2 != 0 else "I'm " + value
    for key, value in [
        (1, "Jessica"),
        (2, "Mike"),
        (3, "John"),
        (4, "Abby"),
        (5, "Ashley"),
    ]
}

print(student_list_with_index)
print(list(student_list_with_index))

for i, student in enumerate(student_list, start=1):
    print(i, "->", student)

print(uppercase_student_list)
print(odd_numbers)
