import time
import sys 
import methods



def handleMonsterRoom(roomType, player):
  if roomType.health <= 0:
    methods.typewriter('You have already defeated this monster. Continue to another room to escape.')
    print()
    return
  
  
  methods.typewriter('------------------------------------')
  print()
  methods.typewriter('You enter the room, and inside you encounter a {}'.format(roomType.name))
  print()
  methods.typewriter('The {} is waiting for you, and strikes with {} damage'.format(roomType.name, roomType.damage))
  damageTook = roomType.damage
  player.updateHealth(-int(damageTook))
  print()
  methods.typewriter('------------------------------------')
  print()
  methods.typewriter('After being struck by the {}, you are left with {} health'.format(roomType.name, player.health))
  print()
  while roomType.isAlive:
    if player.health <= 0:
      return
    methods.typewriter('What will you do?')
    print()
    print('1. Attack the monster')
    print('2. Flee')
    desc = input('dd1-me> ')
    print()
    if desc == "1":
      methods.typewriter('You decided to attack the {}, and deal {} damage to it.'.format(roomType.name, player.damage))
      damage = player.damage
      roomType.updateHealth(-int(damage))
      print()
      methods.typewriter('The {} has {} health left.'.format(roomType.name,roomType.health))
      print()
      if roomType.health <= 0:
        print('Congratulations, you defeated the {}'.format(roomType.name)) 
        break
      methods.typewriter('The {} strikes back and does {} damage to you.'.format(roomType.name, roomType.damage))
      print()
      DamageTook = roomType.damage
      player.updateHealth(-int(DamageTook))
      methods.typewriter('You are left with {} health.'.format(player.health))
      print()
      methods.typewriter('------------------------------------')
      print() 
      if roomType.health <= 0:
        print('Congratulations, you defeated the {}'.format(roomType.name))
        return   
        break
    elif desc == "2":
      print('You decided to flee')
      break
      return
    else:
      print('Please input what you want to do.')




def handleItemRoom(roomType, player):
  if roomType.grabbed:
    methods.typewriter('You have already found this item. Continue to another room to escape.')
    print()
    return
  if roomType.name == "Nothing":
    methods.typewriter("You enter the room, but you find nothing inside.")
    print()
    return
  methods.typewriter('You enter the room, and inside you find {}'.format(roomType.name))
  print()
  methods.typewriter('Upon inspecting the {}, you decide to take it to be used in your escape.'.format(roomType.name))
  print()
  methods.typewriter('Item {} was added to your inventory!'.format(roomType.name))
  print()
  methods.typewriter('------------------------------------')
  print()

  if roomType.name == "Magic Stones": 
    player.addItem(roomType)
    player.health = player.health + 100
    roomType.grabbed = True
    return
  if roomType.name == "Dagger": 
    player.addItem(roomType)
    player.damage = roomType.damage + player.damage
    roomType.grabbed = True
    return
