from tkinter import *

# Creating a Canvas
root = Tk()
root.geometry("500x500")
root.title("My First GUI")

icon = PhotoImage(file='Logo.png')
root.iconphoto(True,icon)
root.config(background = "#2e2d2d")

root.mainloop()