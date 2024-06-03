from enum import Enum, StrEnum, auto


class Size(StrEnum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"


# auto function will start from "1" if we don't overload function "_generate_next_value_"
class AutoEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return f"{count + 1}, [{name}]"

    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()
    FIFTH = auto()


class LoginStatus(Enum):
    SUCCESS = 0
    INVALID_INPUT = 1
    INVALID_ACCOUNT = 2
    LOCKED_ACCOUNT = 3
    OTHER_ERROR = 4


def main() -> None:
    width: int = 16

    for size_element in Size:
        print(f"{size_element}")
    print()

    for element in AutoEnum:
        print(f"{element:{width}} = {element.value}")
    print()

    print(f"{'Name:':{width}} {'Member:'}")
    for name, member in LoginStatus.__members__.items():
        print(f"{name:{width}} {member}")
    print()

    print(LoginStatus(1))
    print(LoginStatus["INVALID_INPUT"])
    print(LoginStatus.INVALID_INPUT)
    print(LoginStatus.INVALID_INPUT.name)
    print(LoginStatus.INVALID_INPUT.value)
    print()

    login_status: LoginStatus = LoginStatus.SUCCESS
    status: str | None = None

    match login_status:
        case LoginStatus.SUCCESS:
            status = "Success"
        case LoginStatus.INVALID_INPUT:
            status = "Invalid input"
        case LoginStatus.INVALID_ACCOUNT:
            status = "Invalid account"
        case LoginStatus.LOCKED_ACCOUNT:
            status = "Locked account"
        case _:
            status = "Other error"
    print("Status is %r" % status)


if __name__ == "__main__":
    main()
