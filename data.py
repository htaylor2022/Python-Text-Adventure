import random
from user import User

# Declate item class
class Item():
  type = 'Item'
  def __init__(self, name, description, value, grabbed):
    self.name = name
    self.description = description
    self.value = value
    self.grabbed = grabbed
# Declate monster class
class Monster():

  type = 'Monster'
  def __init__(self, name, health, damage,):
    self.name = name
    self.health = health
    self.damage = damage    
  def isAlive():
    if self.health > 0:
      return True
    else:
      return False
  def updateHealth(self, healthChange):
    self.health = self.health + healthChange 




# Declaring weapon class
class Weapon(Item):
  type = 'Weapon'
  def __init__(self, name, description, value, damage, grabbed):
    self.damage = damage
    super().__init__(name, description, value, grabbed)




# Declaring floors class

class room():
  def __init__(self, name):
    self.name = name

class upStairs(room):
  type = 'upStairs'
  def __init__(self):
    super().__init__(name='up stairs')
class downStairs(room):
  type = 'downStairs'
  def __init__(self):
    super().__init__(name='down stairs')






# Declaring items
class Dagger(Weapon):
  def __init__(self):
    super().__init__(name="Dagger", description="A small tool fit for the job \n Damage: 55", value=0, damage=55, grabbed=False)
class DevSword(Weapon):
  def __init__(self):
    super().__init__(name="Dev Sword", description="op loser \n Damage: 1000", value=1, damage=1000, grabbed=False)

class MagicStones(Item):
    def __init__(self):
      super().__init__(name="Magic Stones", description="Magic stones that increase health", value=2, grabbed=False)

      
class Nothing(Item):
    def __init__(self):
      super().__init__(name="Nothing", description="", value=2, grabbed=False)






# Declaring monsters

class Gremlin(Monster):
  def __init__(self):
    super().__init__(name="Gremlin", health= random.randint(55,73), damage= random.randint(48,63))


class Zombie(Monster):
  def __init__(self):
    super().__init__(name="Zombie", health= random.randint(55,73), damage= random.randint(48,63))

class Skeleton(Monster):
  def __init__(self):
    super().__init__(name="Skeleton", health= random.randint(68,84), damage= random.randint(49,74))

class Boss(Monster):
  def __init__(self):
    super().__init__(name="Boss", health= 312, damage= random.randint(48,73))



