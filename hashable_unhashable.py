width: int = 16
id_width: int = 4

""" number handling """
number: int = 1
number_id: int = id(number)

print(f"Number id: {number_id}", end="\n\n")


""" string handling (hashable object) - tuple"""
message_1: str = "Hello world"
message_2: str = "Hello John"

# current id
message_1_id: int = id(message_1)
message_2_id: int = id(message_2)

message_1 = message_1 + ", I am Mike"
message_2 += ", I am Mike"

# new id
new_message_1_id: int = id(message_1)
new_message_2_id: int = id(message_2)

print(f"String (message)", end="")
message_output: str = f"""
{'Id':{id_width}}{'Current'   :<{width}}New
{'1' :{id_width}}{message_1_id:<{width}}{new_message_1_id}
{'2' :{id_width}}{message_2_id:<{width}}{new_message_2_id}
"""
print(message_output)


""" list handling (not hashable object) - dictionary """
values_1: list[int] = [1, 2, 3]
values_2: list[int] = [4, 5, 6]

# current id
values_1_id: int = id(values_1)
values_2_id: int = id(values_2)

values_1 = values_1 + [1]
# or: values_1 = values_1.__add__([1])
values_2 += [1]
# or: values_1.__add__([1])

# new id
new_values_1_id: int = id(values_1)
new_values_2_id: int = id(values_2)

print("List (values)", end="")
values_output: str = f"""
{'Id':{id_width}}{'Current'  :<{width}}New
{'1' :{id_width}}{values_1_id:<{width}}{new_values_1_id}
{'2' :{id_width}}{values_2_id:<{width}}{new_values_2_id}
"""
print(values_output)
