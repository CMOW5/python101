class Dog:

    kind = 'canine'         # class variable shared by all instances

    # class instantiation automatically invokes __init__() 
    # for the newly-created class instance
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance (data attribute)

    def setName(self, name):
        self.name = name


if __name__ == '__main__':

    d = Dog('Fido')
    e = Dog('Buddy')

    # shared by all dogs
    d.kind # output => 'canine' 

    # shared by all dogs
    e.kind # output => 'canine'

    # unique to d
    d.name # output => 'Fido'

    # unique to e
    e.name # output =>'Buddy'

    e.setName('hola')
    print(e.name)
    print(d.name)