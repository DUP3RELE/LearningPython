name = input('What is your name?')
print('hello ' + name)
print(type(2 + 4))
print(4 + 4)
print(type(6 / 2))
print(14 // 3)
print(14% 3)
print(round(1.67))
print(abs(-20))
iq = 190
variable
print(iq)
constant
PI = 3.14
a,b,c = 1,2,3
print(a)
print(b)
print(c)
some_value = 5
some_value += 2
print(some_value)
first_name = 'Krystian'
last_name = 'Żywczak'
full_name = first_name + " " + last_name
print(full_name)
weather = "\t it\'s \"kind of\" sunny \n hope You have a good day!"
print(weather)

name = 'Johnny'
age = 55
print(f'hey {name}, You are {age} years old')
print('hey {}, You are {} years old'.format(name, age))
print('hey {1}, You are {0} years old'.format(name, age))
selfish = 'me me me'
print(selfish[0:5])
print(selfish[0:8:3])
print(selfish[::-1])
# 1.26
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.replace('be', 'me'))
li = [1,2,3,4,5]
matrix = [[1,2,3],[2,4,6],[1,3,5]]
li.extend([100, 5])
print(li)
li.pop()
print(li)
li.pop(0)
print(li)
li.remove(4)
print(li)

basket = ['b', 'd', 'y', 'g', 'b', 'd', 'y', 'r', 'b', 'd', 'a', 'z']
# basket.sort()
print(basket)

# creates a new array! (sorted)
print(sorted(basket))

basket.reverse()
print(basket)

print(list(range(1, 100)))

sentence = ' '

new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Krystian'])

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Krystian'])

print(new_sentence)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

dictionary = {'a': 1, 'b': 2, 'c': 3}

print(dictionary['b'])

dictionary inside of a list, list is sorted, dict is not!

list = [{
    'a': 1,
    'b': 2,
    'c': 3
}, {
    'd': 4,
    'e': 5,
    'f': 6
}, {
    'g': 7,
    'h': 8,
    'i': 9
}]

list = [1,2,3,4,5,6,7,7,7]

user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user.get('height',180))
print('basket' in user)
list2 = list.copy()
print(list.clear())
print(list2)
# tuple = () list = [], dict = {key:value}, set = {}
tuple = (1,2,3,4,5)
my_set = {1,2,3,4,5,5,5}
print(my_set)
print(len(list))