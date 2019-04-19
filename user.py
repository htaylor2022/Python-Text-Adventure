import random
import time
import floors
class User:
  def __init__(self):
    self.current_floor = 0
    self.items = []
    self.health = 180
    self.damage = random.randint(19,35)
    self.DEVELOPER_MODE = True
    # Generate floor1s
    self.floor1 = floors.genFloor1()
    self.floor2 = floors.genMidFloor()
    self.floor3 = floors.genMidFloor()

    # Generate floor before boss
    self.floor4 = floors.genPreBossFloor()

    # Generate boss level
    self.floor5 = floors.genBossFloor()

  def updateFloor(self, floor):
    self.current_floor = floor   
  def addItem(self, item):
    self.items.append(item)
  def updateHealth(self, healthChange):
    self.health = self.health + healthChange 
  def updateDamage(self, damageChange):
    self.damage = self.damage + damageChange  
