#mine niraj chand
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox


window=Tk()
window.geometry("1400x720")
window.title("PROFILE")
window.minsize(width=200,height=200)
Photo= Image.open("bg6.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
icon=ImageTk.PhotoImage(Image.open("Icons/profile.png"))
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

def log_out():
    window.destroy()
    import logout

def open_nots():
    window.destroy();
    import notification


#creating button
Button(image=icon1,compound=LEFT,text='HOME',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_home).place(x=3,y= 200,height=65,width=312)
Button(image=icon2,compound=LEFT,text='ROOM AVAILABILITY',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Room_availability).place(x=3,y=263,height=65,width=312)
Button(image=icon3,compound=LEFT,text='BOOK NOW',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Book_now).place(x=3,y=326,height=65,width=312)
Button(image=icon4,compound=LEFT,text='CUSTOMER RECORD',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Customer_records).place(x=3,y=389,height=65,width=312)
Button(image=icon5,compound=LEFT,text='RECEIPT & TRANSACTION',font=('Times',16,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=receipt_pay).place(x=3,y=452,height=65,width=312)
Button(image=icon6,compound=LEFT,text='CUSTOMER SERVICE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=customer_service).place(x=3,y=515,height=65,width=312)
Button(image=icon7,compound=LEFT,text='PROFILE',font=('Times',17,'bold'),fg='#00008b',bg='light blue',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2").place(x=3,y=578,height=65,width=312)
Button(image=icon8,compound=LEFT,text='LOG OUT',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=log_out).place(x=3,y=641,height=65,width=312)

Button(image=icon9,fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_nots).place(x=1430,y=100,height=33,width=33)
Frame(window, height=615, width=1160, bg='#cc00ff').place(x=350, y=220)

Label(window,text='Account',bg='white',font=('Arial',18,"bold")).place(x=350,y=180)
Frame(window, height=420, width=378, bg='white').place(x=780, y=320)

Label(window,text="First Name:",font=('Arial',11,'bold'),bg='white').place(x=788,y=328)
Label(window,text="Last Name:",font=('Arial',11,'bold'),bg='white').place(x=985,y=328)
Label(window,text="Email:",font=('Arial',11,'bold'),bg='white').place(x=788,y=400)
Label(window,text="Phone:",font=('Arial',11,'bold'),bg='white').place(x=788,y=472)
Label(window,text="Password:",font=('Arial',11,'bold'),bg='white').place(x=788,y=544)
Label(window,text="Confirm Password:",font=('Arial',11,'bold'),bg='white').place(x=985,y=544)

try:
    conn=sqlite3.connect('admins.db')
    c=conn.cursor()
    c.execute("SELECT * from users WHERE status=:act",{'act':True})
    records=c.fetchall()
    a=records[0][0]
    b=records[0][1]
    c=records[0][2]
    d=records[0][3]
    e=records[0][4]
    f=records[0][5]
    conn.commit()
    conn.close()
except:
    a="First Name"
    b="Last Name"
    c="Email"
    d="Phone"
    e="Password"
    f="Confirm Password"

#show password 
def show():
    if (showw.get()==1):
        ps.config(show='')
    else:
        ps.config(show='*')

def show2():
    if (showww.get()==1):
        psc.config(show='')
    else:
        psc.config(show='*')


fname=Entry(window,borderwidth=2,font=("Helvetica",11))
fname.insert(0,a)
fname.place(x=788,y=355,width=160,height=30)

lname=Entry(window,borderwidth=2,font=("Helvetica",11))
lname.insert(0,b)
lname.place(x=985,y=355,width=160,height=30)

mail=Entry(window,borderwidth=2,font=("Helvetica",11))
mail.insert(0,c)
mail.place(x=788,y=425,width=355,height=30)

phone=Entry(window,borderwidth=2,font=("Helvetica",11))
phone.insert(0,d)
phone.place(x=788,y=495,width=355,height=30)

ps=Entry(window,show='*',borderwidth=2,font=("Helvetica",11))
ps.insert(0,e)
ps.place(x=788,y=565,width=160,height=30)
showw=IntVar(value=0)
Checkbutton(text='Show',offvalue=0,variable=showw,bg='white',command=show).place(x=887,y=567)

psc=Entry(window,show='*',borderwidth=2,font=("Helvetica",11))
psc.insert(0,f)
psc.place(x=985,y=565,width=160,height=30)
showww=IntVar(value=0)
Checkbutton(text='Show',offvalue=0,variable=showww,bg='white',command=show2).place(x=1083,y=567)

#logout function
def logout():
    msb=messagebox.askquestion("Logout","Do you really want to logout?")
    if msb=='yes':
        #set user status 
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
# update
def verify():
    a=fname.get()
    b=lname.get()
    c=mail.get()
    d=phone.get()
    e=ps.get()
    f=psc.get()
         
    if (a=="" or a=="First Name") or (b=="" or b=="Last Name") or (c=="" or c=="Enter Your Email") or (d=="" or d=="Enter Your Phone Number") or (e=="" or e=="Create Password") or (f=="" or f=="Confirm Password"):
        messagebox.showerror("Signup","Required fields Empty.")
    elif "@" and ".com" not in c:
        messagebox.showerror("Signup","Invalid Email")
    elif len(e)<6 or len(f)<6:
        messagebox.showerror("Signup","Password must be more than 6 characters")
    elif len(d)!=10:
        messagebox.showerror("Signup","Invalid Phone Number Length")
    elif e!=f:
        messagebox.showerror("Signup","Passwords do not match")
    else:
        try:
            int(d)
            update()
        except:
            messagebox.showerror("Signup","Invalid Phone Number")   
#devil_nct
#update function
def update():
    #database update
    conn=sqlite3.connect('admins.db')
    c=conn.cursor()
    c.execute("""UPDATE users SET
    fname=:a,
    lname=:b,
    mail=:d,
    phone=:e,
    ps=:f,
    psc=:g
    WHERE status=:act""",
    {
        'a':fname.get(),
        'b':lname.get(),
        'd':mail.get(),
        'e':phone.get(),
        'f':ps.get(),
        'g':psc.get(),
        'act':True
    })
    conn.commit()
    conn.close()

    #messagebox after update
    messagebox.showinfo("Accounts","Information updated-sucess")

#delete function
def delete():
    msb=messagebox.askquestion("Delete","Do you really want to delete account ?")
    if msb=='yes':
        conn=sqlite3.connect('admins.db')
        c=conn.cursor()
        c.execute("DELETE from users WHERE status=:act",{'act':True})
        conn.commit()
        conn.close()

        #import function
        window.destroy()
        import login 

Button(window,text="UPDATE",font=('Arial',10,'bold'),fg='white',bg="red",width=11,height=2,cursor='hand2',command=verify).place(x=790, y=670)
Button(window,text="DELETE",font=('Arial',10,'bold'),fg='white',bg="red",width=11,height=2,cursor='hand2',command=delete).place(x=915, y=670)
Button(window,text="LOGOUT",font=('Arial',10,'bold'),fg='white',bg="red",width=11,height=2,cursor='hand2',command=logout).place(x=1050, y=670)

window.mainloop()