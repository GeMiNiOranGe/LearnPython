class NotInRangeException(Exception):
    def __init__(self, variable_name: str, range_start: str, range_end: str) -> None:
        message: str = f"'{variable_name}' is not in [{range_start}, {range_end}] range"
        super().__init__(message)
