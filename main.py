# is_old = False
# is_licenced = True
# if is_old:
#   print('you are old enough to drive')
# elif is_licenced:
#   print('You can drive now')
# else:
#   print('you are not old enough to drive!')

# if is_old and is_licenced:
#   print('You are ready to drive')
# else:
#     print('you are not old enough to drive!')

# is_friend = False
# is_user = True
# can_message = "message allowed" if  is_friend else 'message not allowed'
# print(can_message)
# # 30:00
# # short circuting
# if is_friend or is_user:
#   print('best friends forever!')
# if is_friend and is_user:
#   print('best friends forever!')
# a = [1,2,3]
# b = [1,2,3]

# print(a is b)
# print(a == b)

# for item in 'Zero to mastery':
#   print(item + '%')

# for item in (1,2,3,4):
#   for x in ['a','b','c','d']:
#     print(item, x)

# user = {
#   'name': 'Golem',
#   'age': 5006,
#   'can_swim': False
# }
# for key in user:
#   print(key)
# for value in user:
#   print(value)
# for key, value in user.items():
#   print(key, value)

# for i,char in enumerate('helloooooo'):
#   print(i,char)
# for item in range(0,10):
#   print(item)

# for i,char in enumerate(list(range(100))):
#   if char == 50:
#     print(i, char)

# i = 0
# while i < 50:
#   print(i)
#   # break
#   i += 1
# else:
#   print('done with all the work')
#   # 1:33

# while True:
#   response = input('Hello, say something: ')
#   if (response == 'bye'):
#     break

# my_list = [1, 2, 3]
# for item in my_list:
#   # thinking about it
#   pass
# i = 0
# while i < len(my_list):
#   i += 1
#   continue
#   print(i)
#   print(my_list[i])

# for item in (1,2,3,4):
#   for x in ['a','b','c','d']:
#     print(item, x)

# name = 'John'
# emoji = ':)'

# default, positional and keyword arguments
# def say_hello(name='darth vader', emoji=':<'):
#   print(f'Hello {name} {emoji}')

# say_hello('John', ':)')
# say_hello(':)', 'John')
# say_hello(emoji=':)', name='John')
# say_hello()

# def sum(num1, num2):
#   return num1 + num2

# total = sum(10,5)
# print(sum(4,total))

# def sum(num1, num2):
#   def another_function(num1, num2):
#     return num1 + num2
#   return another_function(num1, num2)
#   print('hellooo!')

# total = sum(10,20)
# print(total)

# def printer(a):
#   '''
#   this function prints parameter a
#   '''
#   print(a)

# printer('hello!!')
# help(printer)
# print(printer.__doc__)

# def is_even(num):
#   return num % 2 == 0

# print(is_even(50))

# args and kwargs
# def super_func(*args, **kwargs):
#   print(kwargs)
#   return sum(args) + sum(kwargs.values())

# print(super_func(1,2,3,4,5, num1=5, num2=10))

# a = 'heloooooooooo'

# if (len(a)) > 10:
#   print(f'too long {len(a)} letters sentence!')
# # walrus operator - assing values to variables as longer sentences
# if ((n := len(a)) > 10):
#   print(f'too long {n} letters sentence!')

# b = 1

# def scope_example():
#   b = 10
#   return b

# print(b)
# print(scope_example)

# total = 0

# def count(total):
#   total += 1
#   return total

# print(count(count(count(total))))

# def outer():
#   x = 'local'
#   def inner():
#     nonlocal x
#     x = 'nonlocal'
#     print("inner: ", x)
#   inner()
#   print("outer: ", x)
# outer()

# class PlayerCharacter:
#   # class object atribute
#   Membership = True

#   def __init__(self, name='anonymous', age=0):
#     if (age >= 18):
#       self.name = name
#       self.age = age
#     else:
#       print('You are too young to play sir!')

#   def run(self):
#     print(f'My name is {self.name}')
#     return 'done'

#   @classmethod
#   def adding_things(cls, num1, num2):
#     return cls('Teddy', num1 + num2)

#   @staticmethod
#   def adding_things2(num1, num2):
#     return num1 + num2

# Player1 = PlayerCharacter('John', 41)
# Player2 = PlayerCharacter('Tom', 18)

# print(Player1.name)
# print(Player2.name)
# Player3 = PlayerCharacter.adding_things(21,3)
# print(Player3.age)
# print(Player3.name)
# Player1.name = "hacked!"
# print(Player1.name)
# # convention for making names "private" is to write _ before name. eg = "_name"
# print('hello!')

# class User():
#   def sign_in(self):
#     print('signed in')

# class Wizard(User):
#   def __init__(self, name, power):
#     self.name = name
#     self.power = power
#   def attack(self):
#     print(f'{self.name} attacks with {self.power}')

# class Archer(User):
#   def __init__(self, name, arrows_num):
#     self.name = name
#     self.arrows_num = arrows_num
#   def attack(self):
#     print(f'{self.name} attacks with arrows, and have {self.arrows_num} arrows left')

# wizard1 = Wizard('Gandalf', 'fireball')
# archer1 = Archer('Robin', 500)
# print(wizard1.attack())
# print(archer1.attack())
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, User))

# def player_attack(char):
#   char.attack()

# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#   char.attack()

# # introspection
# print(dir(wizard1))

# class Toy():
#   def __init__(self, color, age):
#     self.color = color
#     self.age = age
#     self.my_dict = {
#       'name':'Yoyo',
#       'has pets':False
#     }

#   def __str__(self):
#     return f'{self.color}'

#   def __getitem__(self, i):
#     return self.my_dict[i]

# action_figure = Toy('red', 13)
# print(action_figure.__str__())
# print(str(action_figure))
# print(action_figure['name'])

# class SuperList(list):
#   def __len__(self):
#     return 1000

# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))

# class User():
#   def sign_in(self):
#     print('signed in')

# class Wizard(User):
#   def __init__(self, name, power):
#     self.name = name
#     self.power = power
#   def attack(self):
#     print(f'{self.name} attacks with {self.power}')

# class Archer(User):
#   def __init__(self, name, arrows_num):
#     self.name = name
#     self.arrows_num = arrows_num
#   def attack(self):
#     print(f'{self.name} attacks with arrows, and have {self.arrows_num} arrows left')

# class Hybrid(Wizard, Archer):
#   def __init__(self, name, power, arrow_num):
#     Wizard.__init__(self, name, power)
#     Archer.__init__(self, name, arrow_num)

# hybrid1 = Hybrid('Nina', 'fireball', 50)

# print(hybrid1.sign_in())
# print(hybrid1.attack())
# from functools import reduce
# new_list = [1,2,3]
# your_list = [10,20,30]
# their_list = [5,4,3]

# def multiply_by2(item):
#   return item*2

# def check_odd(item):
#   return item % 2 != 0

# def accumulator(acc, item):
#   return acc + item

# print(list(map(multiply_by2, new_list)))
# print(list(filter(check_odd, new_list)))
# print(new_list)
# print(list(zip(new_list, your_list, their_list)))
# print(reduce(accumulator, new_list, 0))
# # lambda - one time anonymous function
# print(list(map(lambda item: item*2, new_list)))

# square

# my_list = [char for char in 'hello']

# # for char in 'hello':
# #   my_list.append(char)

# print(my_list)

# my_list2 = [num for num in range(0,100)]

# print(my_list2)

# my_list3= [num*2 for num in range(0,100)]

# print(my_list3)

# my_list4= [num**2 for num in range(0,100) if num % 2 == 0]

# print(my_list4)

# simple_dict = {
#   'a':1,
#   'b':2,
#   'c':3,
#   'd':4
# }
# my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
# your_dict = {num:num*2 for num in [1,2,3]}
# print(my_dict)
# print(your_dict)

# higher order function

# def greet(func):
#   func()

# def greet2(func):
#   def func():
#     return 5
#   return func

# def my_decorator(func):
#   def wrap_func():
#     print('****')
#     func()
#     print('****')
#   return wrap_func

# @my_decorator
# def hello():
#   print('helooo')

# hello

# def my_decorator(func):
#   def wrap_func(*args, **kwargs):
#     print('****')
#     func(*args, **kwargs)
#     print('****')
#   return wrap_func

# @my_decorator
# def hello(greeting, emoji):
#   print(greeting, emoji)

# hello('hi', ':P')

# from time import time
# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1} ms')
#     return result
#   return wrapper

# @performance
# def long_time():
#   for i in range(1000000):
#     i*5

# long_time()
# while True:
#   try:
#     age = int(input('what is Your age?: '))
#     10/age
#     print(age)
#   except ValueError:
#     print('Please enter a number')
#     continue
#   except ZeroDivisionError:
#     print('Please enter a number higher than 0')

#   else:
#     print('Thank You!')
#     break
#   finally:
#     print('Ok, im finally done')
#   print('Can you hear me?')

# def sum(num1, num2):
#   try:
#     return num1 + num2
#   except TypeError as err:
#     print(f'please enter a numbers {err}')

# def sum(num1, num2):
#   try:
#     return num1/num2
#   except (TypeError, ZeroDivisionError):
#     print('oops')

# print(sum('1', 2))

# def generator_function(num):
#   for i in range(num):
#     yield i*2

# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))

# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       print(iterator)
#       next(iterator)
#     except StopIteration:
#       break

# special_for([1,2,3])

# class MyGen():
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration

# gen = MyGen(0,100)
# for i in gen:
#   print(i)


# def fib(number):
#   a = 0
#   b = 1
#   for i in range(number):
#     yield a
#     temp = a
#     a = b
#     b = temp + b

# def fib2(number):
#   a = 0
#   b = 1
#   result = []
#   for i in range(number):
#     result.append(a)
#     temp = a
#     a = b
#     b = temp + b
#   return result

# for x in fib(20):
#   print(x)

# print(fib2(20))

# import utility
# import shopping.shopping_cart

# print(utility.multiply(2,3))
# print(utility.divide(6,2))
# print(shopping.shopping_cart.buy('apple'))

# import random

# my_list = [1,2,3,4,5,6]

# print(random.choice([1,2,3,4,5,6]))
# random.shuffle(my_list)
# print(random.randint(1,10))
# print(my_list)

# import random
# random_num = random.randint(1,10)
# user_num = int(input('guess the number from 1 to 10: '))
# if random_num == user_num:
#   print("you got it champ!")
# else:
#   print(f'you missed! The number was {random_num}')

import pyjokes

joke = pyjokes.get_joke('en', 'neutral')

print(joke)

# Usefull modules

from collections import Counter, defaultdict, OrderedDict

# counting items
li = [1,2,3,4,5,6,7,7]
sentence = 'this is a sentence'

print(Counter(li))
print(Counter(sentence))

# adds values to dict
dictionary = defaultdict(lambda: 5,{'a': 1, 'b': 2})
print(dictionary['c'])
print(dictionary['a'])

# checks order - normal dicts has no sence of order
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

import datetime

# creates time objects
print(datetime.time(5,24,2))

# checks date
print(datetime.date.today())

from array import array
# optimalisation
arr = array('i', [1,2,3,4])

print(arr[0])
print(arr[-1])