from utilities import separate_each_char
import data_structures.tuple


def main() -> None:
    message: str = "Hello world!!!"
    separated_messages: str

    try:
        separated_messages = separate_each_char(message)
    except TypeError as type_error:
        print(f"separate_each_char(): {type_error}")
    else:
        print(separated_messages)
    finally:
        print("Program end")


if __name__ == "__main__":
    main()
