from tkinter import *
root = Tk()

#header
root.title("HMS") 
root.geometry("420x420")
icon = PhotoImage(file="header.png")
root.iconphoto(True,icon)
root.config(background="white")

#label
label = Label(root,
              text="HOSPITAL MANAGEMENT SYSTEM",
              font=("Arial",20),
              fg="black",
              bg="white",
              relief=RAISED,
              bd=5,
              padx=20,
              pady=20)

#button
count=0
def click():
    global count
    count+=1
    print(count)

image = PhotoImage(file="like.png")
button = Button(root,
                text="click me!",
                command=click,
                fg="black",
                bg="white",
                image=image,
                compound="left")
button.pack()

#entry box

def submit():
    user_name = entry.get()
    print("hello "+ user_name)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

entry = Entry(root,
              font=("Arial",12),
              show="*")
entry.pack(side="left")
submit_button = Button(root,text="submit",command=submit)
submit_button.pack(side="right")

delete_button = Button(root,text="Delete",command=delete)
delete_button.pack(side="right")

backspace_button = Button(root,text="backspace",command=backspace)
backspace_button.pack(side="right")

#checkbox:

def display():
    if(x.get()):
        print("I agree")
    else:
        print("I dont agree")

x = BooleanVar()

check_box = Checkbutton(root,
                      text="i agree to something",
                      variable=x,
                      onvalue=True,
                      offvalue=False,
                      command=display,
                      padx=20,
                      pady=20,
                      fg="green",
                      bg="black",
                      activebackground="black",
                      activeforeground="green")
check_box.pack()

#radiobutton

def box():
    if(y.get()==0):
        print("you ordered a pizza")
    elif(y.get()==1):
        print("you ordered a burger")
    else:
        print("you ordered a hotdog")
y = IntVar()
food=["pizza","burger","hotdog"]
for index in range(len(food)):
    radio_button = Radiobutton(root,
                               text=food[index],
                               variable=y,
                               value=index,
                               indicatoron=0,
                               width=350,
                               command=box)
    radio_button.pack()
    
#list box
 
 
label.pack()
root.mainloop()