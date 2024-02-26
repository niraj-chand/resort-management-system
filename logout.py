from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

window=Tk()
window.geometry("1280x720")
window.title("LOG OUT")
window.minsize(width=200,height=200)
Photo= Image.open("bg6.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
icon=ImageTk.PhotoImage(Image.open("Icons/logout.png"))
window.iconphoto(TRUE,icon)

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
#page connection

def Room_availability():
    window.destroy()
    import Ravailability

def Book_now():
    window.destroy()
    import Booknow

def Customer_records():
    window.destroy()
    import Crecords

def receipt_pay():
    window.destroy()
    import receipt

def customer_service():
    window.destroy()
    import service

def open_home():
    window.destroy()
    import home

def Account_profile():
    window.destroy()
    import account

def open_nots():
    window.destroy()
    import notification

def logout():
    msb=messagebox.askquestion("Logout","Do you really want to log out?")
    if msb=='yes':
        #user statuys
        conn=sqlite3.connect('admins.db')
        c=conn.cursor()
        c.execute("""UPDATE users SET
        status= :off
        WHERE status= :on""",
        {
            'off':False,
            'on':True
        })
        conn.commit()
        conn.close()

        try:
        #destroy window and import logout
            window.destroy()
            import login
        except:
           pass
#home
image1 = PhotoImage(file="Icons/Standard1.png")
label = Label(window, text="STANDARD ROOM", image=image1, compound="center",fg="black",font=("sans serif",19,"bold"))
label.place(x=350,y=230)
image2 = PhotoImage(file="Icons/Deluxe1.png")
label1 = Label(window, text="DELUXE ROOM", image=image2, compound="center",fg="black",font=("sans serif",19,"bold"))
label1.place(x=730,y=230)
image3 = PhotoImage(file="Icons/villa1.png")
label2 = Label(window, text="VILLA", image=image3, compound="center",fg="black",font=("sans serif",19,"bold"))
label2.place(x=1110,y=230)
image4 = PhotoImage(file="Icons/Family1.png")
label3 = Label(window, text="FAMILY ROOM", image=image4, compound="center",fg="black",font=("sans serif",19,"bold"))
label3.place(x=350,y=530)
image5 = PhotoImage(file="Icons/Luxury1.png")
label4 = Label(window, text="LUXURY ROOM", image=image5, compound="center",fg="black",font=("sans serif",19,"bold"))
label4.place(x=730,y=530)

image6 = PhotoImage(file="Icons/Gardenv1.png")
label5 = Label(window, text="GARDEN VIEW ROOM", image=image6, compound="center",fg="black",font=("sans serif",19,"bold"))
label5.place(x=1110,y=530)
#creating button
Button(image=icon1,compound=LEFT,text='HOME',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_home).place(x=3,y= 200,height=65,width=312)
Button(image=icon2,compound=LEFT,text='ROOM AVAILABILITY',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Room_availability).place(x=3,y=263,height=65,width=312)
Button(image=icon3,compound=LEFT,text='BOOK NOW',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Book_now).place(x=3,y=326,height=65,width=312)
Button(image=icon4,compound=LEFT,text='CUSTOMER RECORD',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Customer_records).place(x=3,y=389,height=65,width=312)
Button(image=icon5,compound=LEFT,text='RECEIPT & TRANSACTION',font=('Times',16,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=receipt_pay).place(x=3,y=452,height=65,width=312)
Button(image=icon6,compound=LEFT,text='CUSTOMER SERVICE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=customer_service).place(x=3,y=515,height=65,width=312)
Button(image=icon7,compound=LEFT,text='PROFILE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Account_profile).place(x=3,y=578,height=65,width=312)
Button(image=icon8,compound=LEFT,text='LOG OUT',font=('Times',17,'bold'),fg='#00008b',bg='light blue',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=logout).place(x=3,y=641,height=65,width=312)

Button(image=icon9,fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_nots).place(x=1430,y=100,height=33,width=33)
window.mainloop()
