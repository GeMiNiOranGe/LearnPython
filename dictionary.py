# dict comprehension
human: dict[str, object] = dict()
human = {key: value for key, value in [("id", 0), ("name", "John")]}
print(human, end="\n\n")

# initialize with iterable
# case 1
doctor_iterable: list[tuple[str, object]] = [
    ("id", 1),
    ("name", "Jessica"),
]
doctor: dict[str, object] = dict(doctor_iterable)
print(doctor)

# case 2
teacher_iterable: list[list[str]] = [["id", "2"], ["name", "Mei"]]
teacher: dict[str, str] = dict(teacher_iterable)
print(teacher, end="\n\n")

# initialize with keyword arguments
artist: dict[str, object] = dict(id=3, name="Jack")
print(artist, end="\n\n")

# initialize with fromkeys method
barber_key: tuple[str, str] = ("id", "name")
# or: barber_key: list[str] = ["id", "name"]

barber_none = dict.fromkeys(barber_key)
barber = dict.fromkeys(barber_key, "default value")

print(barber_none)
print(barber, end="\n\n")

# normal initialization
person: dict[str, object] = {
    "id": 4,
    "name": "Mike",
    "sex": "female",
    "age": 30,
    "phone_number": "9999999999",
}

print("Items -------------------")
person_items = person.items()
person_item_list: list[tuple[str, object]] = list(person_items)
print(person_items)
print(f"List     : {person_item_list}")
print(f"Person id: {person_item_list[0][1]}")

print("Keys --------------------")
person_keys = person.keys()
person_key_list: list[str] = list(person_keys)
print(person_keys)
print(f"List    : {person_key_list}")
print(f"Key para: {person_key_list[0]}")

print("Values ------------------")
person_values = person.values()
person_value_list: list[object] = list(person_values)
print(person_values)
print(f"List      : {person_value_list}")
print(f"Value para: {person_value_list[0]}")

print("-------------------------")
print(f"Old: {person}")

person["phone_number"] = "1763871268"
person["email"] = "mike130@email.com"

value = person.get("age")
if isinstance(value, int):
    age: int = int(str(value))
    age += 2
    person["age"] = age

person.update(
    sex="male",
    favourite=[
        "programing",
        "science",
        "tennis",
        "volleyball",
        "badminton",
    ],
)

print(f"New: {person}")
print(f"People's favorite: {person['favourite']}")
