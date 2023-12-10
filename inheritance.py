class User():
  def sign_in(self):
    print('signed in')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power
  def attack(self):
    print(f'{self.name} attacks with {self.power}')


class Archer(User):
  def __init__(self, name, arrows_num):
    self.name = name
    self.arrows_num = arrows_num
  def attack(self):
    print(f'{self.name} attacks with arrows, and have {self.arrows_num} arrows left')


wizard1 = Wizard('Gandalf', 'fireball')
archer1 = Archer('Robin', 500)
print(wizard1.attack())
print(archer1.attack())