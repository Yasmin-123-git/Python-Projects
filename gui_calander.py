from tkinter import *
import calendar
def Calendar_See():
    pass
if __name__ == '--main--':
    root = Tk()
    root.config(background="yellow")
    root.title("GUI Calendar")
    root.geometry("280x170")
    name=Label(root,text="Calendar",bg="light pink",font=("Arial",20,'bold'))
    name.grid(row=1,column=1)
    year=Label(root,text="Enter the year",bg="light blue",font=("Arial",15,"bold"))
    year.grid(row=2,column=1)
    year_entry = Entry(root, font=("Arial",15,"bold"))
    
    root.mainloop()
    
    
    