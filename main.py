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
is_magician = False
is_expert = True

if is_magician and is_expert:
  print('You are master magician!')

elif is_magician or is_expert:
  print('At least You\'re getting there')

if not(is_magician):
  print('You need to learn magic')