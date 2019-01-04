class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


print(MyClass.i)

MyClass.i = 'changed'

b = MyClass()
print(MyClass.i)
print(b.i)

MyClass.counter = 2
print(MyClass.counter)