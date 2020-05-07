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
        self._color = value

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
        P1 = Board("red", 1, None)
        P2 = Board("purple", 2, None)
        P3 = Board("yellow", 3, None)
        P4 = Board("blue", 4, None)
        P5 = Board("orange", 5, None)
        P6 = Board("green", 6, None)
        P7 = Board("red", 7, None)
        P8 = Board("purple", 8, None)
        P9 = Board("yellow", 9, None)
        P10 = Board("blue", 10, None)
        P11 = Board("orange",11, None)
        P12 = Board("green", 12, None)
        P13 = Board("red", 13, None)
        P14 = Board("purple", 14, None)
        P15 = Board("yellow", 15, None)
        P16 = Board("blue", 16, None)
        P17 = Board("orange",17, None)
        P18 = Board("green", 18, None)
        P19 = Board("red", 19, None)
        P20 = Board("purple", 20, None)
        P21 = Board("pink", 21, "peppermint")
        P22 = Board("yellow", 22, None)
        P23 = Board("blue", 23, None)
        P24 = Board("orange",24, None)
        P25 = Board("green", 25, None)
        P26 = Board("red", 26, None)
        P27 = Board("purple", 27, "x")
        P28= Board("yellow", 28, None)
        P29= Board("blue", 29, None)
        P30 = Board("orange", 30, None)
        P31 = Board("green", 31, None)
        P32 = Board("red", 32, None)
        P33 = Board("pink", 33, "peanut")
        P34 = Board("purple", 34, None)
        P35 = Board("yellow", 35, None)
        P36 = Board("blue", 36, None)
        P37 = Board("orange",37, None)
        P38 = Board("green", 38, None)
        P39 = Board("red", 39, None)
        P40 = Board("purple", 40, None)
        P41 = Board("yellow", 41, None)
        P42 = Board("blue", 42, None)
        P43 = Board("orange", 43, None)
        P44 = Board("green", 44, None)
        P45 = Board("red", 45, None)
        P46 = Board("purple", 46, None)
        P47 = Board("yellow", 47, None)
        P48 = Board("blue", 48, None)
        P49 = Board("orange", 49, None)
        P50 = Board("pink", 50, "lollipop")
        P51 = Board("green", 51, None)
        P52 = Board("red", 52, None)
        P53 = Board("purple", 53, None)
        P54 = Board("yellow", 54, "x")
        P55 = Board("blue", 55, None)
        P56 = Board("orange", 56, None)
        P57 = Board("green", 57, None)
        P58 = Board("red", 58, None)
        P59 = Board("purple", 59, None)
        P60 = Board("yellow", 60, None)
        P61 = Board("blue", 61, None)
        P62 = Board("orange", 62, None)
        P63 = Board("green", 63, None)
        P64 = Board("red", 64, None)
        P65 = Board("purple", 65, None)
        P66 = Board("yellow", 66, None)
        P67 = Board("pink", 67, "icecream")
        P68 = Board("blue", 68, None)
        P69 = Board("orange", 69, None)
        P70 = Board("green", 70, None)
        P71 = Board("red", 71, None)
        P72 = Board("purple", 72, None)
        P73 = Board("yellow", 73, None)
        P74 = Board("blue", 74, None)
        P75 = Board("orange", 75, None)
        P76 = Board("green", 76, None)
        P77 = Board("red", 77, None)
        P78 = Board("purple", 78, None)
        P79 = Board("yellow", 79, None)
        P80 = Board("blue", 80, None)
        P81 = Board("orange", 81, None)
        P82 = Board("green", 82, None)

        Game.BoardListPlacement = [P1.placement, P2.placement, P3.placement, P4.placement, P5.placement, P6.placement, P7.placement, P8.placement, P9.placement, \
                              P10.placement, P11.placement, P12.placement, P13.placement, P14.placement, P15.placement, P16.placement, P17.placement, P18.placement, P19.placement, \
                              P20.placement, P21.placement, P22.placement, P23.placement, P24.placement, P25.placement, P26.placement, P27.placement, P28.placement, P29.placement, \
                              P30.placement, P31.placement, P32.placement, P33.placement, P34.placement, P35.placement, P36.placement, P37.placement, P38.placement, P39.placement, \
                              P40.placement, P41.placement, P42.placement, P43.placement, P44.placement, P45.placement, P46.placement, P47.placement, P48.placement, P49.placement, \
                              P50.placement, P51.placement, P52.placement, P53.placement, P54.placement, P55.placement, P56.placement, P57.placement, P58.placement, P59.placement, \
                              P60.placement, P61.placement, P62.placement, P63.placement, P64.placement, P65.placement, P66.placement, P67.placement, P68.placement, P69.placement, \
                              P70.placement, P71.placement, P72.placement, P73.placement, P74.placement, P75.placement, P76.placement, P77.placement, P78.placement, P79.placement, \
                              P80.placement, P81.placement, P82.placement]

    def setupGUI(self):
        def changepic():
            new_Image = [ "Sred", "Dred", "Spurple", "Dpurple", "Syellow", "Dyellow", "Sblue", "Dblue", "Sorange", "Sorange", "Sgreen", "Dgreen", "Candycane", "Gumdrop", "Icecream", "Lollipop", "Peanut" ]
            color = new_Image[randint(0, len(new_Image) - 1)]
            img = PhotoImage(file = "{}.gif".format(color))
            L4.configure(image = img)
            L4.image = img

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

                for placement in Game.BoardListPlacement:
                    Game.player1.placement +=1
                    if (placement == Game.player1.placement):
                        if (colorClick == P(str(placement)).color):
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ". Player 1 turn over")
                            Game.text.config(state = DISABLED)
                        else:
                            pass
                    else:
                        pass
                        
                        
                # once the player reaches placement of 82, they win the game
                if (Game.player1.placement >= 82):
                    Game.text.config(state = NORMAL)
                    Game.text.delete("1.0", END)
                    Game.text.insert(END, "Congrats player 1! \nYou have won the game! \nPlease exit the window and play again.")
                    Game.text.config(state = DISABLED)
                    break
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
                if (Game.player2.placement >= 82):
                    Game.text.config(state = NORMAL)
                    Game.text.delete("1.0", END)
                    Game.text.insert(END, "Congrats player 2! \nYou have won the game! \nPlease exit the window and play again.")
                    Game.text.config(state = DISABLED)
                    break
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
                    if (Game.player3.placement >= 82):
                        Game.text.config(state = NORMAL)
                        Game.text.delete("1.0", END)
                        Game.text.insert(END, "Congrats player 3! \nYou have won the game! \nPlease exit the window and play again.")
                        Game.text.config(state = DISABLED)
                        break
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
                        if (Game.player4.placement >= 82):
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Congrats player 4! \nYou have won the game! \nPlease exit the window and play again.")
                            Game.text.config(state = DISABLED)
                            break
                        # add one because they completed their turn
                        p4turn +=1
            
            
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
        Game.player1 = Players(Game1.names[0], 0, None)
        Game.player2 = Players(Game1.names[1], 0, None)
        Game.player3 = Players(Game1.names[2], 0, None)
        Game.player4 = Players(Game1.names[3], 0, None)
        Game.text2.config(state = NORMAL)
        Game.text2.delete("1.0", END)
        list1 += ("Player 1 is " + Game.player1.name + "\n") + ("Player 2 is " + Game.player2.name + "\n") + \
                 ("Player 3 is " + Game.player3.name + "\n") + ("Player 4 is " + Game.player4.name)
        Game.text2.insert(END, list1)
        Game.text2.config(state = DISABLED)

                        
    def play(self):
        self.createPlayers()
        self.createBoard()
        


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
