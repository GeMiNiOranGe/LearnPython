from custom_exception import NotInRangeException


class Person:
    test: str = "This attribute is called from the class name"
    static_id: int = 1

    def __init__(
        self,
        name: str = "noname",
        sex: str = "male",
        age: int = 0,
        phone_number: str | None = None,
    ) -> None:
        self.id = Person.static_id
        self.name = name
        self.sex = sex
        self.age = age
        self.phone_number = phone_number
        Person.static_id += 1

    # region properties
    # Property for "id"
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("'id' must be set to int")
        self._id = value

    @id.deleter
    def id(self) -> None:
        del self._id

    # Property for "name"
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("'name' must be set to string")
        self._name = value.capitalize()

    @name.deleter
    def name(self) -> None:
        del self._name

    # Property for "sex"
    @property
    def sex(self) -> str:
        return self._sex

    @sex.setter
    def sex(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("'sex' must be set to string")
        self._sex = value.lower()

    @sex.deleter
    def sex(self) -> None:
        del self._sex

    # Property for "age"
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("'age' must be set to int")
        if value < 0:
            raise NotInRangeException("age", "0", "inf")
        self._age = value

    @age.deleter
    def age(self) -> None:
        del self._age

    # Property for "phone_number"
    @property
    def phone_number(self) -> str | None:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str | None) -> None:
        if not isinstance(value, (str, type(None))):
            raise TypeError("'phone_number' must be set to string")
        self._phone_number = value

    @phone_number.deleter
    def phone_number(self) -> None:
        del self._phone_number

    # endregion

    # region method
    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, sex: {self.sex}, age: {self.age}, phone number: {self.phone_number}"

    # endregion
