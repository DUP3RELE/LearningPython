import random
random_num = random.randint(1,10)
user_num = int(input('guess the number from 1 to 10: '))
if random_num == user_num:
  print("you got it champ!")
else:
  print(f'you missed! The number was {random_num}')


# import random
# import sys

# random_num2 = random.randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#   try:
#     user_num = int(input('guess the number from 1 to 10: '))
#     if  0 < user_num < 11:
#       if user_num == random_num2:
#         print("you got it champ!")
#         break
#     else:
#       print(f'you missed!')
#   except ValueError:
#     print('Please give me number 1-10')
#     continue