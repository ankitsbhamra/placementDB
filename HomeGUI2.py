from Tkinter import *
import Backend
import ImageTk
import functools
from Tix import *
import traceback

#path="Images"
#print path

def enter(e1,e2,e3,e4,e5,e6,frame8):
    try:
        e1=e1.get()
        e2=e2.get()
        e3=float(e3.get())
        e4=float(e4.get())
        e5=float(e5.get())
        e6=e6.get()
        print e1,e2,e3,e4,e5,e6
    except ValueError as e:
        print e
        #print traceback.print_exc()
        la = Label(frame8, text=e)
        la.pack(padx=10, pady=10)
    else:
        m=Backend.insertAcademics(e1,e2,e3,e4,e5,e6)
        la = Label(frame8, text=m)
        la.pack(padx=10, pady=10)
        print m
    #finally:
def insAca():
    rootf=Toplevel()
    rootf.title("Insert into academics")

    root=Frame(rootf)
    root.pack(side=TOP,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1=Label(frame1,text="USN")
    l1.pack(side=TOP,padx=10,pady=10)
    e1=Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="Project")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="12 Marks")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="10 Marks")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="CGPA")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Extra Curricular")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    button1 = Button(frame7, text="Exit", command=lambda :rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)



    button2 = Button(frame7, text="Confirm",command=functools.partial(enter,e1,e2,e3,e4,e5,e6,frame8))
    button2.pack(side=RIGHT, padx=10, pady=10)



def enterCol(e1,e2,e3,e4,e5,e6,e7,e8,frame8):
    try:
        e1 = int(e1.get())
        e2 = e2.get()
        e3 = e3.get()
        e4 = int(e4.get())
        e5 = e5.get()
        e6 = e6.get()
        e7=int(e7.get())
        e8=e8.get()
            #print e1, e2, e3, e4, e5, e6,e7,e8
    except ValueError as e:
        print e
    # print traceback.print_exc()
        la = Label(frame8, text=e)
        la.pack(padx=10, pady=10)
    else:
        m = Backend.insertCollege(e1, e2, e3, e4, e5, e6,e7,e8)
        la = Label(frame8, text=m)
        la.pack(padx=10, pady=10)
    #print m
    # finally:


def insCol():
    rootf = Toplevel()
    rootf.title("Insert into College")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame61 = Frame(root)
    frame61.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="CollegeCode")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="CollegeName")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="Address")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="Phone Number")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Contact Info.")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Affiliation")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    l7 = Label(frame61, text="Established")
    l7.pack(side=TOP, padx=10, pady=10)
    e7 = Entry(frame61)
    e7.pack(side=TOP)

    l8 = Label(frame61, text="Name of Logo File")
    l8.pack(side=TOP, padx=10, pady=10)
    e8 = Entry(frame61)
    e8.pack(side=TOP)

    button1 = Button(frame7, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame7, text="Confirm", command=functools.partial(enterCol,e1,e2,e3,e4,e5,e6,e7,e8,frame8))
    button2.pack(side=RIGHT, padx=10, pady=10)

def enterComp(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,frame8):
    try:
        e1 = int(e1.get())
        e2 = e2.get()
        e3 = float(e3.get())
        e4 = e4.get()
        e5 = float(e5.get())
        e6 = e6.get()
        e7 = e7.get()
        e8 = int(e8.get())
        e9=e9.get()
        e10=e10.get()
        #print e1, e2, e3, e4, e5, e6,e7,e8,e9,e10
    except ValueError as e:
        print e
        #print traceback.print_exc()
        la = Label(frame8, text=e)
        la.pack(padx=10, pady=10)
    else:
        m = Backend.insertCompany(e1, e2, e3, e4, e5, e6, e7, e8,e9,e10,frame8)
        la = Label(frame8, text=m)
        la.pack(padx=10, pady=10)
def insComp():
    rootf = Toplevel()
    rootf.title("Insert into Company")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame61 = Frame(root)
    frame61.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame62 = Frame(root)
    frame62.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame63 = Frame(root)
    frame63.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame64 = Frame(root)
    frame64.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame72 = Frame(rootf)
    frame72.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="CompanyId")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="CompanyName")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="Cut-Off")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="Company Profile")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Package")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Job Profile")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    l7 = Label(frame61, text="Company Address")
    l7.pack(side=TOP, padx=10, pady=10)
    e7 = Entry(frame61)
    e7.pack(side=TOP)

    l8 = Label(frame7, text="College Code")
    l8.pack( side=TOP,padx=10, pady=10)
    e8 = Entry(frame7)
    e8.pack(side=TOP)

    l9 = Label(frame7, text="Contact Info")
    l9.pack( side=TOP,padx=10, pady=10)
    e9 = Entry(frame7)
    e9.pack(side=TOP)

    l10 = Label(frame7, text="Logo")
    l10.pack(side=TOP, padx=10, pady=10)
    e10 = Entry(frame7)
    e10.pack(side=TOP)

    button1 = Button(frame72, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame72, text="Confirm",
                     command=functools.partial(enterComp,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,frame8))
    button2.pack(side=RIGHT, padx=10, pady=10)

def enterInt(e1,e2,e3,e4,e5,frame8):
    try:
        e1 = e1.get()
        e2 = e2.get()
        e3 = float(e3.get())
        e4 = e4.get()
        e5 = int(e5.get())
        #e6 = e6.get()
        print e1, e2, e3, e4, e5
    except ValueError as e:
        print e
        # print traceback.print_exc()
        la = Label(frame8, text=e)
        la.pack(padx=10, pady=10)
    else:
        m = Backend.insertInternship(e1, e2, e3, e4, e5)
        la = Label(frame8, text=m)
        la.pack(padx=10, pady=10)
        print m


def insInt():
    rootf = Toplevel()
    rootf.title("Insert into internship")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="USN")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="Profile")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="Duration")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="Company Name")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Conversion")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)


    button1 = Button(frame7, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame7, text="Confirm", command=functools.partial(enterInt, e1, e2, e3, e4, e5, frame8))
    button2.pack(side=RIGHT, padx=10, pady=10)

def EnterStu(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,e11, frame8):
    try:
        e1 = e1.get()
        e2 = e2.get()
        e3 = int(e3.get())
        e4 = e4.get()
        e5 = e5.get()
        e6 = e6.get()
        e7 = e7.get()
        e8 = e8.get()
        e9 = int(e9.get())
        e10 = int(e10.get())
        e11=e11.get()
        # print e1, e2, e3, e4, e5, e6,e7,e8,e9,e10
    except ValueError as e:
        print e
        # print traceback.print_exc()
        la = Label(frame8, text=e)
        la.pack(padx=10, pady=10)
    else:
        m = Backend.insertStudent(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,e11, frame8)
        la = Label(frame8, text=m)
        la.pack(padx=10, pady=10)


def insStu():
    rootf = Toplevel()
    rootf.title("Insert into Student")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame61 = Frame(root)
    frame61.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame62 = Frame(root)
    frame62.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame63 = Frame(root)
    frame63.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame64 = Frame(root)
    frame64.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame72 = Frame(rootf)
    frame72.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="Student Name")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="DOB(yyyy-mm-dd)")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="SEM")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="USN")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Branch")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Contact Info")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    l7 = Label(frame61, text="Parent's Name")
    l7.pack(side=TOP, padx=10, pady=10)
    e7 = Entry(frame61)
    e7.pack(side=TOP)

    l8 = Label(frame7, text="Residential Address")
    l8.pack(side=TOP, padx=10, pady=10)
    e8 = Entry(frame7)
    e8.pack(side=TOP)

    l9 = Label(frame7, text="College Code")
    l9.pack(side=TOP, padx=10, pady=10)
    e9 = Entry(frame7)
    e9.pack(side=TOP)

    l10 = Label(frame7, text="Company Code")
    l10.pack(side=TOP, padx=10, pady=10)
    e10 = Entry(frame7)
    e10.pack(side=TOP)

    l11 = Label(frame7, text="Name Of Photo")
    l11.pack(side=TOP, padx=10, pady=10)
    e11 = Entry(frame7)
    e11.pack(side=TOP)

    button1 = Button(frame72, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame72, text="Confirm",
                     command=functools.partial(someFunc))
    button2.pack(side=RIGHT, padx=10, pady=10)


def insSelection(var):
    n = var.get()
    if n == 1:
        insAca()
    elif n == 2:
        insCol()
    elif n == 3:
        insComp()
    elif n ==4:
        insInt()
    else:
        insStu()

def insert():
    root = Toplevel()

    root.title("Insert")

    frame1 = Frame(root)
    frame1.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    label=Label(frame1,text="Select a table to insert into")
    label.pack(side=TOP,padx=10,pady=10)

    n = IntVar()

    radioButton1 = Radiobutton(frame2, text="Academics", variable=n, value=1)
    radioButton1.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="College", variable=n, value=2)
    radioButton2.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton3 = Radiobutton(frame2, text="Company", variable=n, value=3)
    radioButton3.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame2, text="Internship", variable=n, value=4)
    radioButton4.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame2, text="Student", variable=n, value=5)
    radioButton4.pack(side=LEFT, padx=10, pady=10, anchor=W)

    button1 = Button(frame3, text="Back")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: root.destroy())

    button2 = Button(frame3, text="Next")
    button2.pack(side=RIGHT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: insSelection(n))

    # print n.get()

    root.mainloop()
    return n.get()

def updateAca(l1,e1,l2,e2,l3,e3,l4,e4,l5,e5,l6,e6):
    for i,j in zip( (e2.get(),e3.get(),e4.get(),e5.get(),e6.get()),(l2,l3,l4,l5,l6)):
        if i!="":
            Backend.updateAcademics(e1.get(),j,i)

def updAca():
    rootf = Toplevel()
    rootf.title("Insert into academics")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="USN")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="Project")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="12 Marks")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="10 Marks")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="CGPA")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Extra Curricular")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    button1 = Button(frame7, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    #eArr={e1,e2,e3,e4,e5,e6}
    #print eArr
    button2 = Button(frame7, text="Confirm", command=functools.partial(updateAca,"USN",e1,"project",e2,"12Marks",e3,"10Marks",e4,"cgpa",e5,"extraCurricular",e6))
    button2.pack(side=RIGHT, padx=10, pady=10)




def updCol():
    rootf = Toplevel()
    rootf.title("Insert into College")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame61 = Frame(root)
    frame61.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="CollegeCode")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="CollegeName")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="Address")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="Phone Number")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Contact Info.")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Affiliation")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    l7 = Label(frame61, text="Established")
    l7.pack(side=TOP, padx=10, pady=10)
    e7 = Entry(frame61)
    e7.pack(side=TOP)

    l8 = Label(frame61, text="Name of Logo File")
    l8.pack(side=TOP, padx=10, pady=10)
    e8 = Entry(frame61)
    e8.pack(side=TOP)

    button1 = Button(frame7, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame7, text="Confirm",
                     command=functools.partial(someFunc))
    button2.pack(side=RIGHT, padx=10, pady=10)
def updComp():
    rootf = Toplevel()
    rootf.title("Insert into Company")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame61 = Frame(root)
    frame61.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame62 = Frame(root)
    frame62.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame63 = Frame(root)
    frame63.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame64 = Frame(root)
    frame64.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame72 = Frame(rootf)
    frame72.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="CompanyId")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="CompanyName")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="Cut-Off")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="Company Profile")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Package")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Job Profile")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    l7 = Label(frame61, text="Company Address")
    l7.pack(side=TOP, padx=10, pady=10)
    e7 = Entry(frame61)
    e7.pack(side=TOP)

    l8 = Label(frame7, text="College Code")
    l8.pack(side=TOP, padx=10, pady=10)
    e8 = Entry(frame7)
    e8.pack(side=TOP)

    l9 = Label(frame7, text="Contact Info")
    l9.pack(side=TOP, padx=10, pady=10)
    e9 = Entry(frame7)
    e9.pack(side=TOP)

    l10 = Label(frame7, text="Logo")
    l10.pack(side=TOP, padx=10, pady=10)
    e10 = Entry(frame7)
    e10.pack(side=TOP)

    button1 = Button(frame72, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame72, text="Confirm",
                     command=functools.partial(someFunc))
    button2.pack(side=RIGHT, padx=10, pady=10)

def updInt():
    rootf = Toplevel()
    rootf.title("Insert into internship")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="USN")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="Profile")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="Duration")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="Company Name")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Conversion")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    button1 = Button(frame7, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame7, text="Confirm", command=functools.partial(someFunc))
    button2.pack(side=RIGHT, padx=10, pady=10)
def updStu():
    rootf = Toplevel()
    rootf.title("Insert into Student")

    root = Frame(rootf)
    root.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame6 = Frame(root)
    frame6.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame61 = Frame(root)
    frame61.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame62 = Frame(root)
    frame62.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame63 = Frame(root)
    frame63.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame64 = Frame(root)
    frame64.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame7 = Frame(rootf)
    frame7.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame72 = Frame(rootf)
    frame72.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame8 = Frame(rootf)
    frame8.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    l1 = Label(frame1, text="Student Name")
    l1.pack(side=TOP, padx=10, pady=10)
    e1 = Entry(frame1)
    e1.pack(side=TOP)

    l2 = Label(frame2, text="DOB(yyyy-mm-dd)")
    l2.pack(side=TOP, padx=10, pady=10)
    e2 = Entry(frame2)
    e2.pack(side=TOP)

    l3 = Label(frame3, text="SEM")
    l3.pack(side=TOP, padx=10, pady=10)
    e3 = Entry(frame3)
    e3.pack(side=TOP)

    l4 = Label(frame4, text="USN")
    l4.pack(side=TOP, padx=10, pady=10)
    e4 = Entry(frame4)
    e4.pack(side=TOP)

    l5 = Label(frame5, text="Branch")
    l5.pack(side=TOP, padx=10, pady=10)
    e5 = Entry(frame5)
    e5.pack(side=TOP)

    l6 = Label(frame6, text="Contact Info")
    l6.pack(side=TOP, padx=10, pady=10)
    e6 = Entry(frame6)
    e6.pack(side=TOP)

    l7 = Label(frame61, text="Parent's Name")
    l7.pack(side=TOP, padx=10, pady=10)
    e7 = Entry(frame61)
    e7.pack(side=TOP)

    l8 = Label(frame7, text="Residential Address")
    l8.pack(side=TOP, padx=10, pady=10)
    e8 = Entry(frame7)
    e8.pack(side=TOP)

    l9 = Label(frame7, text="College Code")
    l9.pack(side=TOP, padx=10, pady=10)
    e9 = Entry(frame7)
    e9.pack(side=TOP)

    l10 = Label(frame7, text="Company Code")
    l10.pack(side=TOP, padx=10, pady=10)
    e10 = Entry(frame7)
    e10.pack(side=TOP)

    l11 = Label(frame7, text="Name Of Photo")
    l11.pack(side=TOP, padx=10, pady=10)
    e11 = Entry(frame7)
    e11.pack(side=TOP)

    button1 = Button(frame72, text="Exit", command=lambda: rootf.destroy())
    button1.pack(side=LEFT, padx=10, pady=10)

    button2 = Button(frame72, text="Confirm",
                     command=functools.partial(someFunc))
    button2.pack(side=RIGHT, padx=10, pady=10)


def updSelection(var):
    n = var.get()
    if n == 1:
        updAca()
    elif n == 2:
        updCol()
    elif n == 3:
        updComp()
    elif n == 4:
        updInt()
    else:
        updStu()

def update():
    root = Toplevel()

    root.title("Update")

    frame1 = Frame(root)
    frame1.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame3 = Frame(root)
    frame3.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    label = Label(frame1, text="Select a table to Update")
    label.pack(side=TOP, padx=10, pady=10)

    n = IntVar()

    radioButton1 = Radiobutton(frame2, text="Academics", variable=n, value=1)
    radioButton1.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="College", variable=n, value=2)
    radioButton2.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton3 = Radiobutton(frame2, text="Company", variable=n, value=3)
    radioButton3.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame2, text="Internship", variable=n, value=4)
    radioButton4.pack(side=LEFT, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame2, text="Student", variable=n, value=5)
    radioButton4.pack(side=LEFT, padx=10, pady=10, anchor=W)

    button1 = Button(frame3, text="Back")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: root.destroy())

    button2 = Button(frame3, text="Next")
    button2.pack(side=RIGHT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: updSelection(n))

    # print n.get()

    root.mainloop()
    return n.get()







#DISPLAY PART
def displayCollegeDetails(name):
    root = Toplevel()
    collegeDetails = Backend.collegeDetails(name)
    text = "Details of " + name +" College"
    root.title(text)
    t = "College Code\t\tCollege Name\t\tAddress\t\tPhone Number\t\tContact Info.\t\tAffiliation\t\tYear of est."
    s = ""
    tl = t.split("\t\t")
    frame1 = Frame(root)
    frame1.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
    frameArr = []
    for i, j in zip(collegeDetails[0], tl):
        frame = Frame(frame1)
        frame.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(Frame(frame))
        label2 = Label(frame, text=str(j) + "\n" + str(i))
        label2.pack(side=TOP, padx=10, pady=10)


def someFunc():
    pass


def displayStudentDetails(name):
    root=Toplevel()
    studentDetails=Backend.studentDetails(name)
    text="Details of " + name
    root.title(text)
    t= "Name\t\tDOB\t\tSemester\t\tUSN\t\tBranch\t\tContact Number\t\tParent's Name\t\tAddress\t\tCollege Code\t\tCompany Code"
    s=""
    tl=t.split("\t\t")
    frame1 = Frame(root)
    frame1.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
    frameArr=[]
    for i,j in zip(studentDetails[0],tl):
        frame=Frame(frame1)
        frame.pack(side=LEFT , fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(Frame(frame))
        label2 = Label(frame, text=str(j)+"\n"+str(i))
        label2.pack(side=TOP, padx=10, pady=10)

def displayAcademicDetails(name):
    root = Toplevel()
    collegeDetails = Backend.academicDetails(name)
    text = "Academic and Internship Details of " + name
    root.title(text)
    t = "USN\t\tProject Title\t\tClass 12 Percentage\t\tClass 10 Percentage\t\tCGPA\t\tExtra Curricular Activities"
    s = ""
    tl = t.split("\t\t")
    frame1 = Frame(root)
    frame1.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
    frameArr = []
    label = Label(frame1, text="Academic Details")
    label.pack(side=TOP, padx=10, pady=10)
    for i, j in zip(collegeDetails[0], tl):
        frame = Frame(frame1)
        frame.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(Frame(frame))
        label2 = Label(frame, text=str(j) + "\n" + str(i))
        label2.pack(side=TOP, padx=10, pady=10)

    internshipDetails = Backend.internshipDetails(name)
    t2 = "USN\t\tWork Profile\t\tDuration of Internship\t\tName of the company\t\tConverted to Job\t\tReport"
    s = ""
    tl2 = t2.split("\t\t")
    frame2 = Frame(root)
    frame2.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
    frameArr2 = []
    labeL = Label(frame2, text="Internship Details")
    labeL.pack(side=TOP, padx=10, pady=10)
    for i, j in zip(internshipDetails[0], tl2):
        frame = Frame(frame2)
        frame.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr2.append(Frame(frame))
        stri=str(i)
        if stri=="0":
            stri="NO"
        elif stri=="1":
            stri=YES
        else:
            stri=str(i)

        label2 = Label(frame, text=str(j) + "\n" + stri)
        label2.pack(side=TOP, padx=10, pady=10)


def displayCompanyStudents(name):
    root = Toplevel()
    frame1 = Frame(root)
    text = "Students recruited in " + name
    root.title(text)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameButtonArr = []
    photoButtonArr = []
    frameArr=[]
    name, logo = Backend.studentInCompany(name)

    for i, j in zip(name, logo):
        # buttonClass1 = Creation.MakeButton(frame1, i, someFunc())
        # button1 = buttonClass1.makeB()

        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        frame2 = Frame(frame)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1 = Button(frame1, text=i, command=functools.partial(displayAcademicDetails,i))
        button1.pack(side=TOP,anchor="w", padx=10, pady=10)
        nameButtonArr.append(button1)

        # buttonClass2 = Creation.MakeButton(frame2, j, someFunc())
        # button2 = buttonClass2.makeB()

        path2 = j+".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, image=image, command=functools.partial(displayStudentDetails,i))
        button2.image = image
        button2.pack(side=TOP,anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        photoButtonArr.append(button2)


def displayCompanyDetails(name):
    companyDetails = Backend.companyDetails(name)

    root = Toplevel()
    text = "Details of " + name
    root.title(text)
    t = "Company Code\t\tName\t\tCutoff\t\tCompany Profile\t\tPackage\t\tJob Profile\t\tAddress\t\tCollege Code\t\tContact Info."
    s = ""
    tl = t.split("\t\t")
    frame1 = Frame(root)
    frame1.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
    frameArr = []
    for i, j in zip(companyDetails[0], tl):
        frame = Frame(frame1)
        frame.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(Frame(frame))
        label2 = Label(frame, text=str(j) + "\n" + str(i))
        label2.pack(side=TOP, padx=10, pady=10)

def displayCollegeCompanies(name):
    root =Toplevel()

    #rootFrame=ScrolledWindow(root,scrollbar=Y)
    #rootFrame.pack(fill=BOTH,expand=True)
    #frame1 = Frame(canvas)
    text="Companies recruiting from "+ name
    root.title(text)
    #frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=10)

    #frame2 = Frame(canvas)
    #frame2.pack(side=RIGHT, fill=BOTH, expand=True,  padx=10)

    nameButtonArr = []
    logoButtonArr = []
    frameArr=[]
    name, logo = Backend.showCompany(name)

    for i, j in zip(name, logo):
        #buttonClass1 = Creation.MakeButton(frame1, i, someFunc())
        #button1 = buttonClass1.makeB()
        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        frame2 = Frame(frame)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1=Button(frame1,text=i,command=functools.partial(displayCompanyStudents,i))
        button1.pack(side=TOP,anchor="w", padx=10, pady=10)
        nameButtonArr.append(button1)

        path2 = j + ".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2=Button(frame2,image=image,command=functools.partial(displayCompanyDetails,i))
        button2.image = image
        button2.pack(side=TOP,anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        logoButtonArr.append(button2)

def collegeDisplay():
    name,logo=Backend.showCollege()

    root=Toplevel()
    root.title("College Details")
    #frame1 = Frame(root)
    #frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    #frame2 = Frame(root)
    #frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameButtonArr=[]
    logoButtonArr=[]
    frameArr=[]

    for i,j in zip(name,logo):
        #buttonClass1=Creation.MakeButton(frame1,i)
        #button1=buttonClass1.makeB()
        #button1.bind("<Button-1>",lambda event:displayCollegeCompanies(i))

        # frame Create for 1

        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1 = Button(frame1, text=i, command=functools.partial(displayCollegeCompanies, i))
        button1.pack(side=TOP,anchor="w", padx=10, pady=10)


        nameButtonArr.append(button1)

        frame2 = Frame(frame)
        frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        path2 = j + ".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, image=image, command=functools.partial(displayCollegeDetails, i))
        button2.image=image
        button2.pack(side=TOP,anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        logoButtonArr.append(button2)

    root.mainloop()

def studentInBranch(cname,bname):
    print cname
    name,photo=Backend.showStudentInBranch(cname,str(bname))
    root = Toplevel()
    frame1 = Frame(root)
    text = "Students recruited from " + bname+" branch"
    root.title(text)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameButtonArr = []
    photoButtonArr = []
    frameArr = []
    for i, j in zip(name, photo):
        # buttonClass1 = Creation.MakeButton(frame1, i, someFunc())
        # button1 = buttonClass1.makeB()

        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        frame2 = Frame(frame)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1 = Button(frame1, text=i, command=functools.partial(displayAcademicDetails, i))
        button1.pack(side=TOP, anchor="w", padx=10, pady=10)
        nameButtonArr.append(button1)

        # buttonClass2 = Creation.MakeButton(frame2, j, someFunc())
        # button2 = buttonClass2.makeB()

        path2 = j + ".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, image=image, command=functools.partial(displayStudentDetails, i))
        button2.image = image
        button2.pack(side=TOP, anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        photoButtonArr.append(button2)


def branchInCollege(cname):
    name, count = Backend.showBranch(cname)
    root = Toplevel()
    root.title("Branchwise Placement Details")

    nameButtonArr = []
    logoButtonArr = []
    frameArr = []

    frame0 = Frame(root)
    frame0.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    la = Label(frame0, text="Branchwise Placement")
    la.pack(side=TOP)
    print name, count
    for i, j in zip(name, count):
        frame = Frame(frame0)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        label1=Label(frame1, text=i)
        label1.pack(side=TOP, anchor="w", padx=10, pady=10)

        nameButtonArr.append(label1)

        frame2 = Frame(frame)
        frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        # path2 = j + ".jpg"
        # image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, text=j, command=functools.partial(studentInBranch,cname,str(i)))
        # button2.image = image
        button2.pack(side=TOP, anchor="e", padx=10, pady=10)
        # button2.config(height=50, width=50)
        logoButtonArr.append(button2)

    root.mainloop()

def branchDisplay():
    name, logo = Backend.showCollege()

    root = Toplevel()
    root.title("College Details")
    # frame1 = Frame(root)
    # frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    # frame2 = Frame(root)
    # frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameButtonArr = []
    logoButtonArr = []
    frameArr = []

    for i, j in zip(name, logo):
        # buttonClass1=Creation.MakeButton(frame1,i)
        # button1=buttonClass1.makeB()
        # button1.bind("<Button-1>",lambda event:displayCollegeCompanies(i))

        # frame Create for 1

        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1 = Button(frame1, text=i, command=functools.partial(branchInCollege, i))
        button1.pack(side=TOP, anchor="w", padx=10, pady=10)

        nameButtonArr.append(button1)

        frame2 = Frame(frame)
        frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        path2 = j + ".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, image=image, command=functools.partial(displayCollegeDetails, i))
        button2.image = image
        button2.pack(side=TOP, anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        logoButtonArr.append(button2)

    root.mainloop()

def companyDisplay():
    name,logo=Backend.company()
    root = Toplevel()

    text = "Companies List"
    root.title(text)

    nameButtonArr = []
    logoButtonArr = []
    frameArr = []


    for i, j in zip(name, logo):
        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        frame2 = Frame(frame)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1 = Button(frame1, text=i, command=functools.partial(displayCompanyStudents, i))
        button1.pack(side=TOP, anchor="w", padx=10, pady=10)
        nameButtonArr.append(button1)

        path2 = j + ".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, image=image, command=functools.partial(displayCompanyDetails, i))
        button2.image = image
        button2.pack(side=TOP, anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        logoButtonArr.append(button2)


def companyCategory(prof):
    root=Toplevel()
    text=prof+" Companies"
    root.title(text)
    print prof

    name,logo=Backend.companyByCategory(prof)

    print name,logo

    nameButtonArr = []
    logoButtonArr = []
    frameArr = []

    for i, j in zip(name , logo):
        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        frame2 = Frame(frame)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        button1 = Button(frame1, text=i, command=functools.partial(displayCompanyStudents, i))
        button1.pack(side=TOP, anchor="w", padx=10, pady=10)
        nameButtonArr.append(button1)

        path2 = j + ".jpg"
        image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, image=image, command=functools.partial(displayCompanyDetails, i))
        button2.image = image
        button2.pack(side=TOP, anchor="e", padx=10, pady=10)
        button2.config(height=50, width=50)
        logoButtonArr.append(button2)


def categoryDisplay():
    category,number=Backend.companyCategory()
    root = Toplevel()

    text = "Company Profile"
    root.title(text)

    nameButtonArr = []
    numButtonArr = []
    frameArr = []

    for i, j in zip(category,number):
        frame = Frame(root)
        frame.pack(side=TOP, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
        frameArr.append(frame)

        frame1 = Frame(frame)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        frame2 = Frame(frame)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

        label1 = Label(frame1, text=i)
        label1.pack(side=TOP, anchor="w", padx=10, pady=10)
        nameButtonArr.append(label1)

        #path2 = j + ".jpg"
        #image = ImageTk.PhotoImage(file=path2)

        button2 = Button(frame2, text=j, command=functools.partial(companyCategory,i))
        #button2.image = image
        button2.pack(side=TOP, anchor="e", padx=10, pady=10)
        #button2.config(height=50, width=50)
        numButtonArr.append(button2)


def display():
    root = Toplevel()

    root.title("Placement Records")

    frame1 = Frame(root)
    frame1.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    label1=Label(frame1,text="View placement records by:")
    label1.pack(fill=BOTH, expand=True, side=LEFT, anchor=W)


    button1 = Button(frame2, text="College")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: collegeDisplay())

    button2=Button(frame2,text="Branch")
    button2.pack(side=LEFT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: branchDisplay())

    button3 = Button(frame2, text="Company")
    button3.pack(side=LEFT, padx=10, pady=10)
    button3.bind("<Button-1>", lambda event: companyDisplay())

    button4 = Button(frame2, text="Company Category")
    button4.pack(side=LEFT, padx=10, pady=10)
    button4.bind("<Button-1>", lambda event: categoryDisplay())

    root.mainloop()


def selection(var):
    n=var.get()
    if n==1:
        insert()
    elif n==2:
        update()
    #elif n==3:
    #    delete()
    else:
        display()
def homeScreen():
    root = Tk()

    root.title("Welcome")

    frame1 = Frame(root)
    frame1.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    #frame3 = Frame(root)
    #frame3.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame4 = Frame(root)
    frame4.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame5 = Frame(root)
    frame5.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    n = IntVar()

    radioButton1 = Radiobutton(frame1, text="Insert", variable=n, value=1)
    radioButton1.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="Update", variable=n, value=2)
    radioButton2.pack(side=TOP, padx=10, pady=10, anchor=W)

    #radioButton3 = Radiobutton(frame3, text="Delete", variable=n, value=3)
    #radioButton3.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame4, text="Display", variable=n, value=4)
    radioButton4.pack(side=TOP, padx=10, pady=10, anchor=W)

    button1 = Button(frame5, text="Exit")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: sys.exit())

    button2 = Button(frame5, text="Next")
    button2.pack(side=RIGHT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: selection(n))

    # print n.get()

    root.mainloop()
    return n.get()


homeScreen()