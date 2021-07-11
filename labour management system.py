import time
import string
from tkinter import *
gui = Tk()

def TM():
    Time = time.strftime('%I:%M:%S')
    clock.config(text=Time)
    clock.after(200, TM)


alphabets = ['e','m','a','d']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ids = ['12345678','87654321']


def roger():
    def name():
        if list(ent1.get()) in alphabets:
            data = ent1.get() + '\n'
            approve1 = Label(gui, text='approved ✔')
            approve1.grid(row=1, column=3)

            def Id():
                if len(ent2.get()) == 8:
                    if ent2.get() in ids:
                        current_time=time.strftime('%I:%M:%S')
                        main_data = data + ent2.get() + '\n' + current_time + '\n'
                        with open('labours data.txt', 'a') as f:
                            f.writelines(main_data)

                else:
                    decline2 = Label(gui, text='your id lenght is nor correct')
                    decline2.grid(row=3, column=3)


        else:
            decline1 = Label(gui, text='✖ use the above format ')
            decline1.grid(row=2, column=3)

            Id()

    name()


clock = Label(gui)
clock.grid(rowspan=2, column=4)
outsource = Label(gui, text='OUT SOURCING LABOURS MANAGEMENT SYSTEM')
outsource.grid(row=0, columnspan=2)
name = Label(gui, text='ENTER YOUR NAME')
name.grid(row=1, column=0)
ent1 = Entry(gui)
ent1.grid(row=1, column=1)
uniqueid = Label(gui, text='ENTER YOUR ID')
uniqueid.grid(row=2, column=0)
ent2 = Entry(gui)
ent2.grid(row=2, column=1)
submit = Button(gui, text='SUBMIT', command=roger)
submit.grid(row=3, column=1)
format1 = Label(gui,text='use lower case alphabets only')
format1.grid(row=1, column=2)
format2 = Label(gui,text='enter only in numbers')
format2.grid(row=2, column=2)
TM()
gui.mainloop()
