"""
This is docs string
Pretty cool, huh ???
"""

raw_string: str = r"this\is\path" + "\n"
print(raw_string * 3)


""" This is another docs string """
other_message: str = "Python is so slow"

string_to_find: str = "Python"
is_find: bool = string_to_find in other_message

index: int = 0
reverse_index: int = -1
string_length: int = len(other_message)

start: int = 0
stop: int = 6
step: int = 2

output: str = f"""
result                : {is_find}
length                : {string_length}
first letter is       : {other_message[index]}
last letter is        : {other_message[reverse_index]}
substring             : {other_message[start:stop]}
substring with step   : {other_message[start:stop:step]}
string is reversed    : {other_message[::-1]}
"""
print(output)
