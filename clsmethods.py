class Student:
    no_of_employess=10
    def __init__(self,aname,arole):
        self.name=aname
        self.role=arole
@classmethod
def change_employess(cls, newemployee):
    cls.no_of_employess = newemployee
harry=Student("jarvihs","pgm")
harry.change_employess(20)

print(harry.no_of_employess)
