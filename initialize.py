from tkinter import *
root = Tk()
root.title("bro code")
root.geometry("420x420")

icon = PhotoImage(file="Screenshot (3).png")
root.iconphoto(True,icon)
root.config(background="black")
label = Label(root,text="HOSPITAL MANAGEMENT SYSTEM",
              font=("Arial",20,"bold"),
              fg="white",
              bg="black",
              )
label.pack()
root.mainloop()