#import modules
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
            mob.insert(0,rec[0][4])
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

#submit function
def submit():
    #add values to database
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("INSERT INTO customers VALUES (:fn, :ln, :gen, :dob, :mob, :email, :address, :nationality, :cod, :number)",
        {
            'fn':fn.get(),
            'ln':ln.get(),
            'gen':gen.get(),
            'dob':dob.get(),
            'mob':mob.get(),
            'email':eml.get(),
            'address':add.get(),
            'nationality':nat.get(),
            'cod':cod.get(),
            'number':rno.get()
        })
    conn.commit()

    #get customer id for just booked customer
    c.execute("SELECT oid from customers where mob=:phn",{'phn':mob.get()})
    cid=c.fetchall()

    #display customer id
    messagebox.showinfo("Booking","Room Booked Successfully, CustomerID: {}".format(cid[0][0]))
    conn.commit()
    conn.close()

    #update table
    table()
    #reset entries
    reset()

    try:
        #create bill for new customer
        conn=sqlite3.connect('booking.db')
        c=conn.cursor()
        c.execute("""CREATE TABLE bill(
            cid int,
            particular text,
            rate int,
            qty int,
            price int
        )""")
        conn.commit()
        conn.close()
    except:
        pass

    #get room number and number of days from customers table
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number,days from customers where oid=:cid",{'cid':cid[0][0]})
    room=c.fetchall()
    conn.commit()
    conn.close()

    #get price and room type from room table
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Price,Room_Type from room where Room_Number=:cid",{'cid':room[0][0]})
    price=c.fetchall()
    conn.commit()
    conn.close()
    days=room[0][1]
    rtype=price[0][1]
    prc=price[0][0]
    
    #inserting values to bill for room
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("INSERT INTO bill VALUES (:cid, :particular, :rate, :qty, :prc)",
    {
        'cid':cid[0][0],
        'particular':rtype,
        'rate':prc,
        'qty':days,
        'prc':prc*days
    })
    conn.commit()
    conn.close()

#verification for customer update
def verifyforupdate():
    #getting all occupied rooms and adding to a list
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from room WHERE Room_Status=:oc",{'oc':"Occupied"})
    list1=c.fetchall()
    y=[]
    for i in list1:
        y.append(i[0])
    conn.commit()
    conn.close()

    #getting values to verify
    a=fn.get()
    b=ln.get()
    c=gen.get()
    d=dob.get()
    e=mob.get()
    f=eml.get()
    g=add.get()
    h=nat.get()
    i=cod.get()
    j=rno.get()

    #verification
    if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i=="" or j=="":
        messagebox.showerror("Booking","Required Fields Empty!")
    elif len(d)!=4:
        messagebox.showerror("Booking","Invalid Date")
    elif len(e)!=10:
        messagebox.showerror("Booking","Invalid Phone Number")
    elif "@" and ".com" not in f:
        messagebox.showerror("Booking","Invalid Email")
    elif j!="T1" and j!="T2" and j!="T3" and j!="C1" and j!="C2" and j!="R1" and j!="R2" and j!="R3" and j!="R4":
        messagebox.showerror("Booking","Invalid Room Number")
    elif d[0].isalpha() or d[1].isalpha() or d[2].isalpha() or d[3].isalpha():
        messagebox.showerror("Booking","Invalid Date")
    elif e[0].isalpha() or e[1].isalpha() or e[2].isalpha() or e[3].isalpha() or e[4].isalpha() or e[5].isalpha() or e[6].isalpha() or e[7].isalpha() or e[8].isalpha() or e[9].isalpha():
        messagebox.showerror("Booking","Invalid Phone Number")
    elif i[0].isalpha() or i[len(i)-1].isalpha() or len(i)>2:
        messagebox.showerror("Booking","Invalid Number of Days")
    else:
        #occupied room verification 
        if j in y:
            conn=sqlite3.connect('booking.db')
            c=conn.cursor()
            c.execute("SELECT Room_Number from customers where mob=:phn",{'phn':e})
            rn=c.fetchall()
            conn.commit()
            conn.close()
            if j==rn[0][0]:
                update()
            else:
                messagebox.showerror("Booking","Room Full")
        else:
            update()

#update function           
def update():
    a=rno.get()
    days=cod.get()
    
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("""UPDATE customers SET
        fname=:a,
        lname=:b,
        gender=:d,
        dob=:e,
        mob=:f,
        email=:g,
        address=:h,
        nationality=:i,
        days=:k,
        Room_Number=:l
        WHERE oid=:cid""",{
            'a':fn.get(),
            'b':ln.get(),
            'd':gen.get(),
            'e':dob.get(),
            'f':mob.get(),
            'g':eml.get(),
            'h':add.get(),
            'i':nat.get(),
            'k':cod.get(),
            'l':rno.get(),
            'cid':cid.get()
        })
    conn.commit()
    conn.close()
    reset()
    table()

    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Price, Room_Type from room WHERE Room_Number=:number",{'number':a})
    price=c.fetchall()
    conn.commit()
    conn.close()
    rtype=price[0][1]
    prc=price[0][0]
    summ=int(days)*int(prc)
    print(summ)

    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("""UPDATE bill SET
    particular=:newroom,
    rate=:price,
    qty=:days,
    price=:money WHERE cid=:cid""",{'newroom':rtype,'price':prc,'days':days,'money':summ,'cid':cid.get()})
    conn.commit()
    conn.close()

    messagebox.showinfo("Update","Updated information Success")

#verification for submitting
def verifyforsubmit():
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from room WHERE Room_Status=:oc",{'oc':"Occupied"})
    list1=c.fetchall()
    y=[]
    for i in list1:
        y.append(i[0])
    conn.commit()
    conn.close()
    
    a=fn.get()
    b=ln.get()
    c=gen.get()
    d=dob.get()
    e=mob.get()
    f=eml.get()
    g=add.get()
    h=nat.get()
    i=cod.get()
    j=rno.get()
    if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i=="" or j=="":
        messagebox.showerror("Booking","Required Fields Empty!")
    elif len(d)!=4:
        messagebox.showerror("Booking","Invalid Date")
    elif len(e)!=10:
        messagebox.showerror("Booking","Invalid Phone Number")
    elif "@" and ".com" not in f:
        messagebox.showerror("Booking","Invalid Email")
    elif j!="T1" and j!="T2" and j!="T3" and j!="C1" and j!="C2" and j!="R1" and j!="R2" and j!="R3" and j!="R4":
        messagebox.showerror("Booking","Invalid Room Number")
    elif j in y:
        messagebox.showerror("Booking","Room Full")
    elif d[0].isalpha() or d[1].isalpha() or d[2].isalpha() or d[3].isalpha():
        messagebox.showerror("Booking","Invalid Date")
    elif i[0].isalpha() or i[len(i)-1].isalpha() or len(i)>2:
        messagebox.showerror("Booking","Invalid Number of Days")
    elif e[0].isalpha() or e[1].isalpha() or e[2].isalpha() or e[3].isalpha() or e[4].isalpha() or e[5].isalpha() or e[6].isalpha() or e[7].isalpha() or e[8].isalpha() or e[9].isalpha():
        messagebox.showerror("Booking","Invalid Phone Number")
    else:
        submit()

#Labels for data entry
Frame(window,bg='white',height=31,width=870).place(x=350,y=228)

Frame(window,bg='white',width=253,height=270).place(x=350,y=198)
Label(window,text="Customer ID:",bg='white',font=('Open sans',12)).place(x=335,y=230)
Label(window,text="First Name:",bg='white',font=('Open sans',12)).place(x=335,y=255)
Label(window,text="Last Name:",bg='white',font=('Open sans',12)).place(x=335,y=280)
Label(window,text="Gender:",bg='white',font=('Open sans',12)).place(x=335,y=305)
Label(window,text="Birth Year:",bg='white',font=('Open sans',12)).place(x=335,y=330)
Label(window,text="Mobile:",bg='white',font=('Open sans',12)).place(x=335,y=355)
Label(window,text="Email:",bg='white',font=('Open sans',12)).place(x=335,y=380)
Label(window,text="Address:",bg='white',font=('Open sans',12)).place(x=335,y=405)
Label(window,text="Nationality:",bg='white',font=('Open sans',12)).place(x=335,y=430)

#Entry boxes
cid=Entry(window,relief=SOLID)
fn=Entry(window,relief=SOLID)
ln=Entry(window,relief=SOLID)
gen=Entry(window,relief=SOLID)
dob=Entry(window,relief=SOLID)
mob=Entry(window,relief=SOLID)
eml=Entry(window,relief=SOLID)
add=Entry(window,relief=SOLID)
nat=Entry(window,relief=SOLID)

cid.place(x=430,y=227,height=25,width=155)
fn.place(x=430,y=252,height=25,width=155)
ln.place(x=430,y=277,height=25,width=155)
gen.place(x=430,y=302,height=25,width=155)
dob.place(x=430,y=327,height=25,width=155)
mob.place(x=430,y=352,height=25,width=155)
eml.place(x=430,y=377,height=25,width=155)
add.place(x=430,y=402,height=25,width=155)
nat.place(x=430,y=427,height=25,width=155)

#entries for booking room
Frame(window,bg='white',width=253,height=130).place(x=350,y=468)
Label(window,text="No. of Nights:",bg='white',font=('open sans',12)).place(x=335,y=452)
Label(window,text="Room No.:",bg='white',font=('open sans',12)).place(x=335,y=476)

cod=Entry(window,relief=SOLID)
rno=Entry(window,relief=SOLID)

cod.place(x=430,y=452,height=25,width=155)
rno.place(x=430,y=476,height=25,width=155)

#buttons
Button(window,text="RETRIEVE",font=('Arial',9,'bold'),fg='white',bg="#1d2951",width=9,height=1,cursor='hand2',command=fetch).place(x=512, y=227)
Button(window,text="SAVE",font=('Arial',9,'bold'),fg='white',bg="#1d2951",width=6,height=1,cursor='hand2',command=verifyforsubmit).place(x=405, y=520)
update1=Button(window,text="UPDATE",font=('Arial',8,'bold'),fg='white',bg="#1d2951",width=6,height=1,cursor='hand2',state=DISABLED,command=verifyforupdate)
update1.place(x=470, y=520)
Button(window,text="RESET",font=('Arial',9,'bold'),fg='white',bg="#1d2951",width=6,height=1,cursor='hand2',command=reset).place(x=538, y=520)
table()
window.mainloop()