import time
import floors
from user import User
from methods import typewriter, enterRoom, helpScreen, commandHandler






# Instantiate user class
player = User()




# print("Floor 1")
# print(player.floor1)

# print("Floor 2")
# print(player.floor2)

# print("Floor 3")
# print(player.floor3)

# print("Floor 4")
# print(player.floor4)

# print("Floor 5")
# print(player.floor5)


# Begin game
print('\n' * 100)
print('\n\nWelcome to Dungeon Delver 1!')
print('\nDeveloped by Hayden Taylor, 4/9/2019')
print('\n\n\n------------------------')
print('     DUNGEON DELVER    ')
print('------------------------')
print('\nv0.1.6 : Dungeon Delver 1\n ')
time.sleep(1)
typewriter("You have mysteriously appeared in the bottom of a tower. You don't know how you got here, or where you are.")
print('\n')
time.sleep(1)
typewriter("Upon looking around the empty, seemingly abandoned room, you see a old, broken door.")
print('\n')
time.sleep(2)
typewriter("Realizing you're not restrained, you stand up and walk to the door. You open the door slowly, hoping to not alert your captors of your escape.")
print('\n')
time.sleep(3)
typewriter("After opening the door, you are met with a hallway with 5 doors, each presumeably leading to escape.")
print('\n')
time.sleep(1)
typewriter("Suddenly, the door you entered the hallway from slams shut, and you hear the sound of a lock tightening on the other side.")
print('\n')
time.sleep(2)
typewriter("You are left with no other choice than to traverse the tower through each of these doors. What will you do? ")
time.sleep(2)
print('\n')


def start(player):
  print('------------------------------------')
  if player.current_floor == 0:
    for i in range(len(player.floor1)):
      print('{}. Enter Room {}'.format(i+1,i+1))
  print('type help for more information')

  

  
  # Handling user input
  commandHandler(player)

  
  
  





if __name__ == "__main__":
	start(player)
