import time
import random
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
entry_time = datetime.now()
exit_time = datetime.now()
duration = datetime.now()
#index_key=0





#THIRD WINDOW

def exit_sys():
    global new_ids
    exit = Tk()
    exit.geometry('1180x420')
    exit.config(bg='#86C5D8')

    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)

    def roger():
        def name():
            def Id():
                if len(exit_ent2.get()) == 5:
                    print('success')

                    if int(exit_ent2.get()) == labours_data[index_key]:
                        approve2 = Label(exit, text='(✔ your id is correct)', bg='#86C5D8')
                        approve2.grid(row=3, column=3)
                        exit_time = datetime.now()
                        duration_in_secs = (exit_time - entry_time).total_seconds()
                        duration = round(duration_in_secs/3600, 3)
                        daily_wage_per_hour= 62.5
                        calculated_wage=daily_wage_per_hour*duration
                        print(calculated_wage)
                        print(duration)
                        main_data = data + exit_ent2.get() + '\n' + str(exit_time) + '\n'
                        #decline_2.destroy()
                        duration_label = Label(exit, text='DURATION IN THE SYSTEM:', font=('Times 11 bold'),bg='#86C5D8')
                        duration_label.grid(row=7, column=0)
                        duration_label = Label(exit, text= str(duration) + ' ' + 'Hours', font=('Times 11 bold'), bg='#86C5D8')
                        duration_label.grid(row=8, column=0)
                        wage_label=Label(exit, text='YOUR WAGE CALCULATED IS:', font=('Times 11 bold'),bg='#86C5D8')
                        wage_label.grid(row=9, column=0)
                        final_wage=Label(exit, text= str(calculated_wage) + ' ' + 'Rs' , font=('Times 11 bold'), bg='#86C5D8')
                        final_wage.grid(row=10,column=0)
                        with open('(Labours Exit Data).txt', 'a') as f:
                            f.writelines(main_data)

                    else:
                        decline_2 = Label(exit, text='(✖ your id is not correct correct)', bg='#86C5D8')
                        decline_2.grid(row=3, column=3)


                else:
                    decline2 = Label(exit, text='(✖ your id lenght is not correct)', bg='#86C5D8')
                    decline2.grid(row=3, column=3)

            for k in labours_data:
                if k == exit_ent1.get():
                    print(k)
                    index_key = k
                    # print(type(k))
                    print(labours_data[k])
                    # print(type(labours_data[k]))
                    # index_key=labours_data[k]
                    # print(labours_data[index_key])
                    data = exit_ent1.get() + '\n'
                    #decline1.destroy()
                    approve1 = Label(exit, text='(✔ your name is in our system)', bg='#86C5D8')
                    approve1.grid(row=2, column=3)
                    Id()
                else:
                    decline1 = Label(exit, text='(✖ your name is not in our system)', bg='#86C5D8')
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

    clock = Label(exit, font=('Times 20 bold'), bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(exit, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM', font=('Times 20 bold'), pady=20, bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    exit_label = Label(exit, text='EXIT SYSTEM', font=('Times 20 bold'), bg='#86C5D8')
    exit_label.grid(row=1, columnspan=2)


    name = Label(exit, text='ENTER YOUR FULL NAME', font=('Times 10 bold'), pady=10, bg='#86C5D8')
    name.grid(row=2, column=0)

    exit_ent1 = Entry(exit, width=45, bd=5, textvariable=input1)
    exit_ent1.grid(row=2, column=1)

    uniqueid = Label(exit, text='ENTER YOUR ID', font=('Times 10 bold'), pady=10, bg='#86C5D8')
    uniqueid.grid(row=3, column=0)

    exit_ent2 = Entry(exit, width=45, bd=5, textvariable=input2)
    exit_ent2.grid(row=3, column=1)

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

    format1 = Label(exit, text='use lower case alphabets only', font=('Times 10 '), bg='#86C5D8')
    format1.grid(row=2, column=2)

    format2 = Label(exit, text='enter only in numbers', font=('Times 10'), bg='#86C5D8')
    format2.grid(row=3, column=2)

    copy_rights = Label(exit, text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved', pady=20, bg='#86C5D8')
    copy_rights.grid(row=9, column=2, columnspan=3)

    TM()
    exit.mainloop()










#SECOND WINDOW

def new_window():
    gui_login = Tk()
    gui_login.geometry('1180x320')
    gui_login.config(bg='#86C5D8')
    def TM():
        Time = time.strftime('%I:%M:%S')
        clock.config(text=Time)
        clock.after(200, TM)


    def roger():
        def name():
            def Id():
                if len(login_ent2.get()) == 5:
                    print('success')

                    if int(login_ent2.get()) == labours_data[index_key]:
                        #decline2.destroy()
                        approve2 = Label(gui_login, text='(✔ your id is correct)', bg='#86C5D8')
                        approve2.grid(row=3, column=3)
                        entry_time = datetime.now()
                        main_data = data + login_ent2.get() + '\n' + str(entry_time) + '\n'
                        with open('(Labours Entry Data).txt', 'a') as f:
                            f.writelines(main_data)

                    else:
                        decline2 = Label(gui_login, text='(✖ your id is not correct correct)', bg='#86C5D8')
                        decline2.grid(row=3, column=3)


                else:
                    decline2 = Label(gui_login, text='(✖ your id lenght is not correct)', bg='#86C5D8')
                    decline2.grid(row=3, column=3)

            for k in labours_data:
                if k == login_ent1.get():
                    print(k)
                    index_key=k
                    #print(type(k))
                    print(labours_data[k])
                    #print(type(labours_data[k]))
                    #index_key=labours_data[k]
                    #print(labours_data[index_key])
                    data = login_ent1.get() + '\n'
                    #decline1.destroy()
                    approve1 = Label(gui_login, text='(✔ your name is in our system)', bg='#86C5D8')
                    approve1.grid(row=2, column=3)
                    Id()
                else:
                    decline1 = Label(gui_login, text='(✖ your name is not in our system)',bg='#86C5D8')
                    decline1.grid(row=2, column=3)



        name()


    #def clear2():
    #    global clean2
    #    clean2=''
    #    input1.set(clean2)
    #    print(input1)
    #    input2.set(clean2)
    #    print(input2)

    #clean2=''
    #input1 = StringVar()
    #input2 = StringVar()

    clock = Label(gui_login,font=('Times 20 bold'),bg='#86C5D8')
    clock.grid(rowspan=2, column=4)

    outsource = Label(gui_login, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM',font=('Times 20 bold'),pady=20,bg='#86C5D8')
    outsource.grid(row=0, columnspan=2)

    login_label =Label(gui_login, text='LOGIN SYSTEM',font=('Times 20 bold'),bg='#86C5D8')
    login_label.grid(row=1, columnspan=2)

    name = Label(gui_login, text='ENTER YOUR FIRST NAME',font=('Times 10 bold'),pady=10,bg='#86C5D8')
    name.grid(row=2, column=0)

    login_ent1 = Entry(gui_login,width=45,bd=5)
    login_ent1.grid(row=2, column=1)

    uniqueid = Label(gui_login, text='ENTER YOUR ID',font=('Times 10 bold'),pady=10,bg='#86C5D8')
    uniqueid.grid(row=3, column=0)

    login_ent2 = Entry(gui_login,width=45,bd=5)
    login_ent2.grid(row=3, column=1)

    submit = Button(gui_login, text='SUBMIT', command=roger,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    submit.place(x=350, y=200)

    next1 = Button(gui_login, text='NEXT',relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    next1.place(x=500,y=200)

    empty=Label(gui_login, text='',bg='#86C5D8')
    empty.grid(row=4,column=3)

    empty = Label(gui_login, text='', bg='#86C5D8')
    empty.grid(row=5, column=3)

    exit1=Button(gui_login, text='EXIT SYSTEM', command=exit_sys,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
    exit1.place(x=420,y=240)

    format1 = Label(gui_login,text='(enter you first name only)',font=('Times 10 '),bg='#86C5D8')
    format1.grid(row=2, column=2)

    format2 = Label(gui_login,text='(enter your unique id)',font=('Times 10'),bg='#86C5D8')
    format2.grid(row=3, column=2)

    copy_rights=Label(gui_login,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
    copy_rights.grid(row=6,column=2,columnspan=3)

    TM()
    gui_login.mainloop()









#FIRST WINDOW

signup=Tk()
signup.config(bg='#86C5D8')
signup.attributes('-fullscreen')
new_ids=[]
alphabets=[]
labours_data={}
def id_generation():
    if ent1.get() !="Enter Your First Name" or ent2.get() !="Enter Your Last Name" or ent3.get() !="03**-*******" or ent4.get() !='' or ent5.get() !='6/22/19' or ent6.get() !='' or ent7.get() !='':
        randomlist = random.sample(range(0, 9), 5)
        code = str(randomlist[0]) + str(randomlist[1]) + str(randomlist[2]) + str(randomlist[3]) + str(randomlist[4])
        new_ids.append(code)
        print(new_ids)
        alphabets.append(ent1.get())
        print(ent1.get())
        labours_data[ent1.get()]=int(code)
        print(labours_data)
        text_input= code
        new_id=Label(signup,text='(you can login to the system)',bg='#86C5D8',pady=20)
        new_id.grid(row=12,column=0,columnspan=2)
        new_code=Label(signup,text='your id is'+' '+ text_input,bg='#86C5D8',font=('Times 20 bold'))
        new_code.grid(row=12, column=2)
        bio_data=ent1.get()+'\n'+ ent2.get()+'\n'+ ent3.get()+'\n'+ ent4.get()+'\n'+ ent5.get()+'\n'+ ent6.get()+'\n'+ ent7.get()+'\n'+'XX-------------------XX---------------------XX'
        with open('(labours bio data).txt','a') as f:
            f.writelines(bio_data)
#       def destroy1():
#           signup.destroy()

#       destroy1()
        new_window()
    else:
        print("can't be empty")

def clear1():
    global clean
    clean=''
    textinput1.set(clean)
    textinput2.set(clean)
    textinput3.set(clean)
    number4.set(clean)
    textinput5.set(clean)
    number6.set(clean)
    number7.set(clean)
clean=''
textinput1=StringVar()
textinput2=StringVar()
textinput3=StringVar()
textinput5=StringVar()


def clear_search1(event):
    ent1.delete(0,END)

def clear_search2(event):
    ent2.delete(0,END)

def clear_search3(event):
    ent3.delete(0,END)

#def clear_search4(event):
    #ent4.delete(0,END)

#def clear_search5(event):
    #ent5.delete(0,END)

#def clear_search6(event):
    #ent6.delete(0,END)

#def clear_search7(event):
    #ent7.delete(0, END)




lab1=Label(signup,text='OUT SOURCING LABOURS MANAGEMENT SYSTEM',font=('Times 20 bold'),pady=20,bg='#86C5D8')
lab1.grid(row=0,columnspan=3)

lab2=Label(signup,text='First Name',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab2.grid(row=1,column=0,columnspan=2)

ent1=Entry(signup,width=45,bd=5,textvariable=textinput1)
ent1.grid(row=1,column=2)
ent1.insert(0,"Enter Your First Name")
ent1.bind("<Button-1>", clear_search1)

lab3=Label(signup,text='Last Name',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab3.grid(row=2,column=0,columnspan=2)

ent2=Entry(signup,width=45,bd=5,textvariable=textinput2)
ent2.grid(row=2,column=2)
ent2.insert(0,"Enter Your Last Name")
ent2.bind("<Button-1>", clear_search2)

lab7=Label(signup,text='Mobile Number',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab7.grid(row=6,column=0,columnspan=2)

ent3=Entry(signup,width=45,bd=5,textvariable=textinput3)
ent3.grid(row=6,column=2)
ent3.insert(0,"03**-*******")
ent3.bind("<Button-1>", clear_search3)

lab8=Label(signup,text='Gender',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab8.grid(row=7,column=0,columnspan=2)

#ent4=Entry(signup,width=45,bd=5,textvariable=textinput4)
#ent4.grid(row=7,column=2)
#ent4.insert(0, "MALE/FEMALE")
#ent4.bind("<Button-1>", clear_search4)


number4 = StringVar()
ent4 = ttk.Combobox(signup, width=45,textvariable=number4)
ent4['values'] = ('','Male','Female','Others')
ent4.grid(row=7,column=2)
ent4.current(0)



lab9=Label(signup,text='Date Of Birth',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab9.grid(row=8,column=0,columnspan=2)

#ent5=Entry(signup,width=45,bd=5,textvariable=textinput5)
#ent5.grid(row=8,column=2)
#ent5.insert(0, "DATE/MONTH/YEAR")
#ent5.bind("<Button-1>", clear_search5)


ent5 = DateEntry(signup, width=45, year= , month=6, day=22,
background='lightblue', foreground='black', borderwidth=2)
ent5.grid(row=8,column=2)

lab10=Label(signup,text='Country',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab10.grid(row=9,column=0,columnspan=2)

#ent6=Entry(signup,width=45,bd=5,textvariable=textinput6)
#ent6.grid(row=9,column=2)
#ent6.insert(0, "Enter Your Country Name")
#ent6.bind("<Button-1>", clear_search6)


number6 = StringVar()
ent6 = ttk.Combobox(signup, width=45,textvariable=number6)
ent6['values'] = ('','Pakistan','India','Bangladesh')
ent6.grid(row=9,column=2)
ent6.current(0)



lab11=Label(signup,text='City',bg='#86C5D8',pady=20,font=('Times 15 bold'))
lab11.grid(row=10,column=0,columnspan=2)

#ent7=Entry(signup,width=45,bd=5,textvariable=textinput7)
#ent7.grid(row=10,column=2)
#ent7.insert(0, "Enter Your City Name")
#ent7.bind("<Button-1>", clear_search7)


number7 = StringVar()
ent7 = ttk.Combobox(signup, width=45,textvariable=number7)
ent7['values'] = ('','Karachi','Hyderabad','Lahore','Islamabad')
ent7.grid(row=10,column=2)
ent7.current(0)



btn2=Button(signup,text='SignUp',command=id_generation,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
btn2.place(x=340,y=540)

btn3=Button(signup,text='Clear All',command=clear1,relief=GROOVE,bd=5,width=15,activebackground='#4682B4')
btn3.place(x=495,y=540)
empty=Label(signup,text='',bg='#86C5D8',pady=10)
empty.grid(row=11,column=2)
copy_rights=Label(signup,text='© 2021 MUHAMMAD EMMAD SIDDIQUI.  All rights reserved',pady=20,bg='#86C5D8')
copy_rights.grid(row=13,column=2,columnspan=3)

signup.mainloop()
