import time
import sys 
from roomHandlers import handleMonsterRoom, handleItemRoom
from user import User
import floors
import data





def typewriter(text):
  for char in text:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

def enterRoom(roomType, player):
  if roomType.type == "Monster":
    handleMonsterRoom(roomType, player)
    
  elif roomType.type == "Item":
    handleItemRoom(roomType, player)
    
  elif roomType.type == "Weapon":
    handleItemRoom(roomType, player)
  elif roomType.type == "upStairs":
    player.current_floor = player.current_floor + 1
    typewriter("Upon entering this room, you're met with a staircase. You decide to go up the staircase, and are now on floor {}".format(player.current_floor + 1))
    print()
  elif roomType.type == "downStairs":
    player.current_floor = player.current_floor - 1
    typewriter("Upon entering this room, you're met with a staircase. You decide to go down the staircase, and are now on floor {}".format(player.current_floor + 1))  
    print()
    

def commandHandler(player):
  while True:
    # What happens when the game ends
    if player.current_floor == 4:
      if player.floor5[2].health <= 0:
        print()
        typewriter("Upon defeating the final boss, a trap door in the ceiling opens, and a staircase to the roof appears.")
        print()
        typewriter('You take the staircase to the top of the roof, and are met with a rope that falls to the ground.')
        print()
        typewriter("You grab ahold of the rope, and slide down to the ground. You've escaped the tower, what you do next is up to you.")
        typewriter('.....')
        print()
        time.sleep(0.5)
        typewriter('.....')
        print()
        time.sleep(0.5)
        typewriter('.....')
        print()
        time.sleep(0.5)
        typewriter('.....')
        print()
        typewriter('Thank you for playing Dungeon Delver!')
        return  

    if player.health <= 0:
      print()
      typewriter('Your journey to escape has come to an end. This is the end of your story..........')
      print()
      print('Restart game to restart your journey.')
      return


    if player.current_floor == 0:
      userInput = input('dd1> ')
      if userInput == str(1):
        enterRoom(player.floor1[0], player)
      elif userInput == str(2):
        enterRoom(player.floor1[1], player)
      elif userInput == str(3):
        enterRoom(player.floor1[2], player)
      elif userInput == str(4):
        enterRoom(player.floor1[3], player)
      elif userInput == str(5):
        enterRoom(player.floor1[4], player)
      elif userInput.lower() == 'help':
        helpScreen(player)
      elif userInput.lower() == 'info':
        infoScreen(player)
      elif userInput.lower() == 'floor':
        print('Current Floor: {}'.format(player.current_floor+1))
      elif userInput.lower() == 'spawnsword()':
        if player.DEVELOPER_MODE:
          devSword = data.DevSword()
          print('Developer Sword added!')
          player.addItem(devSword)
          player.updateDamage(devSword.damage)
        else:
          print('ERROR: Developer mode must be enabled for this command.')  
        
      else:
        print("ERROR: Please input the number of the room you're trying to enter. Type 'help' for more information.")
    if player.current_floor == 1:
      userInput = input('dd1> ')
      if userInput == str(1):
        enterRoom(player.floor2[0], player)
      elif userInput == str(2):
        enterRoom(player.floor2[1], player)
      elif userInput == str(3):
        enterRoom(player.floor2[2], player)
      elif userInput == str(4):
        enterRoom(player.floor2[3], player)
      elif userInput == str(5):
        enterRoom(player.floor2[4], player)
      elif userInput.lower() == 'help':
        helpScreen(player)
      elif userInput.lower() == 'info':
        infoScreen(player)
      elif userInput.lower() == 'floor':
        print('Current Floor: {}'.format(player.current_floor+1))
      elif userInput.lower() == 'spawnsword()':
        if player.DEVELOPER_MODE:
          devSword = data.DevSword()
          print('Developer Sword added!')
          player.addItem(devSword)
          player.updateDamage(devSword.damage)
        else:
          print('ERROR: Developer mode must be enabled for this command.')  
        
      else:
        print("ERROR: Please input the number of the room you're trying to enter. Type 'help' for more information.")    
    if player.current_floor == 2:
      userInput = input('dd1> ')
      if userInput == str(1):
        enterRoom(player.floor3[0], player)
      elif userInput == str(2):
        enterRoom(player.floor3[1], player)
      elif userInput == str(3):
        enterRoom(player.floor3[2], player)
      elif userInput == str(4):
        enterRoom(player.floor3[3], player)
      elif userInput == str(5):
        enterRoom(player.floor3[4], player)
      elif userInput.lower() == 'help':
        helpScreen(player)
      elif userInput.lower() == 'info':
        infoScreen(player)
      elif userInput.lower() == 'floor':
        print('Current Floor: {}'.format(player.current_floor+1))
      elif userInput.lower() == 'spawnsword()':
        if player.DEVELOPER_MODE:
          devSword = data.DevSword()
          print('Developer Sword added!')
          player.addItem(devSword)
          player.updateDamage(devSword.damage)
        else:
          print('ERROR: Developer mode must be enabled for this command.')  
        
      else:
        print("ERROR: Please input the number of the room you're trying to enter. Type 'help' for more information.")

    if player.current_floor == 3:
      userInput = input('dd1> ')
      if userInput == str(1):
        enterRoom(player.floor4[0], player)
      elif userInput == str(2):
        enterRoom(player.floor4[1], player)
      elif userInput == str(3):
        enterRoom(player.floor4[2], player)
      elif userInput == str(4):
        enterRoom(player.floor4[3], player)
      elif userInput == str(5):
        enterRoom(player.floor4[4], player)
      elif userInput.lower() == 'help':
        helpScreen(player)
      elif userInput.lower() == 'info':
        infoScreen(player)
      elif userInput.lower() == 'floor':
        print('Current Floor: {}'.format(player.current_floor+1))
      elif userInput.lower() == 'spawnsword()':
        if player.DEVELOPER_MODE:
          devSword = data.DevSword()
          print('Developer Sword added!')
          player.addItem(devSword)
          player.updateDamage(devSword.damage)
        else:
          print('ERROR: Developer mode must be enabled for this command.')  
        
      else:
        print("ERROR: Please input the number of the room you're trying to enter. Type 'help' for more information.")  

    if player.current_floor == 4:
      userInput = input('dd1> ')
      if userInput == str(1):
        enterRoom(player.floor5[0], player)
      elif userInput == str(2):
        enterRoom(player.floor5[1], player)
      elif userInput == str(3):
        enterRoom(player.floor5[2], player)
      elif userInput == str(4):
        enterRoom(player.floor5[3], player)
      elif userInput == str(5):
        enterRoom(player.floor5[4], player)
      elif userInput.lower() == 'help':
        helpScreen(player)
      elif userInput.lower() == 'info':
        infoScreen(player)
      elif userInput.lower() == 'floor':
        print('Current Floor: {}'.format(player.current_floor+1))
      elif userInput.lower() == 'spawnsword()':
        if player.DEVELOPER_MODE:
          devSword = data.DevSword()
          print('Developer Sword added!')
          player.addItem(devSword)
          player.updateDamage(devSword.damage)
        else:
          print('ERROR: Developer mode must be enabled for this command.')  
        
      else:
        print("ERROR: Please input the number of the room you're trying to enter. Type 'help' for more information.")             

def helpScreen(player):
  print('------------------------------------')
  #print('\n')
  print('             Help Menu:')
  print('\n')
  print("1. Enter command 'info' to view all relevant information for your player")
  print("2. Enter command 'floor' to view the current floor")
  print("3. To enter a room, enter the number of the room into the console")
  print('\n')


def infoScreen(player):
  print('------------------------------------')
  #print('\n')
  print('             Info Menu:')
  print('\n')
  print('Current Health: {}'.format(player.health))
  print('Current Damage: {}'.format(player.damage))
  print('Current Floor: {}'.format(player.current_floor+1))
  print('Items:')
  for idx, val in enumerate(player.items):
    print(str(idx+1) + '.', val.name + '\n')
    print('Description: {}'.format(val.description))
