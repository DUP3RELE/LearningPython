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

class PlayerCharacter:
  # class object atribute
  Membership = True
  
  def __init__(self, name='anonymous', age=0):
    if (age >= 18):
      self.name = name
      self.age = age
    else:
      print('You are too young to play sir!')

  def run(self):
    print(f'My name is {self.name}')
    return 'done'

  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)

  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2

Player1 = PlayerCharacter('John', 41)
Player2 = PlayerCharacter('Tom', 18)

print(Player1.name)
print(Player2.name)
Player3 = PlayerCharacter.adding_things(21,3)
print(Player3.age)
print(Player3.name)

