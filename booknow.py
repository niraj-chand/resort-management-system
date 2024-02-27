
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
