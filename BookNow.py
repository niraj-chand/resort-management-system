[ Tuesday, February 27, 2024 6:20 PM ] ⁨Niraj Chand⁩: #import modules
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

window=Tk()
window.geometry("1400x720")
window.title("BOOK NOW")
window.minsize(width=200,height=200)
Photo= Image.open("bg6.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
icon=ImageTk.PhotoImage(Image.open("Icons/booking.png"))
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

def open_home():
    window.destroy()
    import home

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


#creating button
Button(image=icon1,compound=LEFT,text='HOME',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_home).place(x=3,y= 200,height=65,width=312)
Button(image=icon2,compound=LEFT,text='ROOM AVAILABILITY',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Room_availability).place(x=3,y=263,height=65,width=312)
Button(image=icon3,compound=LEFT,text='BOOK NOW',font=('Times',17,'bold'),fg='#00008b',bg='light blue',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2").place(x=3,y=326,height=65,width=312)
Button(image=icon4,compound=LEFT,text='CUSTOMER RECORD',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Customer_records).place(x=3,y=389,height=65,width=312)
Button(image=icon5,compound=LEFT,text='RECEIPT & TRANSACTION',font=('Times',16,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=receipt_pay).place(x=3,y=452,height=65,width=312)
Button(image=icon6,compound=LEFT,text='CUSTOMER SERVICE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=customer_service).place(x=3,y=515,height=65,width=312)
Button(image=icon7,compound=LEFT,text='PROFILE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Account_profile).place(x=3,y=578,height=65,width=312)
Button(image=icon8,compound=LEFT,text='LOG OUT',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=log_out).place(x=3,y=641,height=65,width=312)
Button(image=icon9,fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_nots).place(x=1430,y=100,height=33,width=33)

Label(window,text='Book Now',bg='white',font=('Arial',18,"bold")).place(x=400,y=160)

try:
    #customer table
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE customers(
        fname text,
        lname text,
        gender text,
        dob int,
        mob text,
        email text,
        address text,
        nationality text,
        ID_type text,
        ID_number int,
        days int,
        Room_Number text
    )""" )
    conn.commit()
    conn.close()
except:
    pass

#reset function
def reset():
    fn.delete(0,END)
    ln.delete(0,END)
    gen.delete(0,END)
    dob.delete(0,END)
    mob.delete(0,END)
    eml.delete(0,END)
    add.delete(0,END)
    nat.delete(0,END)
    cod.delete(0,END)
    rno.delete(0,END)

#teble
def table():
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from room")
    avrooms=c.fetchall()
    for i in avrooms:
        c.execute("""UPDATE room SET
        Room_Status=:st""",{'st': 'Available'})
        conn.commit()
    conn.close()

    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from customers")
    rnum=c.fetchall()
    for i in rnum:
        c.execute("""UPDATE room SET
        Room_Status=:st
        WHERE Room_Number=:rn""",{
            'st': 'Occupied',
            'rn': i[0]
        })
        conn.commit()
    conn.close()

    #table
    table=Frame(window,height=580,width=950,bg='white')
    table.place(x=603,y=198)

    #connection with database
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT * from room")
    lst=c.fetchall()

    #table heading
    lst.insert(0,('S.No.','Room Number','Room Type','Status','Price'))

    #table
    total_rows =len(lst)
    total_columns=len(lst[1])
    for i in range(total_rows):
        #table heading
        if i==0:
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
            #setting colomn width
            if j==0:
                wid=7
            else:
                wid=16
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
    conn.commit()
    conn.close()

#fetch data
def fetch():
    a=cid.get()
    if a=="":
        messagebox.showerror("Fetch","Provide customer ID")
    else:
        try:
            #database connection
            conn=sqlite3.connect('booking.db')
            c=conn.cursor()
            c.execute("SELECT * from customers where oid=:cid",{'cid':a})
            rec=c.fetchall()
            #inserting values into entry boxes
            fn.insert(0,rec[0][0])
            ln.insert(0,rec[0][1])
            gen.insert(0,rec[0][2])
            dob.insert(0,rec[0][3])
[ Tuesday, February 27, 2024 6:20 PM ] ⁨Niraj Chand⁩: mob.insert(0,rec[0][4])
            eml.insert(0,rec[0][5])
            add.insert(0,rec[0][6])
            nat.insert(0,rec[0][7])
            cod.insert(0,rec[0][8])
            rno.insert(0,rec[0][9])
            conn.commit()
            conn.close()
            #update button status to normal
            update1.config(state=NORMAL)
        except:
            messagebox.showerror("Fetch","Incorrect Customer ID")
