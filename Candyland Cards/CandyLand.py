from Tkinter import *
from random import randint
from GetNames import *

# Classes to create the board places
class Board(object):
    def __init__(self, color, placement, special):
        self.color = color
        self.placement = placement
        self.special = None

    # getters and setters
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = color

    @property
    def placement(self):
        return self._placement
    @placement.setter
    def placement(self, value):
        self._placement = value

    @property
    def special(self):
        return self._special
    @special.setter
    def special(self, value):
        self._special = value

class Players(object):
    def __init__(self, name, placement, character):
        self.name = name
        self.placement = placement
        self.character = character

    # getters and setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def placement(self):
        return self._placement
    @placement.setter
    def placement(self, value):
        self._placement = value

    @property
    def character(self):
        return self._character
    @character.setter
    def character(self, value):
        self._character = value
        

##############################################################################################

# Set up the Window
class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createBoard(self):
        r1 = Board("red", 1)
        p1 = Board("purple", 2)
        y1 = Board("yellow", 3)
        b1 = Board("blue", 4)
        o1 = Board("orange", 5)
        g1 = Board("green", 6)
        r2 = Board("red", 7)
        p2 = Board("purple", 8)
        y2 = Board("yellow", 9)
        b2 = Board("blue", 10)
        o2 = Board("orange",11)
        g2 = Board("green", 12)
        r3 = Board("red", 13)
        p3 = Board("purple", 14)
        y3 = Board("yellow", 15)
        b3 = Board("blue", 16)
        o3 = Board("orange",17)
        g3 = Board("green", 18)
        r4 = Board("red", 19)
        p4 = Board("purple", 20)
        P1 = Board("pink", 21, "peppermint")
        y4 = Board("yellow", 22)
        b4 = Board("blue", 23)
        o4 = Board("orange",24)
        g4 = Board("green", 25)
        r5 = Board("red", 26)
        p5 = Board("purple", 27, "x")
        y5 = Board("yellow", 28)
        b5 = Board("blue", 29)
        o5 = Board("orange", 30)
        g5 = Board("green", 31)
        r6 = Board("red", 32)
        P2 = Board("pink", 33, "peanut")
        p6 = Board("purple", 34)
        y6 = Board("yellow", 35)
        b6 = Board("blue", 36)
        o6 = Board("orange",37)
        g6 = Board("green", 38)
        r7 = Board("red", 39)
        p7 = Board("purple", 40)
        y7 = Board("yellow", 41)
        b7 = Board("blue", 42)
        o7 = Board("orange", 43)
        g7 = Board("green", 44)
        r8 = Board("red", 45)
        p8 = Board("purple", 46)
        y8 = Board("yellow", 47)
        b8 = Board("blue", 48)
        o8 = Board("orange", 49)
        P3 = Board("pink", 50, "lollipop")
        g8 = Board("green", 51)
        r9 = Board("red", 52)
        p9 = Board("purple", 53)
        y9 = Board("yellow", 54, "x")
        b9 = Board("blue", 55)
        o9 = Board("orange", 56)
        g9 = Board("green", 57)
        r10 = Board("red", 58)
        p10 = Board("purple", 59)
        y10 = Board("yellow", 60)
        b10 = Board("blue", 61)
        o10 = Board("orange", 62)
        g10 = Board("green", 63)
        r11 = Board("red", 64)
        p11 = Board("purple", 65)
        y11 = Board("yellow", 66)
        P4 = Board("pink", 67, "icecream")
        b11 = Board("blue", 68)
        o11 = Board("orange", 69)
        g11 = Board("green", 70)
        r12 = Board("red", 71)
        p12 = Board("purple", 72)
        y12 = Board("yellow", 73)
        b12 = Board("blue", 74)
        o12 = Board("orange", 75)
        g12 = Board("green", 76)
        r13 = Board("red", 77)
        p13 = Board("purple", 78)
        y13 = Board("yellow", 79)
        b13 = Board("blue", 80)
        o13 = Board("orange", 81)
        g13 = Board("green", 82)

    def setupGUI(self):
        def changepic():
            new_Image = [ "Sred", "Dred", "Spurple", "Dpurple", "Syellow", "Dyellow", "Sblue", "Dblue", "Sorange", "Sorange", "Sgreen", "Dgreen", "Candycane", "Gumdrop", "Icecream", "Lollipop", "Peanut" ]
            color = new_Image[randint(0, len(new_Image) - 1)]
            img = PhotoImage(file = "{}.gif".format(color))
            L4.configure(image = img)
            L4.image = img
            
        # set up the monopoly board image
        img = PhotoImage(file = "board.gif")
        L1 = Label(self.master, image = img)
        L1.image = img
        L1.place( height = 700, width = 700, x = 0 , y = 0)
        L1.pack_propagate(False)
        
        # set up the dice button
        b1 = Button(self.master, text = "Click to pull a card!", command = changepic, bg = "royalblue2", border = 5, relief = "ridge")
        b1.place( height = 700/4, width = 700/2, x = 1050, y = 50)
        b1.pack_propagate(False)

        # set up dice roll number
        img = PhotoImage(file = "start.gif")
        L4 = Label(self.master, image = img)
        L4.place( height = 700/4, width = 700/2 , x = 700, y = 50)
        L4.pack_propagate(False)

        # set up the text for player info
        Game.text = Text(bg = "white", state = DISABLED, borderwidth = 3, relief = "solid")
        Game.text.place( height = 700/2, width = 700/2, x = 700, y = 525/2 + 50)
        Game.text.pack_propagate(False)

        # set up other players info
        Game.text2 = Text(bg = "white", state = DISABLED, borderwidth = 3, relief = "solid")
        Game.text2.place( height = 700/2, width = 700/2, x = 700 + 700/2, y = 525/2 + 50)
        Game.text2.pack_propagate(False)

        # set up label for player info
        L2 = Label(self.master, text = "Info", bg = "royalblue2", borderwidth = 5)
        L2.place( height = 50, width = 700/2, x = 700, y = 525/2)

        # set up label for other player info
        L3 = Label(self.master, text = "Players' Info", bg = "firebrick3", borderwidth = 5)
        L3.place( height = 50, width = 700/2, x = 700 + 700/2, y = 525/2)

        # set up player input box
        Game.E1 = Entry(self.master, bg = "white")
        Game.E1.bind("<Return>", self.createPlayers)
        Game.E1.place( height = 20, width = 700, x = 700, y = 675)
        Game.E1.focus()


    def createPlayers(self):
        list1 = ""
        player1 = Players(Game1.names[0], 0, None)
        player2 = Players(Game1.names[1], 0, None)
        player3 = Players(Game1.names[2], 0, None)
        player4 = Players(Game1.names[3], 0, None)
        Game.text2.config(state = NORMAL)
        Game.text2.delete("1.0", END)
        list1 += ("Player 1 is " + player1.name + "\n") + ("Player 2 is " + player2.name + "\n") + \
                 ("Player 3 is " + player3.name + "\n") + ("Player 4 is " + player4.name)
        Game.text2.insert(END, list1)
        Game.text2.config(state = DISABLED)

    def turns(self):
        # set all turns to 0 at beginning of game
        p1turn = 0
        p2turn = 0
        p3turn = 0
        p4turn = 0
        # while they are all equal (the beginning of a round), it is player 1's turn
        while (p1turn == p2turn) and (p1turn == p3turn) and  (p1turn == p4turn): # and (playerl.placement < 82) and (player2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
            # for now print the statements
            # later, delete this and create a process for it to run
            Game.text.config(state = NORMAL)
            Game.text.delete("1.0", END)
            Game.text.insert(END, "Goodjob")
            Game.text.config(state = DISABLED)
            # once the player reaches placement of 82, they win the game
##            if (player1.placement >= 82):
##                Game.text.config(state = NORMAL)
##                Game.text.delete("1.0", END)
##                Game.text.insert(END, "Congrats player 1! \nYou have won the game! \nPlease exit the window and play again.")
##                Game.text.config(state = DISABLED)
##                break
            # add one because they completed their turn
            p1turn += 1
            
            # while p2 is less than p1 and p2 is equal to p3 and p4, it is player 2's turn
            while ( p1turn > p2turn and p2turn == p3turn and p2turn == p4turn): # and (pl.placement < 82) and (p2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
                # for now print the statements
                # later, delete this and create a process for it to run
                Game.text.config(state = NORMAL)
                Game.text.delete("1.0", END)
                Game.text.insert(END, "heck yeah")
                Game.text.config(state = DISABLED)
                # once the player reaches placement of 82, they win the game
##                if (player2.placement >= 82):
##                    Game.text.config(state = NORMAL)
##                    Game.text.delete("1.0", END)
##                    Game.text.insert(END, "Congrats player 2! \nYou have won the game! \nPlease exit the window and play again.")
##                    Game.text.config(state = DISABLED)
##                    break
                # add one because they completed their turn
                p2turn +=1
                
                # while p3 is less than p1 and p2 and p3 is equal to p4, it is player 3's turn
                while ( p1turn > p3turn and p2turn > p3turn and p3turn == p4turn): # and (pl.placement < 82) and (p2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
                    # for now print the statements
                    # later, delete this and create a process for it to run
                    Game.text.config(state = NORMAL)
                    Game.text.delete("1.0", END)
                    Game.text.insert(END, "Tech yeah")
                    Game.text.config(state = DISABLED)
                    # once the player reaches placement of 82, they win the game
##                    if (player3.placement >= 82):
##                        Game.text.config(state = NORMAL)
##                        Game.text.delete("1.0", END)
##                        Game.text.insert(END, "Congrats player 3! \nYou have won the game! \nPlease exit the window and play again.")
##                        Game.text.config(state = DISABLED)
##                        break
                    # add one because they completed their turn
                    p3turn +=1
                    
                    #while p1 and p2 and p3 are all greater than p4 (final turn of the round), it is player 4's turn
                    # for now, p1 != 3 is set because we do not have positions set for players, this stops the endless loop
                    while (p1turn > p4turn and p2turn > p4turn and p3turn > p4turn) and p1turn != 3: # and (pl.placement < 82) and (p2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
                        # for now print the statements
                        # later, delete this and create a process for it to run
                        Game.text.config(state = NORMAL)
                        Game.text.delete("1.0", END)
                        Game.text.insert(END, "You did it")
                        Game.text.config(state = DISABLED)
                        # once the player reaches placement of 82, they win the game
##                        if (player4.placement >= 82):
##                            Game.text.config(state = NORMAL)
##                            Game.text.delete("1.0", END)
##                            Game.text.insert(END, "Congrats player 4! \nYou have won the game! \nPlease exit the window and play again.")
##                            Game.text.config(state = DISABLED)
##                            break
                        # add one because they completed their turn
                        p4turn +=1

                        
    def play(self):
        self.createPlayers()
        self.turns()
        
        


WIDTH = 1400
HEIGHT = 700

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.configure(bg = "white")
window.title("Monopoly Game")
t = Game(window)
t.setupGUI()
t.play()

# wait for the window to close
window.mainloop()
