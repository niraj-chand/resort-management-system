#import modules
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#window
window=Tk()
window.geometry("1400x720")
window.title("CUSTOMER RECORD")
window.minsize(width=200,height=200)
Photo= Image.open("bg6.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
icon=ImageTk.PhotoImage(Image.open("Icons/customer.png"))
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

def open_home():
    window.destroy()
    import home

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
Button(image=icon3,compound=LEFT,text='BOOK NOW',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Book_now).place(x=3,y=326,height=65,width=312)
Button(image=icon4,compound=LEFT,text='CUSTOMER RECORD',font=('Times',17,'bold'),fg='#00008b',bg='light blue',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2").place(x=3,y=389,height=65,width=312)
Button(image=icon5,compound=LEFT,text='RECEIPT & TRANSACTION',font=('Times',16,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=receipt_pay).place(x=3,y=452,height=65,width=312)
Button(image=icon6,compound=LEFT,text='CUSTOMER SERVICE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=customer_service).place(x=3,y=515,height=65,width=312)
Button(image=icon7,compound=LEFT,text='PROFILE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Account_profile).place(x=3,y=578,height=65,width=312)
Button(image=icon8,compound=LEFT,text='LOG OUT',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=log_out).place(x=3,y=641,height=65,width=312)

Button(image=icon9,fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_nots).place(x=1430,y=100,height=33,width=33)

#value of y for search function
space=295

#search function
def srch():
    #get data from dropdown menu and entry
    Frame(window,height=215,width=20,bg='white').place(x=350,y=295)
    term=clicked.get()
    detail=search.get()

    #database connection
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT oid,* from customers")
    det=c.fetchall()

    #Searching algorithm
    i=len(det)-1
    while i>=0:
        #searching for customer id
        if term=="Customer ID":
            try:
                #comparing values
                int(detail)
                if det[i][0]!=int(detail):
                    i=i-1
                    if i==-1:
                        break
                else:
                    Label(window,text="\u2192",bg='white',font=('open sans',13,'bold'),fg='red').place(x=345,y=(space+20*i))
                    break
            except:
                messagebox.showerror("Search","Invalid Customer ID")
                break
        #searching by first name
        elif term=="First Name":
            if det[i][1]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u2192",bg='white',font=('open sans',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                i=i-1
                if i==-1:
                    break
        #searching by last name
        elif term=="Last Name":
            if det[i][2]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('open sans',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                i=i-1
                if i==-1:
                    break
        #searching by mobile
        elif term=="Mobile":
            if det[i][5]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('open sans',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                break
        #searching by email
        elif term=="Email":
            if det[i][6]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('Open sans',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                break
        else:
            pass
    conn.commit()
    conn.close()    

#frame for customer details
Frame(window,height=48,width=930,bg='white').place(x=350,y=150)
Label(window,text='Customer Details',bg='white',font=('arial',18,'bold')).place(x=720,y=150)
Frame(window,bg='white',width=930,height=320).place(x=350,y=190)

#label, dropdown menu for searching
Label(window,text='\u2192   Search By:',bg='white',font=('Arial',10,'bold')).place(x=350,y=198)
clicked=StringVar()
clicked.set("Customer ID")
drop=OptionMenu(window,clicked,"Customer ID","First Name","Last Name","Mobile","Email")
drop.place(x=450,y=198)
drop.config(width=15,background='white')

#entry for searching
search=Entry(window,relief=SOLID)
search.place(x=375,y=235,height=28,width=175)
Button(window, text="Search",font=('Arial',8,'bold'),fg='white',bg="#1d2951",width=8,height=1,cursor='hand2',command=srch).place(x=560,y=236)

#table
def tbl():
    table=Frame(window,height=580,width=950,bg='white')
    table.place(x=370,y=280)

    try:
        #try fetching data from database
        conn=sqlite3.connect('booking.db')
        c=conn.cursor()
        c.execute("SELECT oid, fname, lname, gender, dob, mob, email, address, nationality, Room_Number from customers")
        lst=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst=[]
    finally:
        #Table headings
        lst.insert(0,('ID','First Name','Last Name','Gender','Date of Birth','Mobile','Email','Address','Nationality','Room'))

    #creating a table
    total_rows =len(lst)
    total_columns=len(lst[0])
    for i in range(total_rows):
        if i==0:
            #table heading
            fontt=('Arial',10,'bold')
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=('Arial',10)
            jus=LEFT
            bgc='white'
        for j in range(total_columns):
            #width for all columns
            if j==0:
                wid=5
            elif j==1 or j==2:
                wid=17
            elif j==3:
                wid=8
            elif j==4:
                wid=13
            elif j==5:
                wid=12
            elif j==6:
                wid=20
            elif j==7:
                wid=14
            elif j==8:
                wid=10
            else:
                wid=8
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

#calling table function
tbl()

window.mainloop()