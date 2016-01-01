##Function and Method
###functions
    map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    reduce(max, [1, 3, 5, 9, 7])
    filter(lambda x: x and x.strip(), ['A', '', 'B', None, 'C', '  '])
    sorted([36, 5, 12, 9, 21], reverce = True)
###compair
    [x * x for x in [1, 2, 3, 4]]
    better than:
    map(lambda x: x * x, [1, 2, 3, 4])

### decorator
    def decorator(func):
        def wrapper():
            before_func()
            func()
            after_func()
            return
        return wrapper

    @decorator
    def foo():
        pass
###functools
    import functools
    int2 = functools.partial(int, base = 2)
###future
    from __future__ import division, unicode_literals
##Object Oriented Programming
###class
    class Student(object):

        def __init__(self, name, score):
            self.name = name
            self.score = score

        def print_score(self):
            print '%s,%s' % (self.name, self.score)

    lisa = Student('Lisa', 60)
    bart = Student('bart', 100)
    print '%s,%s' % (lisa.name, lisa.score)
    bart.print_score()
###private and encapsulation
    class Student(object):

        def __init__(self, name, score):
            self.__name = name
            self.__score = score

        def print_score(self):
            print '%s: %s' % (self.__name, self.__score)

        def get_name(self):
        return self.__name

        def get_score(self):
            return self.__score

        def set_score(self, score):
            if 0 <= score <= 100:
                self.__score = score
            else:
                raise ValueError('bad score')

    nick = Student('Nick', 90)
    nick.print_score()

    print nick.get_score()
    print nick.get_name()

    nick.set_score(80)
    nick.print_score()
    
    print nick._Student__name
    print fox('fox',70)._Student__name

    print nick.__score  # will not work
    nick.__score = 'nick'  # will not work
##inheritance and polymorphism
>*  The subclass inherits the methods and interface from the abstract class, and it provides details for the abstract method by overriding it.
>*  date type is class

    class Animal(object):

        def run(self):
            print 'Animal is running...'


    class Dog(Animal):

        def run(self):
            print 'Dog is running...'

        def eat(self):
            print 'Dog is eating...'


    class Cat(Animal):

        def run(self):
            print 'Cat is running...'

    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    dog.eat()

    print isinstance(dog, Dog)
    print isinstance(cat, Animal)
    print isinstance(Animal, Dog)


    def run_twice(animal):
        animal.run()
        animal.run()

    run_twice(Dog())
    run_twice(Cat())
    run_twice(Animal())
###get object information
    import types

    print type('abc') == type('123')
    print isinstance(123,int)
    print type(type(None)) == types.TypeType
    print dir(u'abc') == dir(unicode)
###from function to object
    print len('abc')
    print 'abc'.__len__
###attribute
    class MyObject(object):

        def __init__(self):
            self.x = 3

        def power(self):
            return self.x * self.y

    obj = MyObject()
    print hasattr(obj, 'x')
    print hasattr(obj, 'y')
    print hasattr(obj, 'power')

    setattr(obj, 'y', 4)
    print hasattr(obj, "y")

    print obj.y
    print getattr(obj, 'y')
    print getattr(obj, 'z', '404 not find')

    print getattr(obj, 'power')()  # ugly
    print obj.power()  # better