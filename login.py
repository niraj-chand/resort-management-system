#import modules
from tkinter import *
from tkinter import messagebox
import random
import sqlite3
from PIL import Image, ImageTk

#creating a window
window=Tk()
window.geometry("1400x700")
window.title("Green village-login")
window.iconbitmap(r'icon.ico')
window.minsize(width=200,height=200)
Photo= Image.open("background1.png")
resized_image=Photo.resize((1540,850))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
#login function
def login():
    #signup page
    def opensignup():
        window.destroy()
        import signup
    
    def openstatus():
        window.destroy()
        import home
        

# #login frame
    f1=Frame(window,width=400,height=450, highlightbackground="#483d8b", highlightthickness=2,bg="white")
    f1.place(x=960,y=200)
    f2=Frame(window,width=380,height=80,bg="#1d2951")
    f2.place(x=970,y=207)
    Label(window,text="LOG IN",fg="white",bg="#1d2951",font=("arial bold",25)).place(x=1100,y=225)
    #authorization check
    def check():
        a=mail.get()
        b=ps.get()
        try:
            conn=sqlite3.connect('admins.db')
            c=conn.cursor()

            c.execute("SELECT * from users")
            records=c.fetchall()
            i=len(records)-1
            while i>=0:
                if records[i][2]!=a or records[i][4]!=b:
                    i=i-1
                    if i==-1:
                        messagebox.showerror("Login","Invalid Credentials")
                        break
                else:
                    #Switch the user's status to active upon login and deactivate all other users.
                    c.execute("""UPDATE users SET
                    status=:inactive
                    WHERE status=:active""",
                    {'inactive':False,
                    'active':True})
                    conn.commit()
                    
                    c.execute("""UPDATE users SET
                    status= :val
                    WHERE mail = :a""",
                    {
                        'val':True,
                        'a':a
                    })
                    conn.commit()
                    messagebox.showinfo("Login","Success! Logged in")
                    openstatus()
                    break           
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Login","Sign Up First")

    
    def remove(event):
        a=mail.get()
        if a=='Enter Your Email':
            mail.delete(0, END) #removes text from 0 index to end

    def remove2(event):
        b=ps.get()  
        if b=='Enter Your Password': 
            ps.delete(0, END)
        
    #email and password 
    Label(window,text="Email Address",bg="white",font=(1)).place(x=990,y=300)
    mail=Entry(window,width=36,highlightbackground="black", highlightthickness=2,font=("Helvetica",12))
    mail.insert(0, 'Enter Your Email') 
    mail.place(x=995,y=330,height=30)
    mail.bind('<FocusIn>', remove) #bind function is used to know the mouse movement (if it is clicked or hovering and so on)
    Label(window,text="Password",bg="white",font=(1)).place(x=990,y=380)
    ps=Entry(window,width=36,highlightbackground="black", highlightthickness=2,font=("Helvetica",12))
    ps.insert(0, 'Enter Your Password')
    ps.place(x=995,y=408,height=30)
    ps.bind('<FocusIn>', remove2)
    showw=IntVar(value=1)

    def show():
        if (showw.get()==1): #checkbutton passes value 1 for true and 0 for false
            ps.config(show='') 
        else:
            ps.config(show='*')

    #show password checkbutton
    check_btn = Checkbutton(window, offvalue=0, text="Show", variable=showw,bg="white",command=show)
    check_btn.place(x=1264,y=417,height=10)

    #login button
    button1=Button(window,width=32,text='Log In',cursor='hand2',fg="white",font=("arial bold",13),bg='#483d8b',command=login)
    button1.place(x=995,y=490,height=33)

    #forgot password and signup links
    button2=Button(window,text='Forgot Password?',cursor='hand2',fg="blue",font=('Open Sans',10,'bold'),bg='white',command=reset)
    button2.place(x=1199,y=445)

    Label(window,text="Don't have an account?",bg="white",font=("arial bold",12)).place(x=1070,y=550)
    button3=Button(window,width=13,text='Sign Up Here',cursor='hand2',bg="white",font=("Arial baltic",11),fg='blue',relief=GROOVE,command=opensignup)
    button3.place(x=1097,y=580,height=30)
    #verification check
    def verify():
        a=mail.get()
        b=ps.get()
        if (a=="" or a=="Enter Your Email") or (b=="" or b=="Enter Your Password"):
            messagebox.showerror("Login","Missing required fields")
        elif "@" and ".com" not in a:
            messagebox.showerror("Password Reset","Invalid Email")
        elif len(b)<6:
            messagebox.showerror("Password Reset","Password must be more than 6 characters")
        else:
            check()

    #login button
    button1=Button(window,width=32,text='Log In',cursor='hand2',fg="white",font=("arial bold",13),bg='#483d8b',command=verify)
    button1.place(x=995,y=490,height=33)

#forgot password
def reset():

    #creating a toplevel
    top=Toplevel()
    top.geometry('400x360')
    top.title('Forgot Password')
    top.iconbitmap(r'icon.ico')


    Frame(top,bg='#b0c4de',height=400,width=400).place(x=0,y=0)
    Label(top, text='Reset Password', bg="#b0c4de", fg='#1d2951', font=('Arial',20,'bold')).place(x=75, y=20)

    def remove(event):
        a=mail.get()
        if a=='Enter Your Email':
            mail.delete(0, END)

    def remove2(event):
        b=new_ps_ent.get()
        if b=='New Password':
            new_ps_ent.delete(0, END)

    def remove3(event):
        c=new_psc_ent.get()
        if c=='Confirm New Password':
            new_psc_ent.delete(0, END)

    #show password 
    def show():
        if (showw.get()==1):
            new_ps_ent.config(show='')
        else:
            new_ps_ent.config(show='*')

    def show2():
        if (showww.get()==1):
            new_psc_ent.config(show='')
        else:
            new_psc_ent.config(show='*')
    
    #USER INPUTS
    mail=Entry(top)
    mail.insert(0, 'Enter Your Email')
    mail.place(x=40, y=75,width=290, height=30)
    mail.bind('<FocusIn>', remove)

    #security questions
    ans1=StringVar()
    a="Q1:  What is your favourite music genre?"
    b="Q2: What is your favourite sport?"
    c="Q3: What do you want to be when you were child?"
    lst=[a,b,c]
    ques=random.choice(lst)
    num=int(ques[1])-1
    Label(top,text=ques,bg='#b0c4de').place(x=40,y=118)
    Entry(top,textvariable=ans1).place(x=40,y=140,width=290,height=30)

    #new password
    new_ps_ent=Entry(top)
    new_ps_ent.insert(0, 'New Password') #default text inserted in entry box, 0 is positional argument
    new_ps_ent.place(x=40, y=190,width=210, height=30)
    new_ps_ent.bind('<FocusIn>', remove2) #bind function is used to know the mouse movement 
    showw=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showw,bg='#b0c4de',command=show).place(x=260,y=193)

    new_psc_ent=Entry(top)
    new_psc_ent.insert(0, 'Confirm New Password') #default text inserted in entry box, 0 is positional argument
    new_psc_ent.place(x=40, y=230,width=210, height=30)
    new_psc_ent.bind('<FocusIn>', remove3) #bind function is used to know the mouse movement 
    showww=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showww,bg='#b0c4de',command=show2).place(x=260,y=233)

    Button(top,text="CONFIRM",font=('Arial',10,'bold'),fg='white',bg="#483d8b",width=18,height=2,cursor='hand2',command=lambda:verify()).place(x=120, y=280)

    #update new password
    def update():
        a=mail.get()
        b=ans1.get()
        
        #database connection for password update
        conn=sqlite3.connect('admins.db')
        c=conn.cursor()
        c.execute("SELECT * from users")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][2]!=a or records[i][(6+num)]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Password Reset","Invalid Credentials")
                    break
            else:
                ps_upd=new_ps_ent.get()
                psc_upd=new_psc_ent.get()
                c.execute("""UPDATE users SET
                ps= :new_ps,
                psc= :new_psc
                WHERE mail = :a""",
                {
                    'new_ps':ps_upd,
                    'new_psc':psc_upd,
                    'a':a
                })
                messagebox.showinfo("Password Reset","Password Changed Successfully")
               
                top.destroy()
                break             
        conn.commit()
        conn.close()

    #password verification for forgot password functionality
    def verify():
        a=mail.get()
        b=ans1.get()
        c=new_ps_ent.get()
        d=new_psc_ent.get()

        if a=="" or a=="Enter Your Email" or b=="" or c=="" or c=="New Password" or d=="" or d=="Confirm New Password":
            messagebox.showerror("Password Reset","Missing required fields")
        else:
            if "@" and ".com" not in a:
                messagebox.showerror("Password Reset","Invalid Email")
            elif len(c)<6 or len(d)<6:
                messagebox.showerror("Password Reset","Password must be more than 6 characters")
            elif c!=d:
                messagebox.showerror("Password Reset","Passwords do not match")
            else:
                update()

login()

window.mainloop()