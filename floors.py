import random
import time
from data import Dagger, Gremlin, Zombie, MagicStones, Nothing, upStairs,downStairs, Boss
stairs = [upStairs(), downStairs()]

#rooms = [Nothing(),Dagger(),Gremlin(),Zombie(),MagicStones()]
rooms = ['Nothing','Dagger','Gremlin','Zombie','MagicStones']

# Generates first floor
def genFloor1():
  floor1 = []
  for i in range(4):
    choice = random.choice(rooms)
    if choice == "Nothing":
      floor1.append(Nothing())
    elif choice == "Dagger":
      floor1.append(Dagger()) 
    elif choice == "Gremlin":
      floor1.append(Gremlin())
    elif choice == "Zombie":
      floor1.append(Zombie())
    elif choice == "MagicStones":
      floor1.append(MagicStones())       
  floor1.append(stairs[0])
  return floor1

# Generates filler (middle) floors
def genMidFloor():
  midFloor = []

  midFloor.append(stairs[1])
  for i in range(3):
    choice = random.choice(rooms)
    if choice == "Nothing":
      midFloor.append(Nothing())
    elif choice == "Dagger":
      midFloor.append(Dagger()) 
    elif choice == "Gremlin":
      midFloor.append(Gremlin())
    elif choice == "Zombie":
      midFloor.append(Zombie())
    elif choice == "MagicStones":
      midFloor.append(MagicStones())       
  midFloor.append(stairs[0])
  return midFloor

def genPreBossFloor():
  floor = []

  floor.append(stairs[1])
  for i in range(2):
    choice = random.choice(rooms)
    if choice == "Nothing":
      floor.append(Nothing())
    elif choice == "Dagger":
      floor.append(Dagger()) 
    elif choice == "Gremlin":
      floor.append(Gremlin())
    elif choice == "Zombie":
      floor.append(Zombie())
    elif choice == "MagicStones":
      floor.append(MagicStones())
  floor.append(Gremlin())  
  floor.append(stairs[0])
  return floor

def genBossFloor():
  bossFloor = []
  for i in range(2):
    bossFloor.append(Nothing())
  bossFloor.append(Boss())
  for i in range(2):
    bossFloor.append(Nothing())
  return bossFloor
