from Tkinter import *


class Game(Frame):
    def __inti__(self, parent):
        Frame.__init__(self, parent)

    def setupGUI(self):
        Game.names = []
        
        L1 = Label(self.master, text = "Player 1:")
        L1.place(height = 50, width = 50, x = 0, y = 0)

        Game.E1 = Entry(self.master, bg = "white")
        Game.E1.bind("<Return>", self.pickname1)
        Game.E1.place(height = 50, width = 100, x = 50, y = 0)

        L2 = Label(self.master, text = "Player 2:")
        L2.place(height = 50, width = 50, x = 0, y = 50)

        Game.E2 = Entry(self.master, bg = "white")
        Game.E2.bind("<Return>", self.pickname2)
        Game.E2.place(height = 50, width = 100, x = 50, y = 50)

        L3 = Label(self.master, text = "Player 3:")
        L3.place(height = 50, width = 50, x = 0, y = 100)

        Game.E3 = Entry(self.master, bg = "white")
        Game.E3.bind("<Return>", self.pickname3)
        Game.E3.place(height = 50, width = 100, x = 50, y = 100)

        L4 = Label(self.master, text = "Player 4:")
        L4.place(height = 50, width = 50, x = 0, y = 150)

        Game.E4 = Entry(self.master, bg = "white")
        Game.E4.bind("<Return>", self.pickname4)
        Game.E4.place(height = 50, width = 100, x = 50, y = 150)

    def pickname1(self, event):
        Game.names.append(str(Game.E1.get()))
        Game.E1.config(state = "disabled")
        print Game.names[0]
        
    def pickname2(self, event):
        Game.names.append(str(Game.E2.get()))
        Game.E2.config(state = "disabled")
        print Game.names[1]

    def pickname3(self, event):
        Game.names.append(str(Game.E3.get()))
        Game.E3.config(state = "disabled")
        print Game.names[2]
        
    def pickname4(self, event):
        Game.names.append(str(Game.E4.get()))
        Game.E4.config(state = "disabled")
        print Game.names[3]


list_of_names =  Game.names


Height = 200
Width = 200

window = Tk()
window.geometry("{}x{}".format(Width, Height))
window.configure(bg = "white")
window.title("Pick Names")
w = Game(window)
w.setupGUI()
list_of_names =  Game.names

window.mainloop()
