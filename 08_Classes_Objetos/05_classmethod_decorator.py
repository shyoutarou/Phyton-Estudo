class person:
    totalObjects = 0

    def __init__(self):
        person.totalObjects = person.totalObjects + 1

    @classmethod
    def showcount(cls):
        print("Total objects: ", cls.totalObjects)

p1 = person()
p2 = person()
person.showcount() # Total objects:  2
p1.showcount ()    # Total objects:  2
