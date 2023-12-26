import random
random_num = random.randint(1,10)
user_num = int(input('guess the number from 1 to 10: '))
if random_num == user_num:
  print("you got it champ!")
else:
  print(f'you missed! The number was {random_num}')