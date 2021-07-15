import time
import random
from datetime import datetime
from tkinter import *
entry_time =datetime.now()
exit_time =datetime.now()
duration =datetime.now()






#THIRD WINDOW
def exit_sys():
    global new_ids
    exit = Tk()
    exit.geometry('1180x320')
    exit.config(bg='#86C5D8')

    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)

    alphabets = ['Muhammad Emmad Siddiqui', 'ghufran']
    ids = new_ids

    def roger():
        def name():
            def Id():
                if len(ent2.get()) == 5:
                    if ent2.get() in ids:
                        approve2 = Label(exit, text='(✔ your id is correct)', bg='#86C5D8')
                        approve2.grid(row=3, column=3)
                        exit_time=datetime.now()
                        duration =exit_time - entry_time
                        #duration=StringVar()
                        duration_label = Label(exit, text= 'duration', bg='#86C5D8')
                        duration_label.grid(row=7, column=0)
                        print(exit_time - entry_time)
                        main_data = data + ent2.get() + '\n' + str(exit_time) + '\n'

                        with open('labours data.txt', 'a') as f:
                            f.writelines(main_data)


                else:
                    decline2 = Label(exit, text='(✖ your id lenght is not correct)', bg='#86C5D8')
                    decline2.grid(row=3, column=3)

            if ent1.get() in alphabets:
                data = ent1.get() + '\n'
                approve1 = Label(exit, text='(✔ your name is in our system)', bg='#86C5D8')
                approve1.grid(row=2, column=3)
                Id()
            else:
                decline1 = Label(exit, text='(✖ use the right format)', bg='#86C5D8')
                decline1.grid(row=2, column=3)

        name()

    def clear():
        clean = ''
        input1.set(clean)
        input2.set(clean)

    input1 = StringVar()
    input2 = StringVar()


    def final_exit():
        exit.destroy()

    clock = Label(exit, font=('arial 20 bold'), bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(exit, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM', font=('arial 20 bold'), pady=20, bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    exit_label = Label(exit, text='EXIT SYSTEM', font=('arial 20 bold'), bg='#86C5D8')
    exit_label.grid(row=1, columnspan=2)


    name = Label(exit, text='ENTER YOUR FULL NAME', font=('arial 10 bold'), pady=10, bg='#86C5D8')
    name.grid(row=2, column=0)

    ent1 = Entry(exit, width=45, bd=5, textvariable=input1)
    ent1.grid(row=2, column=1)

    uniqueid = Label(exit, text='ENTER YOUR ID', font=('arial 10 bold'), pady=10, bg='#86C5D8')
    uniqueid.grid(row=3, column=0)

    ent2 = Entry(exit, width=45, bd=5, textvariable=input2)
    ent2.grid(row=3, column=1)

    submit = Button(exit, text='SUBMIT', command=roger, relief=GROOVE, bd=5, width=15, activebackground='#4682B4')
    submit.place(x=350, y=200)

    next = Button(exit, text='NEXT', command=clear, relief=GROOVE, bd=5, width=15, activebackground='#4682B4')
    next.place(x=500, y=200)

    empty = Label(exit, text='', bg='#86C5D8')
    empty.grid(row=4, column=0)

    empty = Label(exit, text='', bg='#86C5D8')
    empty.grid(row=5, column=0)

    empty = Label(exit, text='', bg='#86C5D8')
    empty.grid(row=6, column=3)


    exit2 = Button(exit, text='EXIT', command=final_exit, relief=GROOVE, bd=5, width=15, activebackground='#4682B4')
    exit2.place(x=420, y=240)

    format1 = Label(exit, text='use lower case alphabets only', font=('arial 10 '), bg='#86C5D8')
    format1.grid(row=2, column=2)

    format2 = Label(exit, text='enter only in numbers', font=('arial 10'), bg='#86C5D8')
    format2.grid(row=3, column=2)

    copy_rights = Label(exit, text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved', pady=20, bg='#86C5D8')
    copy_rights.grid(row=8, column=2, columnspan=3)

    TM()
    exit.mainloop()










#SECOND WINDOW

def new_window():
    global new_ids
    gui_login = Tk()
    gui_login.geometry('1180x320')
    gui_login.config(bg='#86C5D8')
    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)


    alphabets = ['Muhammad Emmad Siddiqui','ghufran']
    ids = new_ids


    def roger():
        def name():
            def Id():
                if len(ent2.get()) == 5:
                    if ent2.get() in ids:
                        approve2 = Label(gui_login, text='(✔ your id is correct)', bg='#86C5D8')
                        approve2.grid(row=3, column=3)
                        entry_time = datetime.now()
                        main_data = data + ent2.get() + '\n' + str(entry_time) + '\n'
                        with open('labours data.txt', 'a') as f:
                            f.writelines(main_data)


                else:
                    decline2 = Label(gui_login, text='(✖ your id lenght is not correct)', bg='#86C5D8')
                    decline2.grid(row=3, column=3)

            if ent1.get() in alphabets:
                data = ent1.get() + '\n'
                approve1 = Label(gui_login, text='(✔ your name is in our system)',bg='#86C5D8')
                approve1.grid(row=2, column=3)
                Id()
            else:
                decline1 = Label(gui_login, text='(✖ use the right format)',bg='#86C5D8')
                decline1.grid(row=2, column=3)



        name()


    def clear():
        clean=''
        input1.set(clean)
        input2.set(clean)


    input1=StringVar()
    input2=StringVar()

    clock = Label(gui_login,font=('arial 20 bold'),bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(gui_login, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM',font=('arial 20 bold'),pady=20,bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    login_label =Label(gui_login, text='LOGIN SYSTEM',font=('arial 20 bold'),bg='#86C5D8')
    login_label.grid(row=1, columnspan=2)

    name = Label(gui_login, text='ENTER YOUR FULL NAME',font=('arial 10 bold'),pady=10,bg='#86C5D8')
    name.grid(row=2, column=0)

    ent1 = Entry(gui_login,width=45,bd=5,textvariable=input1)
    ent1.grid(row=2, column=1)

    uniqueid = Label(gui_login, text='ENTER YOUR ID',font=('arial 10 bold'),pady=10,bg='#86C5D8')
    uniqueid.grid(row=3, column=0)

    ent2 = Entry(gui_login,width=45,bd=5,textvariable=input2)
    ent2.grid(row=3, column=1)

    submit = Button(gui_login, text='SUBMIT', command=roger,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    submit.place(x=350, y=200)

    next=Button(gui_login, text='NEXT', command=clear,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    next.place(x=500,y=200)

    empty=Label(gui_login, text='',bg='#86C5D8')
    empty.grid(row=4,column=3)

    empty = Label(gui_login, text='', bg='#86C5D8')
    empty.grid(row=5, column=3)

    exit1=Button(gui_login, text='EXIT SYSTEM', command=exit_sys,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    exit1.place(x=420,y=240)

    format1 = Label(gui_login,text='use lower case alphabets only',font=('arial 10 '),bg='#86C5D8')
    format1.grid(row=2, column=2)

    format2 = Label(gui_login,text='enter only in numbers',font=('arial 10'),bg='#86C5D8')
    format2.grid(row=3, column=2)

    copy_rights=Label(gui_login,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
    copy_rights.grid(row=6,column=2,columnspan=3)

    TM()
    gui_login.mainloop()











#FIRST WINDOW

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
#    def destroy1():
#        signup.destroy()

#    destroy1()
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







