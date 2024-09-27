class maktabkhooneh:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def value(self):
        return self.name + self.grade
        
person = maktabkhooneh("Ahmad","Master",24)
print(person.value())