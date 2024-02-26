#import modules
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#creating window
window=Tk()
window.geometry("1260x710")
window.title("Green village -sign up")
window.iconbitmap(r'icon.ico')
window.minsize(width=200,height=200)
Photo= Image.open("background1.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
#database table
try:
    conn=sqlite3.connect('admins.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE users(
        fname text,
        lname text,
        mail text PRIMARY KEY,
        phone text,
        ps text,
        psc text,
        q1 text,
        q2 text,
        q3 text,
        status boolean
    )""" )
    conn.commit()
    conn.close()
except:
    pass

#signup function
def signup():
    def openlogin():
        window.destroy()
        import login

    #remove functions are used as placeholders so that when users click on the entry box, inserted text is deleted.
    def remove(event):
        a=fname_ent.get()
        if a=="First Name":
            fname_ent.delete(0, END)

    def remove1(event):
        a=lname_ent.get()
        if a=="Last Name":
            lname_ent.delete(0, END)

    def remove2(event):
        a=mail_ent.get()
        if a=="Enter Your Email":
            mail_ent.delete(0, END)

    def remove3(event):
        a=phone_ent.get()
        if a=="Enter Your Phone Number":
            phone_ent.delete(0, END)

    def remove4(event):
        a=ps_ent.get()
        if a=="Create Password":
            ps_ent.delete(0, END)

    def remove5(event):
        a=psc_ent.get()
        if a=="Confirm Password":
            psc_ent.delete(0, END)

    #show password functions
    def show():
        if (showw.get()==1):
            ps_ent.config(show='')
        else:
            ps_ent.config(show='*')

    def show1():
        if (showww.get()==1):
            psc_ent.config(show='')
        else:
            psc_ent.config(show='*')

    
    signupframe=Frame(window,width=400,height=450,highlightbackground="#483d8b",highlightthickness=2,bg="white")
    signupframe.place(x=960,y=200)
    frame1=Frame(window,width=380,height=80,bg="#1d2951")
    frame1.place(x=970,y=207)
    Label(window,text="SIGN UP",fg="white", bg="#1d2951", font=("arial bold",25)).place(x=1100,y=225)

    #Credentials input
    fname_ent=Entry(window,width=18,highlightbackground="black",highlightthickness=2,font=("Helvetica",11))
    fname_ent.insert(0, 'First Name')
    fname_ent.place(x=995, y=320,height=25)
    fname_ent.bind('<FocusIn>', remove) #bind function is used for the movement of mouse

    lname_ent=Entry(window,width=18,highlightbackground="black",highlightthickness=2,font=("Helvetica",11))
    lname_ent.insert(0,'Last Name')
    lname_ent.place(x=1170, y=320,height=25)
    lname_ent.bind('<FocusIn>', remove1)

    mail_ent=Entry(window,width=40,highlightbackground="black",highlightthickness=2,font=("Helvetica",11))
    mail_ent.insert(0, 'Enter Your Email')
    mail_ent.place(x=995,y=370,height=25)
    mail_ent.bind('<FocusIn>', remove2)

    phone_ent=Entry(window,width=40,highlightbackground="black",highlightthickness=2,font=("Helvetica",11))
    phone_ent.insert(0, 'Enter Your Phone Number')
    phone_ent.place(x=995, y=420,height=25)
    phone_ent.bind('<FocusIn>', remove3)

    ps_ent=Entry(window,width=40,highlightbackground="black",highlightthickness=2,font=("Helvetica",11))
    ps_ent.insert(0, 'Create Password')
    ps_ent.place(x=995, y=470,height=25)
    ps_ent.bind('<FocusIn>', remove4)
    showw=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=showw,bg='white',command=show).place(x=1262,y=477,height=10) #show password checkbutton

    psc_ent=Entry(window,width=40,highlightbackground="black",highlightthickness=2,font=("Helvetica",11))
    psc_ent.insert(0, 'Confirm Password')
    psc_ent.place(x=995, y=520,height=25)
    psc_ent.bind('<FocusIn>', remove5)
    showww=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=showww,bg='white',command=show1).place(x=1262,y=527,height=10)

    #verification function
    def verify():
        a=fname_ent.get()
        b=lname_ent.get()
        c=mail_ent.get()
        d=phone_ent.get()
        e=ps_ent.get()
        f=psc_ent.get()
            
        if (a=="" or a=="First Name") or (b=="" or b=="Last Name") or (c=="" or c=="Enter Your Email") or (d=="" or d=="Enter Your Phone Number") or (e=="" or e=="Create Password") or (f=="" or f=="Confirm Password"):
            messagebox.showerror("Signup","Missing required fields")
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
                sques()
            except:
                messagebox.showerror("Signup","Invalid Phone Number")

    #Next and back button
    backbutton=Button(window,text="Back", width=12,font=('Arial',13,'bold'),fg='white',bg="#483d8b",cursor='hand2',command=openlogin)
    backbutton.place(x=995,y=580,height=33)
    nextbutton=Button(window,text="Next", width=12,font=('Arial',13,'bold'),fg='white',bg="#483d8b",cursor='hand2',command=verify)
    nextbutton.place(x=1194,y=580,height=33)
    
    def sques():
        a=StringVar()
        b=StringVar()
        d=StringVar()

        Frame(height=300,width=350,bg='white').place(x=990,y=290)
        
        Label(text="Security Questions",font=('Arial',16,'bold'),bg='white',fg='#1d2951').place(x=1065,y=290)

        Label(text="Q1: What is your favourite music genre?",bg='white').place(x=1014,y=333)
        Entry(window, textvariable=a).place(x=1014, y=363, width=290, height=30)
        
        Label(text="Q2: What is your favourite sport?",bg='white').place(x=1014 ,y=403)
        Entry(window, textvariable=b).place(x=1014, y=433, width=290, height=30)

        Label(text="Q3: What do you want to be when you were child?",bg='white').place(x=1014,y=473)
        Entry(window,textvariable=d).place(x=1014, y=503, width=290, height=30)

        #verification for security questions
        def verify2():
            aa=a.get()
            bb=b.get()
            cc=d.get()

            if aa=="" or bb=="" or cc=="":
                messagebox.showerror("Security Questions","Missing required fields")
            else:
                submit()

        #database connection for signup
        def submit():
            conn=sqlite3.connect('admins.db')
            c=conn.cursor()
            c.execute("INSERT INTO users VALUES (:fname, :lname, :mail, :phone, :ps, :psc, :q1, :q2, :q3, :status)",
            {
                'fname':fname_ent.get(),
                'lname':lname_ent.get(),
                'mail':mail_ent.get(),
                'phone':phone_ent.get(),
                'ps':ps_ent.get(),
                'psc':psc_ent.get(),
                'q1':a.get(),
                'q2':b.get(),
                'q3':d.get(),
                'status':False
                })
            conn.commit()
            conn.close()

            messagebox.showinfo("Signup","Sign-up Successful")

            openlogin()

        #signup button
       
        Button(window,text="SIGN UP", width=32,font=('Arial',13,'bold'),fg='white',bg="#483d8b",cursor='hand2',command=verify2).place(x=995,y=580,height=33)
       
signup()


window.mainloop()
