from Tkinter import *


class Game1(Frame):
    def __inti__(self, parent):
        Frame.__init__(self, parent)

    def setupGUI(self):
        Game1.names = []
        
        L1 = Label(self.master, text = "Player 1:")
        L1.place(height = 50, width = 50, x = 0, y = 0)

        Game1.E1 = Entry(self.master, bg = "white")
        Game1.E1.bind("<Return>", self.pickname1)
        Game1.E1.place(height = 50, width = 100, x = 50, y = 0)

        L2 = Label(self.master, text = "Player 2:")
        L2.place(height = 50, width = 50, x = 0, y = 50)

        Game1.E2 = Entry(self.master, bg = "white")
        Game1.E2.bind("<Return>", self.pickname2)
        Game1.E2.place(height = 50, width = 100, x = 50, y = 50)

        L3 = Label(self.master, text = "Player 3:")
        L3.place(height = 50, width = 50, x = 0, y = 100)

        Game1.E3 = Entry(self.master, bg = "white")
        Game1.E3.bind("<Return>", self.pickname3)
        Game1.E3.place(height = 50, width = 100, x = 50, y = 100)

        L4 = Label(self.master, text = "Player 4:")
        L4.place(height = 50, width = 50, x = 0, y = 150)

        Game1.E4 = Entry(self.master, bg = "white")
        Game1.E4.bind("<Return>", self.pickname4)
        Game1.E4.place(height = 50, width = 100, x = 50, y = 150)

    def pickname1(self, event):
        Game1.names.append(str(Game1.E1.get()))
        Game1.E1.config(state = "disabled")
        print Game1.names[0]
        
    def pickname2(self, event):
        Game1.names.append(str(Game1.E2.get()))
        Game1.E2.config(state = "disabled")
        print Game1.names[1]

    def pickname3(self, event):
        Game1.names.append(str(Game1.E3.get()))
        Game1.E3.config(state = "disabled")
        print Game1.names[2]
        
    def pickname4(self, event):
        Game1.names.append(str(Game1.E4.get()))
        Game1.E4.config(state = "disabled")
        print Game1.names[3]




Height = 200
Width = 200

window = Tk()
window.geometry("{}x{}".format(Width, Height))
window.configure(bg = "white")
window.title("Pick Names")
w = Game1(window)
w.setupGUI()

window.mainloop()
