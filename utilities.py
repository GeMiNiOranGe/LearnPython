def separate_each_char(message: str, delimiter: str = " ") -> str:
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    if not isinstance(delimiter, str):
        raise TypeError("Delimiter must be a string")
    chars: list = list(message)
    inside_delim: str = delimiter * 2
    result: str = delimiter + inside_delim.join(chars) + delimiter
    return result
