
def highest_even(li):
  highest = 0
  for num in li:
    if num % 2 == 0 and num > highest:
        highest = num
  return highest


print(highest_even([10,4,5,11,8,3,2]))