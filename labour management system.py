import time
import string
from tkinter import *
def new_window():
    gui = Tk()
    gui.geometry('1180x240')
    gui.config(bg='#86C5D8')
    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)


    alphabets = ['emmad','ghufran']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ids = ['12345678','87654321']


    def roger():
        def name():
            if ent1.get() in alphabets:
                data = ent1.get() + '\n'
                approve1 = Label(gui, text='(approved ✔)',bg='#86C5D8')
                approve1.grid(row=1, column=3)


                def Id():
                    if len(ent2.get()) == 8:
                        if ent2.get() in ids:
                            current_time=time.strftime('%I:%M:%S')
                            main_data = data + ent2.get() + '\n' + current_time + '\n'
                            with open('labours data.txt', 'a') as f:
                                f.writelines(main_data)

                    else:
                        decline2 = Label(gui, text='(your id lenght is nor correct)',bg='#86C5D8')
                        decline2.grid(row=3, column=3)

                calling_id= Id()
            else:
                decline1 = Label(gui, text='(✖ use the right format)',bg='#86C5D8')
                decline1.grid(row=1, column=3)



        name()


    clock = Label(gui,font=('arial 20 bold'),bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(gui, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM',font=('arial 20 bold'),pady=20,bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    name = Label(gui, text='ENTER YOUR FULL NAME',font=('arial 10 bold'),pady=10,bg='#86C5D8')
    name.grid(row=1, column=0)

    ent1 = Entry(gui,width=40,bd=5)
    ent1.grid(row=1, column=1)

    uniqueid = Label(gui, text='ENTER YOUR ID',font=('arial 10 bold'),pady=10,bg='#86C5D8')
    uniqueid.grid(row=2, column=0)

    ent2 = Entry(gui,width=40,bd=5)
    ent2.grid(row=2, column=1)

    submit = Button(gui, text='SUBMIT', command=roger,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    submit.grid(row=3, column=1)

    format1 = Label(gui,text='use lower case alphabets only',font=('arial 10 '),bg='#86C5D8')
    format1.grid(row=1, column=2)

    format2 = Label(gui,text='enter only in numbers',font=('arial 10'),bg='#86C5D8')
    format2.grid(row=2, column=2)

    copy_rights=Label(gui,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
    copy_rights.grid(row=4,column=2,columnspan=3)

    TM()
    gui.mainloop()

signup=Tk()
signup.config(bg='#86C5D8')

def id_generation():
    new_id=Label(signup,text='')
    new_id.grid(row=12,column=0,columnspan=2)
    new_window()
def clear():
    global clean
    clean=''
    textinput1.set(clean)
    textinput2.set(clean)
    textinput3.set(clean)
    textinput4.set(clean)
    textinput5.set(clean)
    textinput6.set(clean)
    textinput7.set(clean)

clean=''
textinput1=StringVar()
textinput2=StringVar()
textinput3=StringVar()
textinput4=StringVar()
textinput5=StringVar()
textinput6=StringVar()
textinput7=StringVar()
lab1=Label(signup,text='OUT SOURCING LABOURS MANAGEMENT SYSTEM',font=('arial 20 bold'),pady=20,bg='#86C5D8')
lab1.grid(row=0,columnspan=3)

lab2=Label(signup,text='First Name',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab2.grid(row=1,column=0,columnspan=2)

ent1=Entry(signup,width=40,bd=5,textvariable=textinput1)
ent1.grid(row=1,column=2)

lab3=Label(signup,text='Last Name',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab3.grid(row=2,column=0,columnspan=2)

ent2=Entry(signup,width=40,bd=5,textvariable=textinput2)
ent2.grid(row=2,column=2)

lab7=Label(signup,text='Mobile Number',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab7.grid(row=6,column=0,columnspan=2)

ent6=Entry(signup,width=40,bd=5,textvariable=textinput3)
ent6.grid(row=6,column=2)

lab8=Label(signup,text='Gender',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab8.grid(row=7,column=0,columnspan=2)

ent7=Entry(signup,width=40,bd=5,textvariable=textinput4)
ent7.grid(row=7,column=2)

lab9=Label(signup,text='Date Of Birth',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab9.grid(row=8,column=0,columnspan=2)

ent8=Entry(signup,width=40,bd=5,textvariable=textinput5)
ent8.grid(row=8,column=2)

lab10=Label(signup,text='Country',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab10.grid(row=9,column=0,columnspan=2)

ent9=Entry(signup,width=40,bd=5,textvariable=textinput6)
ent9.grid(row=9,column=2)

lab11=Label(signup,text='City',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab11.grid(row=10,column=0,columnspan=2)

ent10=Entry(signup,width=40,bd=5,textvariable=textinput7)
ent10.grid(row=10,column=2)

btn2=Button(signup,text='SignUp',command=id_generation,width=10,bd=5,activebackground='#4682B4')
btn2.grid(row=11,column=1,columnspan=2)

btn3=Button(signup,text='Clear All',width=7,command=clear,bd=5,activebackground='#4682B4')
btn3.grid(row=11,column=2,columnspan=3)

copy_rights=Label(signup,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
copy_rights.grid(row=13,column=2,columnspan=3)

signup.mainloop()

