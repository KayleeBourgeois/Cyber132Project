from Tkinter import *
from random import randint
from GetNames import *

play = False

# Things to do
## Turns with multiplayer
## player info on the right
## black spots for skip player turn

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

    # create the board pieces
    # give them a color, placement, and special value
    def createBoard(self):
        Game.P1 = Board("red", 1, None)
        P2 = Board("purple", 2, None)
        P3 = Board("yellow", 3, None)
        P4 = Board("blue", 4, None)
        P5 = Board("orange", 5, None)
        P6 = Board("green", 6, None)
        P7 = Board("red", 7, None)
        P8 = Board("purple", 8, None)
        P9 = Board("pink", 9, "berry")
        P10 = Board("yellow", 10, None)
        P11 = Board("blue",11, None)
        P12 = Board("orange", 12, None)
        P13 = Board("green", 13, None)
        P14 = Board("red", 14, None)
        P15 = Board("purple", 15, None)
        P16 = Board("yellow", 16, None)
        P17 = Board("blue",17, None)
        P18 = Board("pink", 18, "candycane")
        P19 = Board("orange", 19, None)
        P20 = Board("green", 20, None)
        P21 = Board("red", 21, None)
        P22 = Board("purple", 22, None)
        P23 = Board("yellow", 23, None)
        P24 = Board("blue",24, None)
        P25 = Board("orange", 25, None)
        P26 = Board("green", 26, None)
        P27 = Board("red", 27, None)
        P28= Board("purple", 28, None)
        P29= Board("yellow", 29, None)
        P30 = Board("blue", 30, None)
        P31 = Board("orange", 31, None)
        P32 = Board("green", 32, None)
        P33 = Board("red", 33, None)
        P34 = Board("purple", 34, None)
        P35 = Board("yellow", 35, None)
        P36 = Board("blue", 36, None)
        P37 = Board("orange",37, None)
        P38 = Board("green", 38, None)
        P39 = Board("red", 39, None)
        P40 = Board("purple", 40, None)
        P41 = Board("yellow", 41, None)
        P42 = Board("blue", 42, None)
        P43 = Board("pink", 43, "gumdrop")
        P44 = Board("orange", 44, None)
        P45 = Board("green", 45, None)
        P46 = Board("red", 46, None)
        P47 = Board("purple", 47, None)
        P48 = Board("yellow", 48, "x")
        P49 = Board("blue", 49, None)
        P50 = Board("orange", 50, None)
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
        P67 = Board("blue", 67, None)
        P68 = Board("orange", 68, None)
        P69 = Board("green", 69, None)
        P70 = Board("red", 70, None)
        P71 = Board("purple", 71, None)
        P72 = Board("yellow", 72, None)
        P73 = Board("blue", 73, None)
        P74 = Board("red", 74, None)
        P75 = Board("pink", 75, "peanut")
        P76 = Board("green", 76, None)
        P77 = Board("red", 77, None)
        P78 = Board("purple", 78, None)
        P79 = Board("yellow", 79, None)
        P80 = Board("blue", 80, None)
        P81 = Board("orange", 81, None)
        P82 = Board("green", 82, None)
        P83 = Board("red", 83, None)
        P84 = Board("purple", 84, None)
        P85 = Board("yellow", 85, None)
        P86 = Board("blue", 86, "x")
        P87 = Board("orange", 87, None)
        P88 = Board("green", 88, None)
        P89 = Board("red", 89, None)
        P90 = Board("purple", 90, None)
        P91 = Board("yellow", 91, None)
        P92 = Board("blue", 92, None)
        P93 = Board("orange", 93, None)
        P94 = Board("green", 94, None)
        P95 = Board("red", 95, None)
        P96 = Board("pink", 96, "lollipop")
        P97 = Board("purple", 97, None)
        P98 = Board("yellow", 98, None)
        P99 = Board("blue", 99, None)
        P100 = Board("orange", 100, None)
        P101 = Board("green", 101, None)
        P102 = Board("red", 102, None)
        P103 = Board("purple", 103, None)
        P104 = Board("pink", 104, "snowflake")
        P105 = Board("yellow", 105, None)
        P106 = Board("blue", 106, None)
        P107 = Board("orange", 107, None)
        P108 = Board("green", 108, None)
        P109 = Board("red", 109, None)
        P110 = Board("purple", 110, None)
        P111 = Board("yellow", 111, None)
        P112 = Board("blue", 112, None)
        P113 = Board("orange", 113, None)
        P114 = Board("green", 114, None)
        P115 = Board("red", 115, None)
        P116 = Board("purple", 116, None)
        P117 = Board("yellow", 117, None)
        P118 = Board("blue", 118, None)
        P119 = Board("orange", 119, None)
        P120 = Board("green", 120, None)
        P121 = Board("red", 121, "x")
        P122 = Board("purple", 122, None)
        P123 = Board("yellow", 123, None)
        P124 = Board("blue", 124, None)
        P125 = Board("orange", 125, None)
        P126 = Board("green", 126, None)
        P127 = Board("red", 127, None)
        P128 = Board("purple", 128, None)
        P129 = Board("yellow", 129, None)
        P130 = Board("blue", 130, None)
        P131 = Board("orange", 131, None)
        P132 = Board("green", 132, None)
        P133 = Board("red", 133, None)
        P134 = Board("purple", 134, None)
        P135 = Board("yellow", 135, None)
        P136 = Board("blue", 136, None)
        P137 = Board("orange", 137, None)
        P138 = Board("green", 138, None)
        P139 = Board("red", 139, None)

        # create a list of the every board piece's placement to use later in game play
        Game.BoardListPlacement = [Game.P1.placement, P2.placement, P3.placement, P4.placement, P5.placement, P6.placement, P7.placement, P8.placement, P9.placement, \
                              P10.placement, P11.placement, P12.placement, P13.placement, P14.placement, P15.placement, P16.placement, P17.placement, P18.placement, P19.placement, \
                              P20.placement, P21.placement, P22.placement, P23.placement, P24.placement, P25.placement, P26.placement, P27.placement, P28.placement, P29.placement, \
                              P30.placement, P31.placement, P32.placement, P33.placement, P34.placement, P35.placement, P36.placement, P37.placement, P38.placement, P39.placement, \
                              P40.placement, P41.placement, P42.placement, P43.placement, P44.placement, P45.placement, P46.placement, P47.placement, P48.placement, P49.placement, \
                              P50.placement, P51.placement, P52.placement, P53.placement, P54.placement, P55.placement, P56.placement, P57.placement, P58.placement, P59.placement, \
                              P60.placement, P61.placement, P62.placement, P63.placement, P64.placement, P65.placement, P66.placement, P67.placement, P68.placement, P69.placement, \
                              P70.placement, P71.placement, P72.placement, P73.placement, P74.placement, P75.placement, P76.placement, P77.placement, P78.placement, P79.placement, \
                              P80.placement, P81.placement, P82.placement, P83.placement, P84.placement, P85.placement, P86.placement, P87.placement, P88.placement, P89.placement, \
                              P90.placement, P91.placement, P92.placement, P93.placement, P94.placement, P95.placement, P96.placement, P97.placement, P98.placement, P99.placement, \
                              P100.placement, P101.placement, P102.placement, P103.placement, P104.placement, P105.placement, P106.placement, P107.placement, P108.placement, P109.placement, \
                              P110.placement, P111.placement, P112.placement, P113.placement, P114.placement, P115.placement, P116.placement, P117.placement, P118.placement, P119.placement, \
                              P120.placement, P121.placement, P122.placement, P123.placement, P124.placement, P125.placement, P126.placement, P127.placement, P128.placement, P129.placement, \
                              P130.placement, P131.placement, P132.placement, P133.placement, P134.placement, P135.placement, P136.placement, P137.placement, P138.placement, P139.placement ]

        # create a list of every board piece's color to use later in game play
        Game.BoardListColor = [Game.P1.color, P2.color, P3.color, P4.color, P5.color, P6.color, P7.color, P8.color, P9.color, \
                              P10.color, P11.color, P12.color, P13.color, P14.color, P15.color, P16.color, P17.color, P18.color, P19.color, \
                              P20.color, P21.color, P22.color, P23.color, P24.color, P25.color, P26.color, P27.color, P28.color, P29.color, \
                              P30.color, P31.color, P32.color, P33.color, P34.color, P35.color, P36.color, P37.color, P38.color, P39.color, \
                              P40.color, P41.color, P42.color, P43.color, P44.color, P45.color, P46.color, P47.color, P48.color, P49.color, \
                              P50.color, P51.color, P52.color, P53.color, P54.color, P55.color, P56.color, P57.color, P58.color, P59.color, \
                              P60.color, P61.color, P62.color, P63.color, P64.color, P65.color, P66.color, P67.color, P68.color, P69.color, \
                              P70.color, P71.color, P72.color, P73.color, P74.color, P75.color, P76.color, P77.color, P78.color, P79.color, \
                              P80.color, P81.color, P82.color, P83.color, P84.color, P85.color, P86.color, P87.color, P88.color, P89.color, \
                              P90.color, P91.color, P92.color, P93.color, P94.color, P95.color, P96.color, P97.color, P98.color, P99.color, \
                              P100.color, P101.color, P102.color, P103.color, P104.color, P105.color, P106.color, P107.color, P108.color, P109.color, \
                              P110.color, P111.color, P112.color, P113.color, P114.color, P115.color, P116.color, P117.color, P118.color, P119.color, \
                              P120.color, P121.color, P122.color, P123.color, P124.color, P125.color, P126.color, P127.color, P128.color, P129.color, \
                              P130.color, P131.color, P132.color, P133.color, P134.color, P135.color, P136.color, P137.color, P138.color, P139.color ]        

    def setupGUI(self):
        def changepic():
            play = True
            # a list of the image names
            new_Image = [ "Sred", "Sred", "Sred", "Dred", "Dred", "Spurple", "Spurple", "SPurple", "Dpurple", "Dpurple", "Syellow", "Syellow", "Syellow", "Dyellow", "Dyellow", "Sblue",\
                          "Sblue", "Sblue", "Dblue", "Dblue", "Sorange", "Sorange", "Sorange", "Dorange", "Dorange", "Sgreen", "Sgreen", "Sgreen", "Dgreen", "Dgreen", \
                          "Candycane", "Gumdrop", "Lollipop", "Peanut", "Berry", "Snowflake" ]
            global color
            # pick a random image/color value
            color = new_Image[randint(0, len(new_Image) - 1)]
            # set the color picked to the image
            img = PhotoImage(file = "{}.gif".format(color))
            # set the new image for the card picked
            L4.configure(image = img)
            L4.image = img
            # set the global colorclick to use later in game play
            global colorClick
            # set both red cards to a color of red
            if (color == "Sred" or color == "Dred"):
                colorClick = "red"
            # set both purple cards to a color of purple
            if (color == "Spurple" or color == "Dpurple"):
                colorClick = "purple"
            # set both yellow cards to a color of yellow
            if (color == "Syellow" or color == "Dyellow"):
                colorClick = "yellow"
            # set both blue cards to a color of blue
            if (color == "Sblue" or color == "Dblue"):
                colorClick = "blue"
            # set both orange cards to a color of orange
            if (color == "Sorange" or color == "Dorange"):
                colorClick = "orange"
            # set both green cards to a color of green
            if (color == "Sgreen" or color == "Dgreen"):
                colorClick = "green"
            # set caps Berry to berry colorClick
            if (color == "Berry"):
                colorClick = "berry"
            # set caps Candycane to candycane colorClick
            if (color == "Candycane"):
                colorClick = "candycane"
            # set caps Gumdrop to gumdrop colorClick
            if (color == "Gumdrop"):
                colorClick = "gumdrop"
            # set caps Peanut to peanut colorClick
            if (color == "Peanut"):
                colorClick = "peanut"
            # set caps Lollipop to lollipop colorClick
            if (color == "Lollipop"):
                colorClick = "lollipop"
            # set caps Snowflake to snowflake colorClick
            if (color == "Snowflake"):
                colorClick = "snowflake"
            
            # set all turns to 0 at beginning of game
            p1turn = 0
            p2turn = 0
            p3turn = 0
            p4turn = 0
            # while they are all equal (the beginning of a round), it is player 1's turn
            while (p1turn == p2turn) and (p1turn == p3turn) and  (p1turn == p4turn) and (play == True): # and (playerl.placement < 82) and (player2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
##              # for now print the statements
##              # later, delete this and create a process for it to run
##                Game.text.config(state = NORMAL)
##                Game.text.delete("1.0", END)
##                Game.text.insert(END, "Goodjob")
##                Game.text.config(state = DISABLED)

                # increment the placement until it reaches the desires board space
                for placement in Game.BoardListPlacement:
                    # if the placement of the player and the board match, cont.
                    if (placement - 1 == Game.player1.placement):
                        # if on the berry, move to place 9
                        # print placement
                        if (colorClick == "berry"):
                            Game.player1.placement = 9
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".Player 1's turn over.")
                            Game.text.config(state = DISABLED)
                            break
                        # if on candycane, move to place 18
                        # print placement
                        elif (colorClick == "candycane"):
                            Game.player1.placement = 18
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                            Game.text.config(state = DISABLED)
                            break
                        # if on gumdrop, move to place 43
                        # print placement
                        elif (colorClick == "gumdrop"):
                            Game.player1.placement = 43
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                            Game.text.config(state = DISABLED)
                            break
                        # if on peanut, move to place 75
                        # print placement
                        elif (colorClick == "peanut"):
                            Game.player1.placement = 75
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                            Game.text.config(state = DISABLED)
                            break
                        # if on lollipop, move to place 96
                        # print placement
                        elif (colorClick == "lollipop"):
                            Game.player1.placement = 96
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                            Game.text.config(state = DISABLED)
                            break
                        # if on snowflake, move to place 104
                        # print placement
                        elif (colorClick == "snowflake"):
                            Game.player1.placement = 104
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                            Game.text.config(state = DISABLED)
                            break
                        # if color of card is the same as the place, cont.
                        # print placement
                        elif (colorClick == Game.BoardListColor[placement - 1]):
                            Game.player1.placement += 1
                            Game.text.config(state = NORMAL)
                            Game.text.delete("1.0", END)
                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                            Game.text.config(state = DISABLED)
                            # if a color is double, cont.
                            if ((color == "Dred") or (color == "Dpurple") or (color == "Dyellow") or (color == "Dgreen") or (color == "Dblue") or (color == "Dorange")):
                                # move to the next space so you are not still on the same color
                                Game.player1.placement += 1
                                # run the same loop as before to move to the next occurance of that color
                                for placement in Game.BoardListPlacement:
                                    if (placement - 1 == Game.player1.placement):
                                        if (colorClick == Game.BoardListColor[placement - 1]):
                                            Game.player1.placement += 1
                                            Game.text.config(state = NORMAL)
                                            Game.text.delete("1.0", END)
                                            Game.text.insert(END, "Player 1's placement is " + str(Game.player1.placement) + ".\nPlayer 1's turn over.")
                                            Game.text.config(state = DISABLED)
                                            # break out of both for loops
                                            break
                                            break
                                        # if the colors do not match, move to the next space
                                        else:
                                            Game.player1.placement +=1
                            # break from the for loop
                            break
                        # if the colors do not match, move to the next space
                        else:
                            Game.player1.placement +=1
                        
                        
                # once the player reaches placement of 133, they win the game
                if (Game.player1.placement > 133):
                    Game.text.config(state = NORMAL)
                    Game.text.delete("1.0", END)
                    Game.text.insert(END, "Congrats player 1! \nYou have won the game! \nPlease exit the window and play again.")
                    Game.text.config(state = DISABLED)
                    break
                # add one because they completed their turn
                play = False
                p1turn += 1
            
##            # while p2 is less than p1 and p2 is equal to p3 and p4, it is player 2's turn
##            while ( p1turn > p2turn and p2turn == p3turn and p2turn == p4turn and (play == True)): # and (pl.placement < 82) and (p2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
##                # for now print the statements
##                # later, delete this and create a process for it to run
##                Game.text.config(state = NORMAL)
##                Game.text.delete("1.0", END)
##                Game.text.insert(END, "heck yeah")
##                Game.text.config(state = DISABLED)
##                # once the player reaches placement of 133, they win the game
##                if (Game.player2.placement >= 133):
##                    Game.text.config(state = NORMAL)
##                    Game.text.delete("1.0", END)
##                    Game.text.insert(END, "Congrats player 2! \nYou have won the game! \nPlease exit the window and play again.")
##                    Game.text.config(state = DISABLED)
##                    break
##                # add one because they completed their turn
##                play = False
##                p2turn +=1
##                
##            # while p3 is less than p1 and p2 and p3 is equal to p4, it is player 3's turn
##            while ( p1turn > p3turn and p2turn > p3turn and p3turn == p4turn and (play == True)): # and (pl.placement < 82) and (p2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
##                # for now print the statements
##                # later, delete this and create a process for it to run
##                Game.text.config(state = NORMAL)
##                Game.text.delete("1.0", END)
##                Game.text.insert(END, "Tech yeah")
##                Game.text.config(state = DISABLED)
##                # once the player reaches placement of 133, they win the game
##                if (Game.player3.placement > 133):
##                    Game.text.config(state = NORMAL)
##                    Game.text.delete("1.0", END)
##                    Game.text.insert(END, "Congrats player 3! \nYou have won the game! \nPlease exit the window and play again.")
##                    Game.text.config(state = DISABLED)
##                    break
##                # add one because they completed their turn
##                play = False
##                p3turn +=1
##                    
##            #while p1 and p2 and p3 are all greater than p4 (final turn of the round), it is player 4's turn
##            # for now, p1 != 3 is set because we do not have positions set for players, this stops the endless loop
##            while (p1turn > p4turn and p2turn > p4turn and p3turn > p4turn) and (p1turn != 3) and (play == True): # and (pl.placement < 82) and (p2.placement < 82) and (p3.placement < 82) and (p4.placement < 82)
##                # for now print the statements
##                # later, delete this and create a process for it to run
##                Game.text.config(state = NORMAL)
##                Game.text.delete("1.0", END)
##                Game.text.insert(END, "You did it")
##                Game.text.config(state = DISABLED)
##                # once the player reaches placement of 133, they win the game
##                if (Game.player4.placement > 133):
##                    Game.text.config(state = NORMAL)
##                    Game.text.delete("1.0", END)
##                    Game.text.insert(END, "Congrats player 4! \nYou have won the game! \nPlease exit the window and play again.")
##                    Game.text.config(state = DISABLED)
##                    break
##                # add one because they completed their turn
##                play = False
##                p4turn +=1
            
            
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
        # use other file to ask for user input
        # then set the input to each players name in chronological order
        Game.player1 = Players(Game1.names[0], 0, None)
        Game.player2 = Players(Game1.names[1], 0, None)
        Game.player3 = Players(Game1.names[2], 0, None)
        Game.player4 = Players(Game1.names[3], 0, None)
        # update text on the right side to say players names
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
