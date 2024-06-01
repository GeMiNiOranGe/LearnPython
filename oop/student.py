from custom_exception import NotInRangeException
from person import Person


class Student(Person):
    def __init__(
        self,
        name: str = "noname",
        sex: str = "male",
        age: int = 0,
        phone_number: str | None = None,
        grade: int | None = None,
    ) -> None:
        super().__init__(name, sex, age, phone_number)
        self.grade = grade

    # region properties
    # Property for "grade"
    @property
    def grade(self) -> int | None:
        return self.__grade

    @grade.setter
    def grade(self, value: int | None) -> None:
        if not isinstance(value, int | None):
            raise TypeError("'grade' must be set to 'int | None'")
        if value is not None and (int(value) < 1 or 12 < int(value)):
            raise NotInRangeException("grade", "1", "12")
        self.__grade = value

    @grade.deleter
    def grade(self) -> None:
        del self.__grade

    # endregion

    # region method
    def __str__(self) -> str:
        return f"{super().__str__()}, grade: {self.grade}"

    # endregion
