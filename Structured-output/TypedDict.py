from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'John', 'age':20}

print(new_person)

#typedDict provides validation