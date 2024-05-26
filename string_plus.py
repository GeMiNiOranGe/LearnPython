""" This is docs string, Pretty cool, huh ??? """

raw_string: str = r"this\is\path" + " | "
times: int = 3
print(raw_string * times)


""" formatting with string literals, called f-strings """
raw_message: str = "           python iS sO sLoW    "
message: str = raw_message.strip()

string_to_find: str = "python"
is_find: bool = string_to_find in message

index: int = 0
reverse_index: int = -1
string_length: int = len(message)

start: int = 0
stop: int = 6
step: int = 2

output: str = f"""
raw_message           : "{raw_message}"
message               : "{message}"
string_to_find        : {string_to_find}
result                : {is_find}
length                : {string_length}
first letter is       : {message[index]}
last letter is        : {message[reverse_index]}
substring             : {message[start:stop]}
substring with step   : {message[start:stop:step]}
string is reversed    : {message[::-1]}
"""
print(output)


""" formatting with % operator """
name: str = "Mike"
fruit: str = "apple"

"""
%s - String (or %r - "repr" is short for "representation")
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
"""
# TODO: declare data type for variable
data_1 = {"name": name, "fruit": fruit}
method_1: str = "method 1: i'm %(name)s, i like %(fruit)r" % data_1

data_2 = (name, fruit)
method_2: str = "method 2: i'm %s, i like %r" % data_2

print(method_1)
print(method_2)
print()


""" formatting with format() string method """
other_message_1: str = "Are you {}, hello {}, do you want to eat {}?"
other_message_2: str = "Are you {0}, hello {0}, do you want to eat {1}?"
other_message_3: str = "Are you {who}, hello {who}, do you want to eat {food}?"

print(other_message_1.format(name, name, fruit))
print(other_message_2.format(name, fruit))
print(other_message_3.format(who=name, food=fruit))


""" function for string """
string_width: int = 40
fillchar: str = "-"
new_string: str = "c++"
string_to_count: str = "s"
separator: str = "o"

count: int = message.count(string_to_count)
capitalized_message: str = message.capitalize()
uppercase: str = message.upper()
lowercase: str = message.lower()
swapped_message: str = message.swapcase()
title: str = message.title()
centered_message: str = message.center(string_width, fillchar)
aligned_left: str = message.ljust(string_width, fillchar)
aligned_right: str = message.rjust(string_width, fillchar)
replaced_message: str = message.replace(string_to_find, new_string)

# TODO: declare data type for variable
splitted_message = message.split()
partitioned_message = message.partition(separator)

result: str = f"""
Count       : {count}
Capitalize  : {capitalized_message}
Uppercase   : {uppercase}
Lowercase   : {lowercase}
Swapcase    : {swapped_message}
Title       : {title}
Center      : {centered_message}
Align left  : {aligned_left}
Align right : {aligned_right}
Replaced    : {replaced_message}
Splitted    : {splitted_message}
Partitioned : {partitioned_message}
"""
print(result)
