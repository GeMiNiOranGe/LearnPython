from utilities import separate_each_char
import data_structures.tuple


def main() -> None:
    message: str = "Hello world!!!"
    separate_message: str

    try:
        separate_message = separate_each_char(message)
    except TypeError as type_error:
        print(f"separate_each_char(): {type_error}")
    else:
        print(separate_message)
    finally:
        print("Program end")


if __name__ == "__main__":
    main()
