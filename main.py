from utilities import separate_each_char


message: str = "Hello world!!!"
separated_messages: str = separate_each_char(message, delimiter="||")
print(separated_messages)
