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

for i,char in enumerate('helloooooo'):
  print(i,char)
for item in range(0,10):
  print(item)

for i,char in enumerate(range(100)):
  if char == 50:
    print(i, char)