###########################################################################################
# Name: Nikolas Morgan
# Date: 1/6/2020
# Description: 
###########################################################################################

###########################################################################################
# the blueprint for a room
class Room(object):
        # the constructor
        def __init__(self, name):
                # rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
                # items (e.g., table), item descriptions (for each item), and grabbables (things that can
                # be taken into inventory)
                self.name = name
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

###########################################################################################
# creates the rooms
def createRooms():
        # r1, r2, r3, r4, are the four rooms in our mansion
        global currentRoom
        global r2
        global r6
        # floor one
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")

        # floor two
        r5 = Room("Room 5")
        r6 = Room("Room 6")
        r7 = Room("Room 7")
        r8 = Room("Room 8")

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

        # add items to room 6
        r6.addItem("stove", "Someone left the gas on")
        r6.addItem("refrigerator", "the light inside does not work")

        # add exits to room 7
        r7.addExit("east", r8)
        r7.addExit("north", r5)

        # add grabbables to room 7
        r7.addGrabbable("glasses")

        # add items to room 7
        r7.addItem("shower", "The glass is foggy with moisture")
        r7.addItem("Sink", "There is a constant drip of water")
        r7.addItem("towel", "It's still moist")

        # add exits to room 8
        r8.addExit("west", r7)
        r8.addExit("east", None)

        # add grabbables to room 8
        r8.addGrabbable("rope")

        # add items to room 8
        r8.addItem("boxes", "The boxes seem empty")
        r8.addItem("mirror", "It's slightly foggy with age")

        currentRoom = r1

        
# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
        print " " * 17 + "u" * 7
        print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
        print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
        print " " * 9 + "u" + "$" * 21 + "u"
        print " " * 8 + "u" + "$" * 23 + "u"
        print " " * 7 + "u" + "$" * 25 + "u"
        print " " * 7 + "u" + "$" * 25 + "u"
        print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
        print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
        print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
        print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
        print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
        print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
        print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
        print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
        print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
        print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
        print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
        print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
        print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
        print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
        print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
        print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
        print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
        print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
        print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""

def makeMap():
        def map1():
                print "Floor 1"
                print "\n"
                print "\n"
                print " " * 60 + "map " * 5 
                print " " * 60 + "map " + " " * 12 + "map "
                print " " * 60 + "map " + " " * 2 + "stairs " + " " * 3 + "map "
                print " " * 60 + "map " + " " * 12 + "map " 
                print "map " * 16 + "_" * 11 + " " + "map " * 2
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 11 + "living room" + " " * 14 + "map " + " " * 13 + "fire room" + " " * 14 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " * 4 + " " * 12 + "map "* 7 + " " * 12 + "map " * 4
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 14 + "office" + " " * 16 + "map " + " " * 13 + "brewery" + " " * 16 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " * 4 + "_" * 11 + " " + "map " * 14
        def map2():
                print "Floor 2"
                print "\n"
                print "\n"
                print " " * 60 + "map " * 5 
                print " " * 60 + "map " + " " * 12 + "map "
                print " " * 60 + "map " + " " * 2 + "stairs " + " " * 3 + "map "
                print " " * 60 + "map " + " " * 12 + "map " 
                print "map " * 16 + "_" * 11 + " " + "map " * 2
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 14 + "bedroom" + " " * 15 + "map " + " " * 14 + "kitchen" + " " * 15 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " * 4 + " " * 12 + "map "* 14
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 13 + "bathroom" + " " * 15 + "map " + " " * 14 + "closet" + " " * 16 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 76 + "map "
                print "map " + " " * 76 + "  D"
                print "map " + " " * 76 + "  E"
                print "map " + " " * 76 + "  A"
                print "map " + " " * 76 + "  T"
                print "map " + " " * 76 + "  H"
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " + " " * 36 + "map " + " " * 36 + "map "
                print "map " * 21


        map1()
        print "\n"
        map2()
        print "\n"
        print "'______' is a locked door"
        print " DEATH is a window (of opportunity)"
###########################################################################################
# START THE GAME!!!

inventory = []
createRooms()
makeMap()
        
while(True):

        status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

        checkKey = False
        if 'key' in inventory:
                checkKey = True

        if(currentRoom == r2) and (checkKey == True):
                r2.addExit("north", r6)
                
        if(currentRoom == r2) and (checkKey == False):
                print "Key needed to go up stairs"
                
        if(currentRoom == None):
                death()
                break

        print "============================================================================================="
        print status

        # prompt user for input
        action = raw_input("What would you like to do? ")

        action = action.lower()

        if(action == "quit" or action == "exit" or action == "bye"):
           break


        # set a default response
        response = "I don't understand. Try ising verb noun. Valid verbs are" \
                   " go, look, and take."

        # split user input into words
        words = action.split()

        if(len(words) == 2):
                verb = words[0]
                noun = words[1]

                if(verb == "go"):
                        # default response
                        response = "Invalid exit"

                        #check for valid exits in the room
                        if(noun in currentRoom.exits):
                                # if one is found, change the current room
                                currentRoom = currentRoom.exits[noun]
                                # set the response to success
                                response = "Room Changed"

                        
                                
                elif(verb == "look"):
                        # default response
                        response = "I do not see that item"
                        
                        #check for valid items in the room
                        if(noun in currentRoom.items):
                                # if one is found, set the response
                                response = currentRoom.items[noun]


                elif(verb == "take"):
                        #default response
                        response = "I do not see that item"

                        for grabbable in currentRoom.grabbables:
                                if(noun == grabbable):
                                        # add to inventory
                                        inventory.append(grabbable)

                                        # remove the item from the room
                                        currentRoom.delGrabbable(grabbable)

                                        # set the response
                                        response = "Item grabbed"

                                        # no need to check more grabbables
                                        break

        # display the response
        print "\n{}".format(response)

                                

                   
           

           
           
                    
           

           
           
                           


