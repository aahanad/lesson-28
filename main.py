from tkinter import*
from tkinter.filedialog import*
screen=Tk()
screen.title("lists")
#add funtions
def add_item():
    text=user.get()
    list.insert(END,text)
    user.delete(0,END)
#DELETE FUNCTIONS
def delete_item():
    item=list.curselection()
    if item:
        list.delete(item)
# save function
def save_file():
    content=asksaveasfile(defaultextension=".txt")
    if content is not None:
        for item in list.get(0,END):
            print(item.strip(),file=content)
        list.delete(0,END)
#open function
def open_file():
    doc=askopenfile(title="open_file")
    if doc is not None:
        list.delete(0,END)
        text=doc.readlines()
        for item in text:
            list.insert(END,item.strip())
#making boxes
user=Entry(screen)
user.place(x=280,y=130)
save=Button(screen,text="save",fg="white",bg="black",font=("Brush Script Std",10,"bold"),command=save_file)
save.place(x=50,y=200)
delete=Button(screen,text="delete",fg="white",bg="black",font=("Brush Script Std",10,"bold"),command=delete_item)
delete.place(x=600,y=200)
add=Button(screen,text="add",fg="white",bg="black",font=("Brush Script Std",10,"bold"),command=add_item)
add.place(x=325,y=160)
open=Button(screen,text="open",fg="white",bg="black",font=("Brush Script Std",10,"bold"),command=open_file)
open.place(x=325,y=380)
box=Frame(screen)
scroll=Scrollbar(box,orient="vertical")
scroll.pack(side=RIGHT,fill=Y)
list=Listbox(box,width=75,yscrollcommand=scroll.set,fg="black",bg="white",font=("Brush Script Std",8,"bold"))
list.pack(side=LEFT)
scroll.config(command=list.yview)
box.place(x=120,y=200)
#Make an app, where the Listbox is populated with various colors. 
# The user can select one of them and depending upon the color selected the background of the window should change.
#  You should be able to add more colors or remove them from the list.







screen.mainloop()
