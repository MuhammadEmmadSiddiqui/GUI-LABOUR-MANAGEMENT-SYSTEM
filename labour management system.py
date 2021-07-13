import time
import random
import string
from tkinter import *
def exit_sys():
    global new_ids
    exit = Tk()
    exit.geometry('1180x240')
    exit.config(bg='#86C5D8')

    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)

    alphabets = ['Muhammad Emmad Siddiqui', 'ghufran']
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ids = new_ids

    def roger():
        def name():
            def Id():
                if len(ent2.get()) == 5:
                    if ent2.get() in ids:
                        approve2 = Label(exit, text='(✔ your id is correct)', bg='#86C5D8')
                        approve2.grid(row=2, column=3)
                        current_time = time.strftime('%I:%M:%S')
                        main_data = data + ent2.get() + '\n' + current_time + '\n'
                        with open('labours data.txt', 'a') as f:
                            f.writelines(main_data)


                else:
                    decline2 = Label(exit, text='(✖ your id lenght is not correct)', bg='#86C5D8')
                    decline2.grid(row=2, column=3)

            if ent1.get() in alphabets:
                data = ent1.get() + '\n'
                approve1 = Label(exit, text='(✔ your name is in our system)', bg='#86C5D8')
                approve1.grid(row=1, column=3)
                Id()
            else:
                decline1 = Label(exit, text='(✖ use the right format)', bg='#86C5D8')
                decline1.grid(row=1, column=3)

        name()

    def clear():
        clean = ''
        input1.set(clean)
        input2.set(clean)

    input1 = StringVar()
    input2 = StringVar()

    clock = Label(exit, font=('arial 20 bold'), bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(exit, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM', font=('arial 20 bold'), pady=20, bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    name = Label(exit, text='ENTER YOUR FULL NAME', font=('arial 10 bold'), pady=10, bg='#86C5D8')
    name.grid(row=1, column=0)

    ent1 = Entry(exit, width=45, bd=5, textvariable=input1)
    ent1.grid(row=1, column=1)

    uniqueid = Label(exit, text='ENTER YOUR ID', font=('arial 10 bold'), pady=10, bg='#86C5D8')
    uniqueid.grid(row=2, column=0)

    ent2 = Entry(exit, width=45, bd=5, textvariable=input2)
    ent2.grid(row=2, column=1)

    submit = Button(exit, text='SUBMIT', command=roger, relief=GROOVE, bd=5, width=15, activebackground='#4682B4')
    submit.place(x=350, y=160)

    next = Button(exit, text='NEXT', command=clear, relief=GROOVE, bd=5, width=15, activebackground='#4682B4')
    next.place(x=500, y=160)

    empty = Label(exit, text='', bg='#86C5D8')
    empty.grid(row=3, column=3)

    empty = Label(exit, text='', bg='#86C5D8')
    empty.grid(row=4, column=3)

    exit = Button(exit, text='EXIT', command=exit_sys, relief=GROOVE, bd=5, width=15, activebackground='#4682B4')
    exit.place(x=420, y=200)

    format1 = Label(exit, text='use lower case alphabets only', font=('arial 10 '), bg='#86C5D8')
    format1.grid(row=1, column=2)

    format2 = Label(exit, text='enter only in numbers', font=('arial 10'), bg='#86C5D8')
    format2.grid(row=2, column=2)

    copy_rights = Label(exit, text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved', pady=20, bg='#86C5D8')
    copy_rights.grid(row=5, column=2, columnspan=3)

    TM()
    exit.mainloop()












def new_window():
    global new_ids
    gui = Tk()
    gui.geometry('1180x240')
    gui.config(bg='#86C5D8')
    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)


    alphabets = ['Muhammad Emmad Siddiqui','ghufran']
    #numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ids = new_ids


    def roger():
        def name():
            def Id():
                if len(ent2.get()) == 5:
                    if ent2.get() in ids:
                        approve2 = Label(gui, text='(✔ your id is correct)', bg='#86C5D8')
                        approve2.grid(row=2, column=3)
                        current_time = time.strftime('%I:%M:%S')
                        main_data = data + ent2.get() + '\n' + current_time + '\n'
                        with open('labours data.txt', 'a') as f:
                            f.writelines(main_data)


                else:
                    decline2 = Label(gui, text='(✖ your id lenght is not correct)', bg='#86C5D8')
                    decline2.grid(row=2, column=3)

            if ent1.get() in alphabets:
                data = ent1.get() + '\n'
                approve1 = Label(gui, text='(✔ your name is in our system)',bg='#86C5D8')
                approve1.grid(row=1, column=3)
                Id()
            else:
                decline1 = Label(gui, text='(✖ use the right format)',bg='#86C5D8')
                decline1.grid(row=1, column=3)



        name()


    def clear():
        clean=''
        input1.set(clean)
        input2.set(clean)


    input1=StringVar()
    input2=StringVar()

    clock = Label(gui,font=('arial 20 bold'),bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(gui, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM',font=('arial 20 bold'),pady=20,bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    name = Label(gui, text='ENTER YOUR FULL NAME',font=('arial 10 bold'),pady=10,bg='#86C5D8')
    name.grid(row=1, column=0)

    ent1 = Entry(gui,width=45,bd=5,textvariable=input1)
    ent1.grid(row=1, column=1)

    uniqueid = Label(gui, text='ENTER YOUR ID',font=('arial 10 bold'),pady=10,bg='#86C5D8')
    uniqueid.grid(row=2, column=0)

    ent2 = Entry(gui,width=45,bd=5,textvariable=input2)
    ent2.grid(row=2, column=1)

    submit = Button(gui, text='SUBMIT', command=roger,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    submit.place(x=350, y=160)

    next=Button(gui, text='NEXT', command=clear,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    next.place(x=500,y=160)

    empty=Label(gui, text='',bg='#86C5D8')
    empty.grid(row=3,column=3)

    empty = Label(gui, text='', bg='#86C5D8')
    empty.grid(row=4, column=3)

    exit=Button(gui, text='EXIT', command=exit_sys,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    exit.place(x=420,y=200)

    format1 = Label(gui,text='use lower case alphabets only',font=('arial 10 '),bg='#86C5D8')
    format1.grid(row=1, column=2)

    format2 = Label(gui,text='enter only in numbers',font=('arial 10'),bg='#86C5D8')
    format2.grid(row=2, column=2)

    copy_rights=Label(gui,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
    copy_rights.grid(row=5,column=2,columnspan=3)

    TM()
    gui.mainloop()
signup=Tk()
signup.config(bg='#86C5D8')
new_ids=[]
def id_generation():
    randomlist = random.sample(range(0, 9), 5)
    code = str(randomlist[0]) + str(randomlist[1]) + str(randomlist[2]) + str(randomlist[3]) + str(randomlist[4])
    new_ids.append(code)
    print(new_ids)
    text_input= code
    new_id=Label(signup,text='(you can login to the system)',bg='#86C5D8',pady=20)
    new_id.grid(row=12,column=0,columnspan=2)
    new_code=Label(signup,text='your id is'+' '+ text_input,bg='#86C5D8',font=('arial 20 bold'))
    new_code.grid(row=12, column=2)
    bio_data=ent1.get()+'\n'+ ent2.get()+'\n'+ ent3.get()+'\n'+ ent4.get()+'\n'+ ent5.get()+'\n'+ ent6.get()+'\n'+ ent7.get()+'\n'
    with open('labours bio data.txt','a') as f:
        f.writelines(bio_data)



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

ent1=Entry(signup,width=45,bd=5,textvariable=textinput1)
ent1.grid(row=1,column=2)

lab3=Label(signup,text='Last Name',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab3.grid(row=2,column=0,columnspan=2)

ent2=Entry(signup,width=45,bd=5,textvariable=textinput2)
ent2.grid(row=2,column=2)

lab7=Label(signup,text='Mobile Number',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab7.grid(row=6,column=0,columnspan=2)

ent3=Entry(signup,width=45,bd=5,textvariable=textinput3)
ent3.grid(row=6,column=2)

lab8=Label(signup,text='Gender',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab8.grid(row=7,column=0,columnspan=2)

ent4=Entry(signup,width=45,bd=5,textvariable=textinput4)
ent4.grid(row=7,column=2)

lab9=Label(signup,text='Date Of Birth',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab9.grid(row=8,column=0,columnspan=2)

ent5=Entry(signup,width=45,bd=5,textvariable=textinput5)
ent5.grid(row=8,column=2)

lab10=Label(signup,text='Country',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab10.grid(row=9,column=0,columnspan=2)

ent6=Entry(signup,width=45,bd=5,textvariable=textinput6)
ent6.grid(row=9,column=2)

lab11=Label(signup,text='City',bg='#86C5D8',pady=20,font=('arial 15 bold'))
lab11.grid(row=10,column=0,columnspan=2)

ent7=Entry(signup,width=45,bd=5,textvariable=textinput7)
ent7.grid(row=10,column=2)

btn2=Button(signup,text='SignUp',command=id_generation,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
btn2.place(x=340,y=540)

btn3=Button(signup,text='Clear All',command=clear,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
btn3.place(x=495,y=540)
empty=Label(signup,text='',bg='#86C5D8')
empty.grid(row=11,column=2)
copy_rights=Label(signup,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
copy_rights.grid(row=13,column=2,columnspan=3)

signup.mainloop()

