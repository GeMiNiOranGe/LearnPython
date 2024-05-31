class Person:
    test: str = "This attribute is called from the class name"
    static_id: int = 1

    def __init__(
        self,
        name: str = "noname",
        sex: str = "male",
        age: int = 0,
        phone_number: str = "####-###-###",
    ) -> None:
        self.id = Person.static_id
        self.name = name
        self.sex = sex
        self.age = age
        self.phone_number = phone_number
        Person.static_id += 1

    # region properties
    # Property for id
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("'Id' must be set to an int")
        self.__id = value

    @id.deleter
    def id(self) -> None:
        del self.__id

    # Property for name
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("'Name' must be set to an string")
        self.__name = value.capitalize()

    @name.deleter
    def name(self) -> None:
        del self.__name

    # Property for sex
    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("'Sex' must be set to an string")
        self.__sex = value.lower()

    @sex.deleter
    def sex(self) -> None:
        del self.__sex

    # Property for age
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("'Age' must be set to an int")
        if value < 0:
            raise ValueError("'Age' must be a positive number")
        self.__age = value

    @age.deleter
    def age(self) -> None:
        del self.__age

    # Property for phone number
    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("'Phone number' must be set to an string")
        self.__phone_number = value

    @phone_number.deleter
    def phone_number(self) -> None:
        del self.__phone_number

    # endregion

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, sex: {self.sex}, age: {self.age}, phone number: {self.phone_number}"
