class Employee:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal

e1=Employee("Kiran",10000)
print(e1.salary) # 10000
e1.salary=20000
print(e1.salary) # 20000

class Protected_Employee:
    def __init__(self, name, sal):
        self._name=name  # protected attribute
        self._salary=sal # protected attribute

e1=Protected_Employee("Swati",10000)
print(e1._salary) # 10000
e1._salary=20000
print(e1._salary) # 20000



class Private_Employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute
        self.__salary=sal # private attribute

e1=Private_Employee("Bill",10000)
"""
print(e1.__salary)
Traceback (most recent call last):
  File "08.0.0_Encapsulamento.py", line 29, in <module>
    print(e1.__salary)
AttributeError: 'Private_Employee' object has no attribute '__salary'
"""
print(e1._Private_Employee__salary) # 10000
e1._Private_Employee__salary=20000
print(e1._Private_Employee__salary) # 20000
