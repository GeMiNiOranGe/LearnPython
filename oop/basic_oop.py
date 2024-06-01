from person import Person
from student import Student


person: Person = Person("mike", age=30)
person_1: Person = Person("Abby", age=25)

print(Person.test)
print(person.test)

Person.test += " and object of class"

print(Person.test)
print(person.test, end="\n\n")

print(person)
person.phone_number = "0123871268"
print(person, end="\n\n")

print(person.__dict__, end="\n\n")

print(f"Person id             : {person.id}")
print(f"Person 1 id           : {person_1.id}")
print(f"Class Person static id: {Person.static_id}", end="\n\n")

print("-" * 25)
student: Student = Student("jack", age=15)
student.grade = 8
print(f"Student id: {student.id}")
print(student)
