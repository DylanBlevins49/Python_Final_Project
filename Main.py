#Dylan Blevins
#Final Project
import time
import sys
import os
from termcolor import cprint
inventory = []
def clear():
  os.system("clr" if os.name == "nt" else "clear")
def airlock(inventory):
  global inventoy
  userchoice = None
  clear()
  cprint('The door seals behind you as the airlock door closes. The oxygen levels seem sufficiant so you remove your helmet. The air feels cold, heat must be broken. The emergency S.O.S. is still beeping on your handheld console. You look around and see empty floors and bare walls. It seems like a pretty safe area. only two doors decorate the walls. One is the airlock you just came through, the other is oposite the airlock door. which door do you go through?', "cyan")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input('For the airlock door enter 1:\nFor the door into the ship enter 2:\n')
  if userchoice == '1':
    cprint('you open the airlock door and it appears your ship has undocked. The lifeless vacuum of space sucks you into oblivion. Your blood boils as your eyes pop. You have failed the objective. GAME OVER!' , 'red')
    sys.exit()
  elif userchoice == '2':
    clear()
    time.sleep(3.0)
    mainhall(inventory)
  else:
    cprint("That is not an option please select again", "green")
    airlock(inventory)
def mainhall(inventory):
  # global inventory
  userchoice = None
  clear()
  cprint('The door sticks but finally budges. as it creaks open the ghastly smell of death seeps through. The ship is completely silent save the zapping noise of loose electrical wires. The overhead light fixtures hum and zap as the lights flicker repeatedly. On the corner of the wall under a bloody handprint you read the words MAIN HALL.', 'cyan')
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input("Once you finally enter you see a plethora of doors. The first door to your right reads MESS HALL. The next room on the right reads MAINTANENCE. Straight ahead you see a stairwell lableled LVL 2. To the left is one door labeled BARRACKS. Which door you choose to enter?\nFor Messhall enter 1:\nFor Maintennce enter 2:\nFor Stairwell enter 3:\n For Barracks enter 4:\nTo return to the airlock enter 5:\nTo exit the game enter 6:\n")
  if userchoice == '1':
    clear()
    time.sleep(2.0)
    messhall(inventory)
  elif userchoice == '2':
    clear()
    time.sleep(2.0)
    maintanence(inventory)
  elif userchoice == '3':
    clear()
    time.sleep(2.0)
    secondfloorstairwell(inventory)
  elif userchoice == '4':
    clear()
    time.sleep(2.0)
    barracks(inventory)
  elif userchoice == '5':
    time.sleep(2.0)
    airlock(inventory)
  elif userchoice == '6':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please choose again!", "red")
    clear()
    mainhall(inventory)
def barracks(inventory):
  # global inventory
  userchoice = None
  clear()
  cprint("You enter the barracks. Clean orderly bunks line the walls. Screams can be heard echoing through the vents from deeper in the ship. The center of the room is decorated by a bloody mess. Dragmarks through the blood lead to a chest in the corner.", "cyan")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input("To check the contents of the chest enter 1:\nTo go back into the mainhall enter 2:\nTo quit the game enter 3:\n")
  if userchoice == '1':
    clear()
    time.sleep(2.0)
    cprint("you open the chest and a bloody decapitated head stares back at you. You jump back after slamming the lid shut. There didnt seem to be anything of value in there. ", "green")
    time.sleep(8.0)
    barracks(inventory)
  elif userchoice == '2':
    clear()
    time.sleep(2.0)
    mainhall(inventory)
  elif userchoice == '3':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please choose again!\n", "red")
    barracks(inventory)
def messhall(inventroy):
  userchoice = None
  clear()
  cprint("You open the door and immediately vomit from the smell of rotten food and human decay. Bodies litter the floor (all appear lifeless), half eaten rations and silverware clutter the floor as well. there appears to have been a great struggle in here. No weapons can be seen, they must have been attacked when they werent expecting it. After surveying the main room you see nothing of value you. You step into the kitchen area.", "cyan")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input("After entering the kitchen area you find everything in dissaray. out of the corner of your eye you spot a key. It must be for the freezer. To pick up the key and enter the freezer enter 1:\n To return to the main hall enter 2:\nTo exit the game enter 3:\n")
  if userchoice == '1':
    clear()
    time.sleep(2.0)
    cprint("You pick up the Key and use it to unclock the freezer door. It flies open as half frozen bodies fall out. You see someone who appears to be a high ranking officer with a keycard attached to his waist. it must be of some value so you take it.", "cyan")
    time.sleep(10.0)
    cprint("The officers eyes fly open as he screams and grabs your hand. you snage the keycard before managing to slam the door shut. Theres no way he should still be alive. Something sinister must be spreading across the ship. You need to get out of there as quicly as possible", "red")
    inventory.append("Keycard")
    time.sleep(10.0)
    messhall(inventory)
  elif userchoice == '2':
    clear()
    time.sleep(2.0)
    mainhall(inventory)
  elif userchoice == '3':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please try again!", "red")
    messhall(inventory)

def maintanence(inventory):
  userchoice = None
  clear()
  cprint("You enter the maintenance room. Cobwebs and dust litter the shelves, its a very small room. It appears to be mostly cleaning supllies but you spot a toolbox in the corner", "cyan")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input("To search the toolbox enter 1:\nTo return to the main hall enter 2:\nTo quit the game enter 3:\n")
  if userchoice == '1':
    clear()
    time.sleep(2.0)
    cprint("You search the toolbox and find an 8 inch pipe wrench. could be used as a weapon in a pinch if needed. you add it to your bag", "green")
    inventory.append("pipewrench")
    time.sleep(8.0)
    maintanence(inventory)
  elif userchoice == '2':
    clear()
    time.sleep(2.0)
    mainhall(inventory)
  elif userchoice == '3':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please try again!", "red")
    maintanence(inventory)
def secondfloorstairwell(inventory):
  userchoice = None
  clear()
  cprint("You walk down the hall to the stairwell. You peer up the stairs and notice a severed hand gripping the railing. you hear a gurgling, gutteral noise as something hops from the top landing.", "cyan")
  time.sleep(10.0)
  cprint("Staring you in the face is the bloody embodyment of pure hell. Jagged fangs twist from its mouth as it emits the screams all of those its consumed. The eyeless forms opens its mouth and lunges at you as you freeze in pure terror.", "red")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(8.0)
  print("\n\n")
  userchoice = input("You must react quickly.\nTo fight back enter 1:\nTo retreat back to the airlock enter 2:\nTo exit the game enter 3:\n")
  if userchoice == '1' and 'pipewrench' in inventory:
    clear()
    time.sleep(2.0)
    cprint("You strike the beast across the mouth sending it flailing. It stands up but only to retreat back up the stairs. It rest for now but the beast will find you again. BE PREPARED", "green")
    time.sleep(10.0)
    mainhall2(inventory)
  elif userchoice == '1' and "pipewrench" not in inventory:
    clear()
    cprint("The beast tears into your throat sucking your scream through the wound to add to its terrifying collection. The room turns black as the gratifying feeling of death envolopes you. GAME OVER", "red")
    sys.exit()
  elif userchoice == '2':
    clear()
    time.sleep(2.0)
    cprint("You turn around and run back to the airlock as quickly as possible. you slam the door back shut just as the disfigured hand of the beast reaches the opening. You barely made it. Youre lucky this time.", "green")
    time.sleep(7.0)
    airlock(inventory)
  elif userchoice == '3':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please try again!", "red")
    secondfloorstairwell(inventory)
def mainhall2(inventory):
  userchoice = None
  clear()
  cprint("Fueled by adrenaline you sprint up the stairs after the beast. You reach the second floor hall in time to watch it seemingly flow the the crack in a door labeled Command control. Only one other door disrupts the wall. Its labeled Medical", "cyan")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input("Still reeling with adrenaline and anxiety you have to decide what to do. Follow the beast into the command center, or check out medical.\nTo follow the beast into command enter 1:\nTo enter the medical wing enter 2:\nTo return to the LVL 1 main hall enter 3:\nTo quit the game enter 4:\n")
  if userchoice == '1' and "Keycard" in inventory:
    clear()
    time.sleep(2.0)
    cprint("I wonder if that keycard i found before will work", "cyan")
    commandcenter(inventory)
  elif userchoice == '1' and "Keycard" not in inventory:
    cprint("The door is locked, I need to find a keycard. Maybe I should check downstairs", "green")
    time.sleep(5.0)
    mainhall2(inventory)
  elif userchoice == '2':
    clear()
    time.sleep(2.0)
    cprint("Maybe I should check medical for supplies and hopefully a weapon", "cyan")
    medical(inventory)
  elif userchoice == '3':
    clear()
    time.sleep(2.0)
    mainhall(inventory)
  elif userchoice == '4':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please try again!", "red")
    time.sleep(2.0)
    mainhall2(inventory)
def medical(inventory):
    userchoice = None
    clear()
    cprint("You slowly ease the door open as blinding white light from the medical lights blinds you. Once your eyes adjust you stare on in pure horror as all you can see is piles of bodies with their throats ripped out. Faces frozen in expressions of pure agony and terror", "cyan")
    print("\n")
    cprint("inventory:" + str(inventory), "green")
    time.sleep(3.0)
    print("\n\n")
    userchoice = input("Once you become used to the gruesome nature of the place you look around and unfortunatley find nothing of real value. Only one other door can be seen in the room. Its label reads ..... Morgue.\nTo enter the morgue enter 1:\nTo go back into the hallway enter 2:\nTo quit the game enter 3:\n")
    if userchoice == '1':
      clear()
      time.sleep(2.0)
      morgue(inventory)
    elif userchoice == '2':
      time.sleep(2.0)
      mainhall2(inventory)
    elif userchoice == '3':
      clear()
      sys.exit()
    else:
      cprint("That is not an option please try again!", "red")
    time.sleep(2.0)
    medical(inventory)
def morgue(inventory):
  userchoice= None
  clear()
  cprint("With nothing more than pure terror in your heart you open the door to the morgue. To your suprise the place is.... actually really clean and tidy. All those scary movies and stories as kids really arent true then. Not a single body to be seen. All that can be seen is an incinerator, and a metal table with some sort of syringe filled with bright green fluid.","cyan")
  print("\n")
  cprint("inventory:" + str(inventory), "green")
  time.sleep(3.0)
  print("\n\n")
  userchoice = input("The label on the fluid reads: only for use in defcon 5 scenario. You dont know what defcon 5 means but it might be useful.\nTo pick up the mystery fluid and return to the hallway enter 1:\nTo return to medical enter 2:\nTo quit the game enter 3:\n")
  if userchoice == '1':
    clear()
    time.sleep(2.0)
    inventory.append("Syringe")
    cprint("Well hopefully this will will come in handy. You place the syringe into your bag and head to the hallway","green")
    time.sleep(3.0)
    mainhall2(inventory)
  elif userchoice == '2':
    cprint("You decide the leave the syringe and head back into medical","red")
    time.sleep(2.0)
    medical(inventory)
  elif userchoice == '3':
    time.sleep(2.0)
    sys.exit()
  else:
    cprint("That is not an option please try again!", "red")
    time.sleep(2.0)
    mainhall2(inventory)
def commandcenter(inventory):
      userchoice = None
      clear()
      cprint("The door opens with a hiss as you press the keycard to the reciever. The interior of the room is completely black. The gurgling of the beast can be heard in the far corner. The only light in the room is coming from the emrgency S.O.S. broadcast that brought you here in the first place.", "cyan")
      time.sleep(8.0)
      cprint('Suddenly the lights flicker and the beast roars with a thousand screams as it lunges towards you. Your first thought is to use the wrench, but all that did was scare it away the first time. You need something better this time.',"red")
      print("\n")
      cprint("inventory:" + str(inventory), "green")
      time.sleep(5.0)
      print("\n\n")
      userchoice = input('with only a split second to decide what do you choose?:\nTo end this once and for all enter 1:\nTo retreat to the hallway enter 2:\nTo exit the game enter 3:\n')
      if userchoice == '1' and "Syringe" in inventory:
        clear()
        time.sleep(2.0)
        cprint("You pull the syringe from your bag at the last second. as the beast comes in contact with you the needle plunges deep into its throat. As the beast screams it almost seems to flicker in the the light. Eyes appear from a place where previously there were none, they were none other than your own","red")
        time.sleep(12.0)
        finale(inventory)
      elif userchoice == '1' and "Syringe" not in inventory:
        cprint("The beast lunges forward as you strike it with the pipe, nothing happens this time as the beast clamps its fangs along you neck. Sucking the very scream you emit through the wound. blackness envolopes you as you welcome the warmth of death. GAME OVER", "red")
        time.sleep(8.0)
        sys.exit()
      elif userchoice == '2':
        clear()
        time.sleep(2.0)
        cprint("Im not ready for this fight","green")
        mainhall2(inventory)
      elif userchoice == '3':
        time.sleep(2.0)
        sys.exit()
      else:
        cprint("That is not an option please try again!", "red")
        time.sleep(2.0)
        commandcenter(inventory)
def finale(inventory):
  cprint('As you stare into the eyes of the beast your own eyes stare back at you. You find some comfort in the metaphor of it all as you observe the beast within yourself. That all melts away pretty quickly when the fluid in the syringe turns from green to black and the monster seems to vanish into thin air. You stand frozen in pure amazement at what just happened. You look at the syringe and notice the fine print reads that after use the syringe must be destroyed in the incernerator. You make you way back to the morgue after disabling that annoying S.O.S. beacon. You stand in horror as you realize the incinerator isnt working. you try everything in your power to make it functional again but nothing works. You sit and ponder what options you have in the captains chair in the command room. You shuttr as the vile starts to heat and crack releasing faint screams. The realization of what is about to happen hits you as the black fluid burst from the cracks in the syringe. You feel and incredible burning sensation as the fluid begins to overtake your human form. In a last minute effort you power the ship back on and open the shutters to reveal the nearest sun. You set your control module to fly directly into the nearest sun. It will be nowhere near close enough to happen anytime soon but you cant let this thing escape to other ships or planets. The fluid overtakes you as you are consumed into a world of pure nightmare of your own design. all of your worst fears stare you down as the darkness consumes you.',"cyan")
  time.sleep(35.0)
  cprint('the control module springs to life with a new message as your newfound host puppets your body out of the chair. MISSION COMPLETE: Returning Ship To Nearest Port For Refuel and Restock...Standby', "red")
  time.sleep(5.0)
  cprint("The beast lives on to spread among the stars and consume all life.","red")
  time.sleep(5.0)
  sys.exit()
def clear():
  os.system("clr" if os.name == "nt" else "clear")
airlock(inventory)
