#!/usr/bin/env python3

# Object Oriented Programming, abbreviate to OOP.
# Object Oriented Programming is a programming idea.
# OOP simple principle
# 	object as a conponent of programm,
# 	the execution of program be finished by call interface priovded by object.
#       

# OOP have four core concepts.
# 	abstract, encapsulation, inheritance, polymorphism
#
# unexpanded description here. expanded back.

# start with process-oriented.

# the phrase that
# a dog named 'wangcai', make sound 'wang wang wang'
# a cat named 'kitty', make sound 'miu miu miu'

# convert to program language.
# show the pseudo code:
# main() {
#	dog_name = 'wangcai';
# 	dog_sound = 'wang wang wang...';
# 	cat_name = 'kitty';
# 	cat_sound = 'miu miu miu...';
#	print(dog_name + 'is making sound ' + dog_sound);
#	print(cat_name + 'is making sound ' + cat_sound);
# }	
# 
# the execution result:
# wangcai is making sound wang wang wang..
# kitty is making sound miu miu miu...
#
# the above content is process-orented code style.

# ok, finish it by object-oriented programming.
# 
# first sep, abstract
# abstaction is the process of extracting the common features and behaviors 
# from particular instance to form abstract type.
#
# abstract, the process that get abstract description from instance concrete information.
#
# the dog named 'wangcai' can making sound, it's a particular instance, 
# abstract type from particular instance. 
# remeber! different abstract scope will make sure different abstract type.
# usually, the abstract scope just meet enough. it's a ability what need experience.
# it's kind of dog, so 'dog' can be abstract type. 
# it named 'wangcai', so the name can be featrue.
# it making sound, so making sound can be behavior.
#
# abstract result: 
# abstract type, 'dog'  
# feature, the name 'wangcai'
# behavior, making sound 'wang wang wang...'
# 
# convert program code by abstract result.
# show pseudo code:
# dog {		# abstract 
# 	name	# feature
# 	sound()	# behavior
# }
#
# the cat named 'kitty' making sound , also abstract it.
# cat {		# abstract	
# 	name	# feature  
# 	sound() # behavior
# }
#
# usually, in program language
# abstract type, called object name.
# feature, called object attribute.
# behavior, called object method.

# OOP have two basic concepts, Class and Instance
# Class is the template of instance, and
# Instance is concrete object by class created.
# 
# many instances abstract to one class.
# one class can create many concrete object.
# PS:
# in program language 
# instance and object, most of time they are the same concept.

# create a simple class, named 'Test'.
# PS: class name need captialize the first letter.
class Test:
	# note that, 
	# in python2, create class need inherit to parent class 'object'.
	# python3, not required, like this.
	pass
t = Test() # create instance by class.
print(t)
# execution result:
# $python3 test.py
# <__main__.Test instance at a33f0f8f2f> # the default format to print instance.
# 
# the purpose of printing an instance is to know where it is in the machine.
# the instance address of memery aftr 'at', not good for human read.

# the spesual method '__init__' can set the instance initiliztion.
class Test:
	# 'self' is required parameter that __init__ method default syntax.
	# 'name' is also a required parameter,
	# mean that require a parameter when class create instance.
	def __init__(self, name): 
		self.name = name
	def __repr__(self):
		return 'Test: {}'.format(self.name)

t = Test('python') # create instance 
print(t)	# print instance
print(t.name)	# print attribute 'name'
# custom format print instance by __repr__ method,
# it's will good for human read when printing instance.
class Test:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Test: {}'.format(self.name)

t = Test('python')
print(t)
print(t.name)
# execution result 
# $python3 test.py 
# Test: python # customize the print effect
# python

# encapsulation
# encapsulation is the use of class to encapsulation data and data-based operations,
# hide internal data, and priovde common access interface.

# show python code
class Dog(object):
	def __init__(self, name):
# 1-unlike Java or C++, Pythone don't have specilic keyword to declare private attrbute.
# 2-private attribute of python begins with one or two underscores to indicate.
# 3-one underscore indicates that external caller shuld not call this property directly. but you can still call it.
# 4-two underscores indicate that can't call directly outside. 
	def get_name(self):
		return self._name
	def set_name(self, value):
		self._name = value
	def bark(self):
		print(self.get_name() + ' is making sound wang wang wang...')

class Cat(object):
	def __init__(self, name):
		self._name = name
	def get_name(self):
		return self._name
	def set_name(self, value):
		self._name = value
	def mew(self):
		print(self.get_name() + ' is making sound miu miu miu...')
# instancetion a object 
dog = Dog('wangcai')
cat = Cat('kitty')
dog.bark()
cat.mew()
# the benifit of encapsulation is priovde access control.

# inherit 
# sometimes many low abstraction classes can abstract to become a high abstraction class.
# high abstraction class called parent class.
# low abstraction class called sub class.
# inherit and rewirte method.
class Animal(object):
	def __init__(self, name):
		self._name = name
	def get_name(self):
		return self._name
	def set_name(self, value):
		self._name = value
	def make_sound(self):
		pass

class Dog(Animal):
	def make_sound(self):
		print(self.get_name() + ' is making sound wang wang wang...')

class Cat(Animal):
	def make_sound(self):
		print(self.get_name() + ' is making sound miu miu miu...')
 
# polymorphism
# polymorphism simple explanation that use same method for different objects 
# will have different result.
#
# show pseudo code:
# Dog dog1 = new Cat('wangcai')
# Cat cat1 = new Cat('kitty')
# Dog dog2 = new Dog('laifu')
# Dog cat2 = new Cat('Betty')
# dog1.make_sound();
# cat1.make_sound();
# dog2.make_sound():
# cat2.make-sound();
#
# show pseudo code:
# Set animals = [new Dog('wangcai'), new Cat('kitty'), new Dog('laifu'), new Cat('Betty')];
# Animal animal;
# for (i = 0; i <= animals.lent(); i++)
# {
# 	# parent class reference point to sub object
# 	animal = animals[i];
# 	# polymorphism
# 	animal.make_sound();
# }
#
# python code:
animals = [Dog('wangcai'), Cat('kitty'), Dog('laifu'), Cat('betty')]
for animal in animals:
	animal.make_sound()

# private property and method
# in Java and C++ porgram language, can use 'private' and 'protected' keyword
# to decorated property and method, they will control whether external and subclass access,
# in python, the convention is to add two undersocrs before name of property and method to
# deny external access.
class Oop:
	__private_name = 'oop_test'
	def __get_private_name(self):
		return self.__private_name
	
o = Oop()
# will report AttributeError, because property and method all seted to be private.
# o.__private_name
# o.__get_private_name()

# why the convention, because python don't have absolute private, even if use two 
# underscors to constraint, it also can be accessed through 
# obj._Classname__privateAttributeOrMethod,
# but not recommemded.
o._Oop__private_name
o._Oop__get_private_name()
# so '__' the double underscors just constraint, to tell external caller don't use this property and method directly.
# '__' double underscors is standard style to set private property and method, 
# '_' one underscor can be a convention what peproe established by usage, 
# although can access directly it.

# static variable and class method
# 
# static variable and class method can access directly without instantiation object.
# show python code.
class Animal(object):
	owner = 'jack'
	def __init__(self.name):
		self._name = name

print(Animal.owner) # 'jack'
print(Cat.owner) # 'jack'
#
# class method work like private variable, access without instantiation.
# class method use '@classmethod' to decorate.
# class method can access class static variable
# add a class method 'get_owner' below:
class Animal(object):
	owner = 'jack'
	def __init__(self, name):
		self._name = name
	@classmethod
	def get_owner(cls):
		return cls.owner
# note that, class method first parameter is a class object,
# not a instance object, so mark 'cls' here.
# use class method get owner:
print(Animal.get_owner()) # 'jack'
print(Cat.get_owner()) # 'jack'

# 'property' decorator
# in python, 'propery' decorator can make method used like property,
# 'property' decorator realize getter/setter of python style,
# so, we can through the decorator get and set object foo property.
# rewrite class Animal by 'property'
class Animal:
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, value):
		# judgement datatype of passed parameter
		if isinstance(value, int):
		# if datatype is int assignment.
			self._age = value
		else:
		# not, report error
			raise VauleError

cat = Animal() # create instance
# assign a character, will report error.
# cat.age = 'h'
cat.age = 3
print(cat.age)
# in this way, we can get and set 'age' property as access property.
# the example, convert a method to a property, and add a 'setter' method
# to support for set 'age'.
# use 'property' and 'setter', effective to realize the two operations.
# get_age ( get object name), and
# set_age ( set object name) 
# no need to expose directly internal property '_age',
# and check the paramter what set in 'setter' method,
# avoid the potential risk what assign directly internal property of '_age',

# static method
# static method decorate by '@staticmethod', like 'classmetod'.
# 'staticmethod' called without instance participate, 
# 'staticmethod' will put in the class, 
# but no need pass a 'cls' parametr as class method.
#
# static method application scenarios
# when the method can realize alone without class, use static method,
# when the method a little related class, use class method.
# e.g. 
# a method of Animal, master jack can call it to buy food of animal.
class Animal(object):
	owner = 'jack'
	def __init__(self, name):
		self._name = name

	@staticmethod
	def order_animal_food():
		print('ording...')
		print('ok')
# call static method without instantiation.
Animal.order_animal_food()

