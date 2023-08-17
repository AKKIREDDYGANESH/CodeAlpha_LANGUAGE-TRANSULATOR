from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES 

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src 
    dest1 = dest
    trans  = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s  = comn_sor.get()
    d  = comn_des.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)
    

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='LightGreen')

Lab_txt = Label(root,text="Translator",font=("Time New Romen",40,"bold"),bg='LightGreen') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt.place(x=100,y=40,height=50,width=300) # This refer where the heading will align

frame = Frame(root).pack(side=BOTTOM) # THIS is the frame for text box

Lab_txt = Label(root,text="Source Text",font=("Time New Romen",20,"bold"),fg='Black',bg='LightGreen') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt.place(x=100,y=100,height=20,width=300) # This refer where the heading will align


Sor_txt =Text(frame,font=("Time New Romen",20,"bold"),wrap=WORD)# It give source text to type with font style and size
Sor_txt.place(x=10,y=130,height=150,width=480) # This is text box, This refer where the heading will align

List_text = list(LANGUAGES.values()) # it store all types of language in options

comn_sor = ttk.Combobox(frame,value=List_text) #It is a option box with options
comn_sor.place(x=15,y=300,height=40,width=150) # it refer where did it align
comn_sor.set("English") #It give default value in Combo box

button_change = Button(frame,text="Translate",relief=RAISED,command=data) # IT give button with name translate and give 3D animation
button_change.place(x=180,y=300,height=40,width=150)

comn_des = ttk.Combobox(frame,value=List_text) #It is a option box with options
comn_des.place(x=340,y=300,height=40,width=150) # it refer where did it align
comn_des.set("English") #It give default value in Combo box

Lab_txt = Label(root,text="Destination Text",font=("Time New Romen",20,"bold"),fg='Black',bg='LightGreen') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt.place(x=100,y=360,height=20,width=300) # This refer where the heading will align

dest_txt =Text(frame,font=("Time New Romen",20,"bold"),wrap=WORD)# It give source text to type with font style and size
dest_txt.place(x=10,y=400,height=150,width=480) # This is text box, This refer where the heading will align

root.mainloop()

