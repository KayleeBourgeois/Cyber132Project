###########################################################################################
# Name: Nikolas Morgan
# Date: 4/8/2020
# Description: 
###########################################################################################

###########################################################################################
from Tkinter import *
import tkMessageBox

# the blueprint for a room

class Room(object):
        # the constructor
        def __init__(self, name, image):
                # rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
                # rooms also have an image (the name of a file)
                # items (e.g., table), item descriptions (for each item), and grabbables (things that can
                # be taken into inventory)
                self.name = name
                self.image = image
                self.exits = {}
                self.items = {}
                self.grabbables = [] 

        # getters and setters for the instance variables
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value

        @property
        def image(self):
                return self._image

        @image.setter
        def image(self, value):
                self._image = value

        @property
        def exits(self):
                return self._exits

        @exits.setter
        def exits(self, value):
                self._exits = value


        @property
        def items(self):
                return self._items

        @items.setter
        def items(self, value):
                self._items = value


        @property
        def grabbables(self):
                return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
                self._grabbables = value

        

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
                # append the exit and room to the appropriate lists
                self._exits[exit] = room

                
                
        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
                # append the item and description to the appropriate lists
                self._items[item] = desc


                
        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
                # append the item to the list
                self._grabbables.append(item)
                


        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
                # remove the item from the list
                self.grabbables.remove(item)


        # returns a string description of the room
        def __str__(self):
                # first, the room name
                s = "You are in {}.\n".format(self.name)

                # next, the items in the room
                s += "You see: "
                for item in self.items.keys():
                        s += item + " "
                s += "\n"

                # list of grabbables in the room
                s += "You can grab: "
                for grabbable in self.grabbables:
                        s += grabbable + " "
                s += "\n"

                # next, the exits from the room
                s += "Exits: "
                for exit in self.exits.keys():
                        s += exit + " "

                return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
        # the constructor
        def __init__(self, parent):
                # call the constructor in the superclass
                Frame.__init__(self, parent)

        # Create the rooms (move function)
        def createRooms(self):
	# r1, r2, r3, r4, are the four rooms in the first floor, Give he image in the directory
                global currentRoom
                global r2
                global r3
                global r6
                # floor one
                r1 = Room("Room 1", "R1.gif")
                r2 = Room("Room 2", "R2.gif")
                r3 = Room("Room 3", "R3.gif")
                r4 = Room("Room 4", "R4.gif")

                # floor two
                r5 = Room("Room 5", "R5.gif")
                r6 = Room("Room 6", "R6.gif")
                r7 = Room("Room 7", "R7.gif")
                r8 = Room("Room 8", "R8.gif")

                # add exits to room 1
                r1.addExit("east", r2)
                r1.addExit("south", r3)

                # add grabbables to room 1
                r1.addGrabbable("key")

                # add items to room 1
                r1.addItem("chair", "It is a wooded chair")
                r1.addItem("table", "It is a plastic table with the wrapping still on it")

                # add exits to room 2
                r2.addExit("west", r1)
                r2.addExit("south", r4)

                # add items to room 2
                r2.addItem("rug", "It is a bear rug")
                r2.addItem("fireplace", "It is hot with blue flames!!")

                # add exits to room 3
                r3.addExit("east", r4)
                r3.addExit("north", r1)
                r3.addExit("south", None)

                # add grabbables to room 3
                r3.addGrabbable("book")

                # add items to room 3
                r3.addItem("bookshelves", "There are books on them")
                r3.addItem("statue", "It is basic")
                r3.addItem("desk", "The statue is resting on the des, so is the book")
        
                # add exits to room 4
                r4.addExit("west", r3)
                r4.addExit("north", r2)

                # add grabbables to room 4
                r4.addGrabbable("6-pack")

                # add items to room 4
                r4.addItem("brew_rig", "Shome beer is being brewed on it")


                # add exits to room 5
                r5.addExit("east", r6)
                r5.addExit("south", r7)

                # add grabbables to room 5
                r5.addGrabbable("severed hand")

                # add items to room 5
                r5.addItem("bed", "The bed looks really comfy")
                r5.addItem("nightstand", "There is a leg missing and smells interesting")

                # add exits to room 6
                r6.addExit("west", r5)
                r6.addExit("north", r2)

                # add grabbables to room 6
                r6.addGrabbable("mouse")
                r6.addGrabbable("cheeseballs")

                # add items to room 6
                r6.addItem("stove", "Someone left the gas on")
                r6.addItem("refrigerator", "the light inside does not work")

                # add exits to room 7
                r7.addExit("east", r8)
                r7.addExit("north", r5)

                # add grabbables to room 7
                r7.addGrabbable("glasses")

                # add items to room 7
                r7.addItem("mirror", "The glass is foggy with moisture")
                r7.addItem("Sink", "There is a constant drip of water")
                r7.addItem("towel", "It's still moist")

                # add exits to room 8
                r8.addExit("west", r7)
                r8.addExit("east", None)

                # add grabbables to room 8
                r8.addGrabbable("rope")

                # add items to room 8
                r8.addItem("boxes", "The boxes seem empty")

                Game.currentRoom = r1
                # initalize the player's inventory
                Game.inventory = []


        # sets up the GUI
        def setupGUI(self):
                # organize the GUI
                self.pack(fill=BOTH, expand=1)

                # setup the player input at the bottom of the GUI
                # the widget is a TKinter Entry
                # set its background to white and bind the return key to the
                # function process in the class
                # push it to th ebottom of the GUI and let it fill
                # horizontally
                # give it focus so the player doesn't have to click on it
                Game.player_input = Entry(self, bg = "white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side = BOTTOM, fill = X)
                Game.player_input.focus()

                # setup the image to the left of the GUI
                # the widget is a TKinter Label
                # don't let the image control the widget's size
                img = None
                Game.image = Label(self, width = WIDTH / 2, image = img)
                Game.image.image = img
                Game.image.pack(side = LEFT, fill = Y)
                Game.image.pack_propagate(False)

                # setup the test to the right of the GUI
                # first, the frame in which the text will be placed
                text_frame = Frame(self, width = WIDTH / 2)
                # the widget is a Tkinter Text
                # disable it by default
                # don't let the widget control the Frame's size
                Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
                Game.text.pack(fill = Y, expand = 1)
                text_frame.pack(side = RIGHT, fill = Y)
                text_frame.pack_propagate(False)

                
                

        # set the current room image
        def setRoomImage(self):
                if (Game.currentRoom == None):
                        # of dead, set the skull image
                        Game.img = PhotoImage(file = "skull.gif")
                else:
                        # otherwise grab the image for teh current room
                        Game.img = PhotoImage(file = Game.currentRoom.image)

                # display the image on the left of the GUI
                Game.image.config(image = Game.img)
                Game.image.image = Game.image

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                # enable the text widget, clear it, set it, and disabled it
                Game.text.config(state = NORMAL)
                Game.text.delete("1.0", END)
                if (Game.currentRoom == None):
                        # if dead, let the player know
                        Game.text.insert(END, "You are dead.\nThe only thing you can do now is quit.\n")
                else:
                        # otherwise, display the appropriate status
                        Game.text.insert(END, str(Game.currentRoom) +\
                                        "\nYou are carrying: " + str(Game.inventory) +\
                                        "\n\n" + status)
                Game.text.config(state = DISABLED)

        # play the game
        def play(self):
                # add the rooms to the game
                self.createRooms()
                # configure the GUI
                self.setupGUI()
                # set the current room
                self.setRoomImage()
                # set the current status
                self.setStatus("")

        # processes the player's input
        def process(self, event):               
                # grab the player's input from the input at the bottom of
                # the GUI
                action = Game.player_input.get()
                # set the user's input to lowercase to make it easier to
                # compare the verb and noun to known values
                action = action.lower()
                # set a default response
                response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."
                # exit the game if the player wants to leave (supports quit, exit, and bye)
                if (action == "quit" or action == "exit" or action == "bye"\
                    or action == "sionara!"):
                        exit(0)

                # if the player is dead if goes/went south from room 4/other
                if (Game.currentRoom == None):
                        # clear the player's input
                        Game.player_input.delete(0, END)
                        return
                # split the user input into words (words are seperated by spaces)
                # and stores the words in a list
                words = action.split()

                # the game only understands two word imputs
                if (len(words) == 2):
                        # isolate the verb and noun
                        verb = words[0]
                        noun = words[1]

                        # the verb is go
                        if (verb == "go"):
                                # set a default response
                                response = "Invalid exit."

                                # check for valid exits in the current room
                                if (noun in Game.currentRoom.exits):
                                        # if one  is found, chage the current room to
                                        # the one tha tis associated with the
                                        # specific exit
                                        Game.currentRoom = Game.currentRoom.exits[noun]
                                        # set the response (success)
                                        response = "Room changed."
                        # the verb is look
                        elif (verb == "look"):
                                # set a default response
                                response = "I don't see that item."

                                # check for valid items in the current room
                                if (noun in Game.currentRoom.items):
                                        # if one is found, set the response to the
                                        # items description
                                        response = Game.currentRoom.items[noun]
                        # the verb is take
                        elif (verb == "take" or verb == "grab"):
                                # set a default response
                                response = "I don't see that item."

                                # check for valid grabbable items in the current room
                                for grabbable in Game.currentRoom.grabbables:
                                        # a valid grabbable is found
                                        if (noun == grabbable):
                                                # add the grabbale item to the player's inventory
                                                Game.inventory.append(grabbable)
                                                # remove the grabbable from the room
                                                Game.currentRoom.delGrabbable(grabbable)
                                                # set the response (success)
                                                response = "Item grabbed."
                                                # no need to ceck any more grabbable items
                                                break
                # display the response on the right of the GUI
                # display the room's image on th eleft of the GUI
                # clear the player's input
                                # set win equal to something to make it valid
                win = 0
                
                # set checkKey to false, then check for the key in the inventory, if there, make true
                checkKey = False
                if 'key' in Game.inventory:
                        checkKey = True
                        
                # set checkBook to false, then check for the book in the inventory, if there, make true
                checkBook = False
                if 'book' in Game.inventory:
                        checkBook = True
                        
                # set checkGlasses to false, then check for the glasses in the inventory, if there, make true
                checkGlasses = False
                if 'glasses' in Game.inventory:
                        checkGlasses = True

                # if beer is in the inventory, print statement and give death
                if '6-pack' in Game.inventory:
                        Game.text.insert( END,"You drink the 6-pack and are now drunk. You can no longer look for clues to exit." \
                        "\nYou run out of time and die alone in the house.")
                        Game.currentRoom = None
                
                # if you are in r2 and you have the key, add the exit to the north to go upstairs to r6
                if(Game.currentRoom == r2) and (checkKey == True):
                        r2.addExit("north", r6)
                        Game.inventory.remove("key")
                        
                # if you are in r2 and you don't have the key, give instructions
                if(Game.currentRoom == r2) and (checkKey == False) and (response == "Invalid exit"):
                        print "Key needed to go upstairs "
                        
                # if in r3, holding book and glasses, add exit south, set room to win
                if(Game.currentRoom == r3) and (checkBook == True) and (checkGlasses == True):
                        r3.addExit("south", win)
                        print "Now I can read the code to open the front door."
                        
                # if in r3, holding book but not glasses, give instructions
                if(Game.currentRoom == r3) and (checkBook == True) and (checkGlasses == False):
                        print "I cannot read the code. Maybe something upstairs can help."
                        
                # if exiting south from r3, print win
                if(Game.currentRoom == win):
                        print "You win!!!!!!!!!!!!!!!!"
                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)


                
###########################################################################################


        


# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

tkMessageBox.showinfo(title="Greetings", message="Somewhere in the house,\
                                                \nthere is a code to the \
                                                \nfront door in the office.\
                                                \nUnlock the door and exit\
                                                \nto win the game.")


# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
        

                                

                   
           

           
           
                    
           

           
           
                           


