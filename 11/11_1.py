class Person:
    def __init__(self, person_name, person_sex):
        self.person_name = person_name
        self.person_sex = person_sex

    def clothes(self, verh, niz, obuv):
        self.verh = verh
        self.niz = niz
        self.obuv = obuv

    def __str__(self):
        return self.person_name + ' ' + self.person_sex

class Student(Person):
    def __init__(self, person_name, person_sex, student_lvl):
        super.__init__(person_name, person_sex)
        self.student_lvl = student_lvl

    def __str__(self):
        return self.person_name + ' ' + self.person_sex + ' ' + self.student_lvl

class Teacher(Person):
    def __init__(self, person_name, person_sex, teacher_zarplata):
        super.__init__(person_name, person_sex)
        self.teacher_zarplata = teacher_zarplata
    def __str__(self):
        return self.person_name + ' ' + self.person_sex + ' ' + self.teacher_zarplata

Andrii = Student('Andrii','men','low')

print(Andrii)

