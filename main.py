from utilities import separate_each_char


message: str = "Hello world!!!"
separated_messages: str

try:
    separated_messages = separate_each_char(message, delimiter="||")
except TypeError as type_error:
    print(f"(function){separate_each_char.__name__}: {type_error}")
else:
    print(separated_messages)
finally:
    print("Program end")