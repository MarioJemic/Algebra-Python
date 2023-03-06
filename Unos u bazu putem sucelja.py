import tkinter as tk
import sqlite3
from tkinter import *

def my_reset():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry): # If this is an Entry widget class
            widget.delete(0,'end')   # delete all entries 
     
       

db = sqlite3.connect('baza_podataka.db')

try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE korisnici (
                korisnikID INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT (20) ,
                password TEXT (10) );''')
            print('table created successfully')

except:
            print('baza vec postoji')
            db.rollback()
db.close()

def UnesiMe():
    db = sqlite3.connect('baza_podataka.db')
    cur = db.cursor()
    qry = "insert into korisnici (user_name,password) values(?,?);"

    try:
        cur = db.cursor()
        cur.execute(qry,  (txt_entry_Korisnik.get(), txt_entry_Password.get(),))
        db.commit()
        print("records added successfully")
    except:
        print("error in operation unesi")
        db.rollback()
    db.close()
 

def ObrisiMe():
    db = sqlite3.connect('baza_podataka.db')
    try:

        qry = 'DELETE FROM korisnici WHERE user_name=?'
        cur = db.cursor()
        cur.execute(qry,  txt_entry_Korisnik.get() )
        db.commit()
        print("record successfully removed")
    except:
        print("error in operation obrisi")
        db.rollback()
    db.close()


def IspisiMe():
    my_reset()
    db = sqlite3.connect('baza_podataka.db')
    sql = "SELECT * FROM korisnici"
    cur = db.cursor()
    cur.execute(sql)
    j=0
    while True:
        
        record = cur.fetchone()
        print(record)
        if record == None:  
           break 
        else:
            i = 0 
             
            for element in record:                     
                    e = Entry(root, width=10) 
                    e.grid(row=4 + j, column=i)
                    e.insert(END, element)                     
                    i = i+1
                    
             
        j=j+1

    
    

root = tk.Tk()
root.title("Zadaca")
root.geometry("600x400")


Korisnik = tk.Label(root, text="User Name")
Korisnik.grid(column=0, row=0, padx=5, pady=5)
txt_entry_Korisnik = tk.Entry(bd=3)
txt_entry_Korisnik.grid(column=1, row=0, padx=5, pady=5)

Password = tk.Label(root, text="Password")
Password.grid(column=0, row=1, padx=5, pady=5)
txt_entry_Password = tk.Entry(bd=3)
txt_entry_Password.grid(column=1, row=1, padx=5, pady=5)

Unesi = tk.Button(root, text="Unesi", command=UnesiMe)
Unesi.grid(column=0, row=2, padx=5, pady=5)

Obrisi = tk.Button(root, text="Obrisi", command=ObrisiMe)
Obrisi.grid(column=1, row=2, padx=5, pady=5)

Ispisi = tk.Button(root, text="Ispisi", command=IspisiMe)
Ispisi.grid(column=2, row=2, padx=5, pady=5)

#Unesi.bind("<Button-1>", on_Unesi)
#Obrisi.bind("<Button-2>", on_Obrisi)
#Ispisi.bind("<Button-3>", on_Ispisi)

root.mainloop()


def main() : 
    pass

# glavni program
main()
 
