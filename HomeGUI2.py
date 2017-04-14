from Tkinter import *
import Backend
import Creation

def insert():
    pass

def update():
    pass

def delete():
    pass

def displayCollegeDetails(name):
    print "College Name:",name


def someFunc():
    pass

def displayCollegeCompanies(name):
    root =Tk()
    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameButtonArr = []
    logoButtonArr = []

    name, logo = Backend.showCompany(name)

    for i, j in zip(name, logo):
        buttonClass1 = Creation.MakeButton(frame1, i, someFunc())
        button1 = buttonClass1.makeB()
        nameButtonArr.append(button1)

        buttonClass2 = Creation.MakeButton(frame2, j, someFunc())
        button2 = buttonClass2.makeB()
        logoButtonArr.append(button2)

def collegeDisplay():
    name,logo=Backend.showCollege()

    root=Tk()

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameButtonArr=[]
    logoButtonArr=[]

    for i,j in zip(name,logo):
        buttonClass1=Creation.MakeButton(frame1,i)
        button1=buttonClass1.makeB()
        button1.bind("<Button-1>",lambda event:displayCollegeCompanies(i))
        nameButtonArr.append(button1)

        buttonClass2 = Creation.MakeButton(frame2, j)
        button2 = buttonClass2.makeB()
        button2.bind("<Button-1>",lambda event:displayCollegeDetails(j))
        logoButtonArr.append(button2)


    root.mainloop()


def branchDisplay():
    pass

def companyDisplay():
    pass

def categoryDisplay():
    pass

def display():
    root = Tk()

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
    elif n==3:
        delete()
    else:
        display()
def homeScreen():
    root = Tk()

    root.title("Welcome")

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

    n = IntVar()

    radioButton1 = Radiobutton(frame1, text="Insert", variable=n, value=1)
    radioButton1.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="Update", variable=n, value=2)
    radioButton2.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton3 = Radiobutton(frame3, text="Delete", variable=n, value=3)
    radioButton3.pack(side=TOP, padx=10, pady=10, anchor=W)

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