from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

window=Tk()
window.geometry("1400x720")
window.title("ROOM AVAILABILITY")
window.minsize(width=200,height=200)
Photo= Image.open("bg6.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
icon=ImageTk.PhotoImage(Image.open("Icons/roomstatus.png"))
window.iconphoto(TRUE,icon)
#page connect
def open_home():
    window.destroy()
    import home

def Book_now():
    window.destroy()
    import Booknow

def Customer_records():
    window.destroy()
    import Crecords

def receipt_pay():
    window.destroy()
    import receipt

def Account_profile():
    window.destroy()
    import account

def customer_service():
    window.destroy()
    import service

def log_out():
    window.destroy()
    import logout

def open_nots():
    window.destroy()
    import notification

icon1=ImageTk.PhotoImage(Image.open("Icons/home.png"))
icon2=ImageTk.PhotoImage(Image.open("Icons/roomstatus.png"))
icon3=ImageTk.PhotoImage(Image.open("Icons/booking.png"))
icon4=ImageTk.PhotoImage(Image.open("Icons/customer.png"))
icon5=ImageTk.PhotoImage(Image.open("Icons/checkout.png"))
icon6=ImageTk.PhotoImage(Image.open("Icons/service.png"))
icon7=ImageTk.PhotoImage(Image.open("Icons/profile.png"))
icon8=ImageTk.PhotoImage(Image.open("Icons/logout.png"))
icon9=ImageTk.PhotoImage(Image.open("Icons/notification.png"))

Frame(window,height=518,width=320,bg="#cc00ff").place(x=0,y=195)

#creating button
Button(image=icon1,compound=LEFT,text='HOME',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_home).place(x=3,y= 200,height=65,width=312)
Button(image=icon2,compound=LEFT,text='ROOM AVAILABILITY',font=('Times',17,'bold'),fg='#00008b',bg='light blue',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2").place(x=3,y=263,height=65,width=312)
Button(image=icon3,compound=LEFT,text='BOOK NOW',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Book_now).place(x=3,y=326,height=65,width=312)
Button(image=icon4,compound=LEFT,text='CUSTOMER RECORD',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Customer_records).place(x=3,y=389,height=65,width=312)
Button(image=icon5,compound=LEFT,text='RECEIPT & TRANSACTION',font=('Times',16,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=receipt_pay).place(x=3,y=452,height=65,width=312)
Button(image=icon6,compound=LEFT,text='CUSTOMER SERVICE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=customer_service).place(x=3,y=515,height=65,width=312)
Button(image=icon7,compound=LEFT,text='PROFILE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Account_profile).place(x=3,y=578,height=65,width=312)
Button(image=icon8,compound=LEFT,text='LOG OUT',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=log_out).place(x=3,y=641,height=65,width=312)

Button(image=icon9,fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_nots).place(x=1430,y=100,height=33,width=33)
#room status frame and label
# a=Frame(window,height=48,width=930,bg='white').place(x=350,y=150)

Label(window,text='Room Availability',bg='white',font=('Arial',18,"bold")).place(x=350,y=160)
#Frame for table
table=Frame(window,height=580,width=950,bg='white')
table.place(x=351,y=200)

#fetching data from database
conn=sqlite3.connect('booking.db')
c=conn.cursor()

c.execute("SELECT * from room")
lst=c.fetchall()

#table headings
lst.insert(0,('S.No.','Room Number','Room Type','Status','Price'))
print(lst)

#creating a table
total_rows =len(lst)
total_columns=len(lst[1])

for i in range(total_rows):
    if i==0:
        #table heading
        fontt=('Arial',16,'bold')
        jus=CENTER
        bgc='#cc00ff'
    else:
        #table data
        fontt=('Arial',16)
        jus=LEFT
        state=(lst[i][3])
        if state=="Occupied":
            bgc='yellow'
        else:
            bgc='white'

    for j in range(total_columns):
        #first column
        if j==0:
            wid=6
        else:
            
            wid=17
        e=Entry(
            table,
            width=wid,
            font=fontt,
            justify=jus,
            disabledforeground='black',
            disabledbackground=bgc
        )
        e.grid(row=i,column=j)
        e.insert(0,lst[i][j])
        e.config(state=DISABLED)

#Last column
price=Entry(window,font=('Arial',16,'bold'),justify=CENTER,disabledbackground='#cc00ff',disabledforeground='black')
price.insert(0,"Rate")
price.config(state=DISABLED)
price.place(x=1026,y=200)
room=Entry(window,font=('Arial',15),justify=CENTER,bg='white',disabledbackground='white',disabledforeground='black')
room.insert(0,"Rs.2000/night")
room.config(state=DISABLED)
room.place(x=1026,y=228,height=112,width=244)
cottage=Entry(window,font=('Arial',15),justify=CENTER,bg='white',disabledbackground='white',disabledforeground='black')
cottage.insert(0,"Rs.1750/night")
cottage.config(state=DISABLED)
cottage.place(x=1026,y=340,height=57,width=244)
tent=Entry(window,font=('Arial',15),justify=CENTER,bg='white',disabledbackground='white',disabledforeground='black')
tent.insert(0,"Rs.1500/night")
tent.config(state=DISABLED)
tent.place(x=1026,y=396,height=84,width=244)

window.mainloop()