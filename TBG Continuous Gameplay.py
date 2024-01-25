#TBG Continuous Gameplay - Adil Chowdhury
#Jan 24, 2024
#This Program is a Texted-Based Game and it is about a murder myster.
#you must go and find the killer. Everything we have learned in CS 30
#has lead to this project

import cmd
import os
import textwrap
import sys

class inventory:   				#class for Inventory 
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        """adds items to the inventory"""
        self.items.append(item)
        print(f"{item} added to inventory.")
        
    def remove_item(self, item):
        """removes items from the inventory"""
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")
    
    def display_inventory(self):
        """displays the inventory in terminal"""
        if self.items:
            print("Inventory: ")
            for item in self.items:
                print(f" - {item}")
        else:
            print("Your inventory is empty.")

class player: 				#Class for the player 
    def __init__(self):
        """intilization of the player"""
        self.name = ''
        self.hp = 100
        self.location = 'b2'
        self.game_over = False
        self.inventory = inventory()
    
    def pick_up_item(self, item):
        """pick up items"""
        self.inventory.add_item(item)
        
    def drop_item(self, item):
        """drop items"""
        self.inventory.remove_item(item)
        
    def show_inventory(self):
        """shows the inventory"""
        print(f"{self.name}'s Inventory: ")
        self.inventory.display_inventory()

class map:						#class for the map of the game
    def __init__(self):
        """intilization of map"""
        self.map_data = [
            ['Start', 'f1', 'library', 'f2'],
            ['kitchen', 'f3', 'f4', 'conservatory'],
            ['f5', 'study', 'f6', 'f7'],
            ['ballroom', 'f8', 'lounge', 'dinningroom'],
        ]    
        
        self.current_location = (0,0)		#sets starting location at 0, 0
        self.inventory = inventory()		#allows us to access the inventory class
        
    def move(self, direction):
        """handles the players movement in the game"""
        x, y = self.current_location
        
        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < len(self.map_data) - 1 :
            x += 1
        elif direction == "left" and y > 0:
            y -=1
        elif direction == "right" and y < len(self.map_data[0]) - 1:
            y += 1
        
        zone_name = self.map_data[x][y] 			#sets the room name to where the player is
        option = input(f"Do you want to enter the {zone_name}? (yes/no?) ").lower() #asks if the player is sure they want to enter
        
        #if the player says yes print the location name if not don't
        if option.lower() == "yes":       
            self.current_location = (x, y)
            print(f"You are in {zone_name}.")
            self.interact(x, y)
        else:
            print(f"You chose not to enter the {zone_name}.")
        
    def interact(self, x, y):
        """handles all the interactions within the map"""
        zone_name = self.map_data[x][y]
        
        #If player is in room f3 give them the choice of picking up an item
        if zone_name == "f3":
            item = "knife"
            print(f"you found a {item} in f3!")
            option = input("Do you want to pick this item up? ").lower()
            if option.lower() == "yes":
                myPlayer.pick_up_item(item)
                print(f"{item} has been added to your inventory!")
            else:
                print(f"{item} was left in f3.")
        
        #If player is in room f6 give them the choice of picking up an item 
        elif zone_name == "f6":
            item = "gun"
            print(f"you found a {item} in f6!")
            option = input("Do you want to pick this item? ").lower()
            if option.lower() == "yes":
                myPlayer.pick_up_item(item)
                print(f"{item} has been added to your inventory!")
            else:
                print(f"{item} was left in f6.")
        
        #If the player is in room f8 give them the choice of picking up an item 
        elif zone_name == "f8":
            item = "lead pipe"
            print(f"you found a {item} in f8!")
            option = input("Do you want to pick this item up? ").lower()
            if option.lower() == "yes":
                myPlayer.pick_up_item(item)
                print(f"{item} has been added to your inventory!")
            else:
                print(f"{item} has been left in f8")
                
        #If the player is in the dinning room make them guess who the killer is
        #If they are right they win, if they are wrong they lose
        elif zone_name == "dinningroom":
            print("You find Gwen's lifeless body. In the dinning rooom!")
            print(f"After some time, you are ready to make your accusation.")
            player.guess = input("> ")
            if player.guess.lower() == "dora":
                print("Congrats, you succesfully identified the murderer!")
                myPlayer.game_over = True
            else:
                print("Sorry, you guess was incorrect. You lose, Better luck next time")
                myPlayer.game_over =  True
    
        
    def get_description(self, x, y):
        """handles all the descriptions of each room"""
        zone_name = self.map_data[x][y]
        if zone_name == 'start':
            return "This is the start, go on and start exploring!"
        elif zone_name == 'f1':
            return "nothing here, keep moving"
        elif zone_name == 'library':
            return "This place is a mess, books everywhere and pages ripped out. There are stands of dark hair."
        elif zone_name == 'f2':
            return "You find Bill running from something. He seems scared but doesn't say anything..."
        elif zone_name == 'kitchen':
            return "It smells nice in here and there is fresh food. I think someone was in here not to long ago."
        elif zone_name == 'f3':
            return "Johnny is standing outside. When he sees you, he runs away."
        elif zone_name == 'f4':
            return "keep moving"
        elif zone_name == "conservatory":
            return "you see Dora standing looking scared. Dora tells you that she saw Gwen with Bill last. Dora is well-built and fit, her hair is a darker color"
        elif zone_name == "f5":
            return "you find nothing keep moving"
        elif zone_name == "study":
            return "you find Miles hiding underneath a desk. He tells you he heard shouting from two girls and a gunshot."
        elif zone_name == "f6":
            return "You find foot prints. They look like they belong to a bigger person"
        elif zone_name == "f7":
            return "you find nothing"
        elif zone_name == "ballroom":
            return "you find Johnny and Bill talking. Johnny has blonde hair and is skinny. Bill has darker hair and is fairly big."
        elif zone_name == "f8":
            return "nothing here"
        elif zone_name == "lounge":
            return "you find no one here, but you find a piece of paper. Bill confronts you. He tells you that he's been with Johnny this entire time."
        elif zone_name == "dinning room":
            return "you find gwen dead on the floor, you see a strands of hair that seem to be a darker hair color."
        
    def print_map(self):
        """prints the map for the player to see in console"""
        for i, row in enumerate(self.map_data):
            print(" ".join("X" if (i, j) == self.current_location else room for j, room in enumerate(row)))

myPlayer = player() #allowing varible myPlayer to access the player class

game_Map = map() #allowing varible game_Map to access the map class

screen_width = 100

def title_screen_selections():
    """handles the title screen and what the player chooses"""
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play' , 'quit', 'help']:
        print("please enter a vaild command")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("quit"):
            print("thanks for playing!")
            break 
            

def title_screen():
    """prints the title screen"""
    print("#######################")
    print("#### Murder Mystery ###")
    print("####### - Play - ######")
    print("####### - Quit - ######")
    title_screen_selections()
    
def prompt():
    """asks the player what they want to do, ex move or look"""
    print("\n" + "================================")
    print("what would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'look', 'exmaine', 'interact', 'travel', 'inventory']
    while action.lower() not in acceptable_actions:
        print("Unknown action, please try again\n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel']:
        print("Enter which direction you would like to go (up/down/right/left):\n")
        game_Map.print_map()
        direction = input("> ").lower()
        if direction in ['up', 'down', 'left', 'right']:
            game_Map.move(direction)
        else:
            print("Unknown action, please try again\n")
    elif action.lower() in ['examine', 'look']:
        x, y = game_Map.current_location
        description = game_Map.get_description(x, y)
        print(description)
    elif action.lower() == 'inventory':
        myPlayer.show_inventory()
    else:
        print("Please enter a vaild command")


def main_game_loop():
    """loops the game"""
    while myPlayer.game_over is False:
        prompt()
        
def setup_game():
    """Sets up the game so the player can start the game"""
    question1 = "What's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
    player_name = input("> ")
    myPlayer.name = player_name
    
    myPlayer.hp = 100
    
    speech1 = "Welcome " + player_name + " To Murder Mystery. Your goal is to catch the killer\n"
    speech2 = "You are playing as a detective and there are 4 suspects. Miles, Dora, Johnny, and Bill. One of them has killed Gwen\n"
    speech3 = "Go on and investigate, " + player_name + "\n"
    speech4 = "Movement Commands: (move - up/down/right/left) Examination Commands: (look)"
    for character in speech1:
        sys.stdout.write(character)  #Makes the text feel real and almost like someone is typing it out
        sys.stdout.flush()
    for character in speech2:
        sys.stdout.write(character)  #Makes the text feel real and almost like someone is typing it out
        sys.stdout.flush()
    for character in speech3:
        sys.stdout.write(character)  #Makes the text feel real and almost like someone is typing it out
        sys.stdout.flush()
    for character in speech4:
        sys.stdout.write(character)  #Makes the text feel real and almost like someone is typing it out
        sys.stdout.flush()
      
        
    main_game_loop() 
    
title_screen()


    



    

    
            







































    