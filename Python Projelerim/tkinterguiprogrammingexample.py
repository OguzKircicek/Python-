from tkinter import *
from tkinter.ttk import *
import pymysql.cursors

db=pymysql.connect("localhost","root","","blog",use_unicode=True,charset="utf8")
cursor=db.cursor()
cursor.execute('SET NAMES UTF8')
menu=Tk()


def dataekle():
    isim=iadi.get()
    soyisim=isadi.get()
    bolum=combo1.get()
    sql="INSERT INTO kullanıcılar (adi,soyadi,bolum) VALUES ('%s','%s','%s')" % (isim,soyisim,bolum)
    cursor.execute(sql)
    db.commit()
    datalistele()

def datalistele():
    sql="SELECT * FROM kullanıcılar"
    cursor.execute(sql)
    results=cursor.fetchall()
    liste.delete(*liste.get_children())
    for row in results:
        liste.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        db.commit()

def listetikla():
    adtext=liste.item(liste.selection()[0])['values'][0]
    soytext=liste.item(liste.selection()[0])['values'][1]
    bolumtext=liste.item(liste.selection()[0])['values'][2]

    iadi.delete(0,END)
    iadi.insert(0,adtext)

    isadi.delete(0,END)
    isadi.insert(0,soytext)

    combo1.delete(0,END)
    combo1.insert(0,bolumtext)
def ara():
    tar=tara.get()
    sql = "SELECT * FROM kullanıcılar where id IN (%s)" % tar
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        iadi.insert(0,row[1])
        isadi.insert(0,row[2])
        combo1.delete(0,END)
        combo1.insert(0,row[3])
        db.commit()

def guncelle():
    tar=tara.get()
    isim=iadi.get()
    soy=isadi.get()
    bolum=combo1.get()

    sql="UPDATE kullanıcılar SET adi='%s',soyadi='%s',bolum='%s'  where id='%s';" % (isim,soy,bolum,tar)
    cursor.execute(sql)
    db.commit()
    datalistele()


lara=Label(menu,text="Adı  : ").grid(row=1,column=1)
tara=Entry(menu)

tara.grid(row=6,column=6)


btn1=Button(menu,text="ARA",command=ara)
btn1.grid(row=6,column=7)

ladi=Label(menu,text="Adı  : ").grid(row=1,column=1)
iadi=Entry(menu)
iadi.grid(row=1,column=2)

lsadi=Label(menu,text="Soyadı : ")
lsadi.grid(row=2,column=1)

isadi=Entry(menu)
isadi.grid(row=2,column=2)

bollabel=Label(menu,text="Bölümü : ")
bollabel.grid(row=3,column=1)

combo1=Combobox(menu,width=15)
combo1['values']=("Bilgisayar","Makine","Motor","Endüstri")
combo1.current(0)
combo1.grid(row=3,column=2)

btn=Button(menu,text="Güncelle",command=guncelle)
btn.grid(row=4,column=2)

liste=Treeview(menu,height=10,column=0)
liste["columns"]=("sut1","sut2","sut3")
liste.grid(row=5,column=1,columnspan=3)

liste.heading("#0",text="Id")
liste.heading("sut1",text="Adı")
liste.heading("sut2",text="Soyadı")
liste.heading("sut3",text="Bölümü")

liste.bind('<ButtonRelease-1>',listetikla)

datalistele()

menu.mainloop()