class person:
    def __init__(self):
        self.__name = ''

    # Sogrecarga de método name separando
    # o get(name(self)) do set(name(self, value))
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self, value):
        print('Deleting..')
        del self.__name

p = person()
p.name = 'Steve'
print(p.name)

# Se não implementar o decorador @name.delter
# ocorre o erro AttributeError: can't delete attribute
del p.name

# TypeError: name() missing 1 required positional argument: 'value'
print(p.name)