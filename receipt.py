#import required modules
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# window
window=Tk()
window.geometry("1400x720")
window.title("RECEIPT & TRANSACTION")
window.minsize(width=200,height=200)
Photo= Image.open("bg6.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
icon=ImageTk.PhotoImage(Image.open("Icons/checkout.png"))
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

def open_home():
    window.destroy()
    import home

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
Button(image=icon4,compound=LEFT,text='CUSTOMER RECORD',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Customer_records).place(x=3,y=389,height=65,width=312)
Button(image=icon5,compound=LEFT,text='RECEIPT & TRANSACTION',font=('Times',16,'bold'),fg='#00008b',bg='light blue',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2").place(x=3,y=452,height=65,width=312)
Button(image=icon6,compound=LEFT,text='CUSTOMER SERVICE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=customer_service).place(x=3,y=515,height=65,width=312)
Button(image=icon7,compound=LEFT,text='PROFILE',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=Account_profile).place(x=3,y=578,height=65,width=312)
Button(image=icon8,compound=LEFT,text='LOG OUT',font=('Times',17,'bold'),fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=log_out).place(x=3,y=641,height=65,width=312)

Button(image=icon9,fg='#00008b',bg='#f0f8ff',activebackground='white',activeforeground='black',relief=GROOVE,cursor="hand2",command=open_nots).place(x=1430,y=100,height=33,width=33)
#bill and payment banner
a=Frame(window,height=83,width=930,bg='white').place(x=350,y=150)
Label(window,text='Bill and Payment',bg='white',font=('Segoe Print',18)).place(x=717,y=150)

#bill
def bill():
    def reset():
        par.delete(0,END)
        rat.delete(0,END)
        qty.delete(0,END)

    #submit function for database update and connection
    def submit():
        #add a record to bill
        def add():
            a=search.get()
            conn=sqlite3.connect('booking.db')
            c=conn.cursor()
            c.execute("INSERT INTO bill VALUES (:cid, :particular, :rate, :qty, :prc)",
                {
                    'cid':a,
                    'particular':part,
                    'rate':rate,
                    'qty':quant,
                    'prc':rate*quant
                })
            conn.commit()
            conn.close()
            #update bill o
            bill()
        
        #getting the values
        part=par.get()
        rate=int(rat.get())
        quant=int(qty.get())
        a=len(lst)-1
        #directly add to database
        if a==1:
            add()
        #if entries are present
        else:
            while a>1:
                #if that item of that price is present in database, update quantity of existing entry
                if part==lst[a][0] and rate==lst[a][1]:
                    conn=sqlite3.connect('booking.db')
                    c=conn.cursor()
                    c.execute("SELECT qty from bill where particular=:par",{'par':part})
                    oldqty=c.fetchall() #old quantity
                    conn.commit()
                    newqty=oldqty[0][0]+int(quant) #new quantity
                    #update quantity and price
                    c.execute("""UPDATE bill SET
                    qty=:newqt,
                    price=:newprice
                    WHERE particular=:par""",
                    {
                        'newqt':newqty,
                        'newprice':newqty*rate,
                        'par':part
                        })
                    conn.commit()
                    conn.close()
                    bill()
                    break
                else:
                    #if the entry is not already present in database, we add a new entry
                    a=a-1
                    if a==1:
                        add()

    #verification of bill entry               
    def verify():
        b=rat.get()
        c=qty.get()

        #if fields are empty
        if a=="" or b=="" or c=="":
            messagebox.showerror("Bill","Required Fields Empty!")
        #if number is negative
        elif b[0]=="-" or c[0]=="-":
            messagebox.showerror("Bill","Invalid Rate/Quantity")
        else:
            # check if entered data is integer
            try:
                int(b)
                int(c)
                submit()
            except:
                messagebox.showerror("Bill","Invalid Rate/Quantity")

    #Authentication check for user
    def verification():
        top=Toplevel()
        top.geometry('390x255')
        top.title('Confirm Authentication')

        #frame and label for toplevel
        Frame(top,bg='#b0c4de',height=400,width=400).place(x=0,y=0)
        Label(top, text='CONFIRM TRANSACTION', bg="#b0c4de", fg='#1d2951', font=('Arial',20,'bold')).place(x=22, y=20)

        #remove customer data after bill payment
        def removedata():
            msb=messagebox.askquestion("Bill","Do you really want to proceed?")
            if msb=='yes':
                conn=sqlite3.connect('booking.db')
                c=conn.cursor()
                c.execute("SELECT Room_Number from customers where oid=:cid",{'cid':search.get()})
                room=c.fetchall()
                c.execute("""UPDATE room SET Room_Status=:st where Room_Number=:num""",{'st':"Available",'num':room[0][0]})
                conn.commit()
                c.execute("DELETE from bill WHERE cid=:cus",{'cus':a})
                conn.commit()
                c.execute("DELETE from customers WHERE oid=:cid",{'cid':a})
                conn.commit()
                conn.close()
                messagebox.showinfo("Bill","Transaction success")
                
                window.destroy()
                import home

        #show password functionality for password
        def show():
            if (showw.get()==1):
                passw.config(show='')
            else:
                passw.config(show='*')

        #checking user password
        def confirm():
            try:
                conn=sqlite3.connect('admins.db')
                c=conn.cursor()
                c.execute("SELECT ps from users WHERE status=:act",{'act':True})
                ps=c.fetchall()
                conn.commit()
                conn.close()
                if ps[0][0]==passw.get():
                    removedata()
            except:
                messagebox.showerror("Bill","Unable to Procedure")

        #Entry for password
        Label(top,bg='#b0c4de',text='Password:',font=('Arial',11,'bold')).place(x=50,y=75)
        passw=Entry(top,relief=SOLID)
        passw.place(x=145,y=73,height=27,width=170)

        #checkbutton for password
        showw=IntVar(value=1)
        Checkbutton(top,text='Show',offvalue=0,variable=showw,bg='#b4cef3',command=show).place(x=145,y=108)

        #Button for confirm or cancel
        Button(top,text="CONFIRM",font=('Arial',10,'bold'),fg='white',bg="black",width=8,height=1,cursor='hand2',command=lambda:confirm()).place(x=100, y=160)
        Button(top,text="CANCEL",font=('Arial',10,'bold'),fg='white',bg="black",width=8,height=1,cursor='hand2',command=lambda:top.destroy()).place(x=195, y=160)  

    #Getting customer id
    a=search.get()
    
    #Fetching data for bill
    try:
        conn=sqlite3.connect('booking.db')
        c=conn.cursor()
        c.execute("SELECT particular, rate, qty, price from bill WHERE cid=:search",{'search':a})
        lst=c.fetchall()
        conn.commit()
        conn.close()

    #if data doesn't exist, use empty list    
    except:
        lst=[]
    
    #if list is empty, show error to the user
    if lst==[]:
        search.delete(0,END)
        messagebox.showerror("Bill","Invalid Customer ID")
    else:
        #add and display bill

        #Labels for entry
        Frame(window,bg='white',width=320,height=220).place(x=350,y=233)
        Label(window,bg='white',text='Particular:',font=('Arial',11,'bold')).place(x=370,y=270)
        Label(window,bg='white',text='Rate:',font=('Arial',11,'bold')).place(x=370,y=310)
        Label(window,bg='white',text='Quantity:',font=('Arial',11,'bold')).place(x=370,y=350)

        #Entry for bill items
        par=Entry(window,relief=SOLID)
        par.place(x=470,y=268,height=27,width=170)
        rat=Entry(window,relief=SOLID)
        rat.place(x=470,y=308,height=27,width=170)
        qty=Entry(window,relief=SOLID)
        qty.place(x=470,y=348,height=27,width=170)

        #Buttons
        Button(window,text="SAVE",font=('Arial',12,'bold'),fg='white',bg="#1d2951",width=6,height=1,cursor='hand2',command=verify).place(x=460, y=390)
        Button(window,text="RESET",font=('Arial',12,'bold'),fg='white',bg="#1d2951",width=6,height=1,cursor='hand2',command=reset).place(x=560, y=390)
        
        Frame(window,height=270,width=350,bg='white').place(x=800,y=350)
        #Heading of table
        lst.insert(0, ("Particular","Rate","Qty","Price"))

        def table():
        #Frame for table
            table=Frame(window,height=580,width=950,bg='white')
            table.place(x=803,y=350)

            #Creating a table
            total_rows =len(lst)
            total_columns=len(lst[0])
            for i in range(total_rows):
                #font for table heading
                if i==0:
                    fontt=('Arial',10,'bold')
                    ht=3
                #font for items in table
                else:
                    fontt=('Arial',10)
                    ht=1

                #setting width for individual column
                for j in range(total_columns):
                    if j==0:
                        jus=LEFT
                        wid=15
                    elif j==1:
                        jus=CENTER
                        wid=8
                    elif j==2:
                        jus=CENTER
                        wid=6
                    elif j==3:
                        jus=CENTER
                        wid=10
                    
                    #table
                    e=Label(
                        table,
                        width=wid,
                        font=fontt,
                        justify=jus,
                        bg='white',
                        height=ht
                    )
                    e.grid(row=i,column=j)
                    #table entries
                    e.config(text=(lst[i][j]))
            
            #calculating total price till now
            price=[]
            for i in range(1,len(lst)):
                price.append(lst[i][3])
            
            #display total
            Label(window,text="Total:",font=('Arial',10,'bold'),bg='white').place(x=1010,y=550)
            Label(window, text=(sum(price)),bg='white',font=('Arial',10)).place(x=1080,y=550)

        table()
        Button(window, text="Pay",font=('Arial',9,'bold'),fg='white',bg="#1d2951",width=8,height=1,cursor='hand2',command=verification).place(x=1060,y=575)

#Label for entering customer id
Label(window,text='\u2192  Enter Customer ID:',bg='white',font=('open sans',11,'bold')).place(x=350,y=203)

#Bill Frame
Frame(window,height=370,width=350,bg='white').place(x=800,y=250)
#image for bill
photo2=PhotoImage(file='lg1.png')
logo=Label(window, image=photo2).place(x=800,y=250)
#Billing resort deatails
Label(window,text="GREEN VILLAGE RESORT",font=('Alegreya sans',15,'bold'),bg='white').place(x=910,y=270)
Label(window,text="Baneshwor, Kathmandu",font=('Times',14,),bg='white').place(x=967,y=295)
Label(window,text="Phone: 9809416671, 9762485642",font=('Times',10),bg='white').place(x=965,y=320)
#Entry and button to get bill of individual customer
search=Entry(window,relief=SOLID)
search.place(x=520,y=200,height=28,width=175)
Button(window, text="Get Bill",font=('Arial',8,'bold'),fg='white',bg="#1d2951",width=8,height=1,cursor='hand2',command=bill).place(x=700,y=201)

window.mainloop()