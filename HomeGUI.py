from Tkinter import *
import Backend
import Creation


def insertSelection(n):
    pass

def insert():
    root = Tk()

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

    frame6 = Frame(root)
    frame6.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    n = IntVar()

    radioButton1 = Radiobutton(frame1, text="College", variable=n, value=1)
    radioButton1.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="Student", variable=n, value=2)
    radioButton2.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton3 = Radiobutton(frame3, text="Company", variable=n, value=3)
    radioButton3.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame4, text="Academics", variable=n, value=4)
    radioButton4.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton5 = Radiobutton(frame5, text="Internship", variable=n, value=5)
    radioButton5.pack(side=TOP, padx=10, pady=10, anchor=W)

    button1 = Button(frame6, text="Exit")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: root.destroy)

    button2 = Button(frame6, text="Next")
    button2.pack(side=RIGHT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: insertSelection(n))

    # print n.get()

    root.mainloop()
def updateSelection(n):
    pass

def update():

    root = Tk()

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

    frame6 = Frame(root)
    frame6.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    n = IntVar()

    radioButton1 = Radiobutton(frame1, text="College", variable=n, value=1)
    radioButton1.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="Student", variable=n, value=2)
    radioButton2.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton3 = Radiobutton(frame3, text="Company", variable=n, value=3)
    radioButton3.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame4, text="Academics", variable=n, value=4)
    radioButton4.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton5 = Radiobutton(frame5, text="Internship", variable=n, value=5)
    radioButton5.pack(side=TOP, padx=10, pady=10, anchor=W)

    button1 = Button(frame6, text="Exit")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: root.destroy)

    button2 = Button(frame6, text="Next")
    button2.pack(side=RIGHT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: updateSelection(n))

    # print n.get()

    root.mainloop()

def deleteSelection(n):
    pass

def delete():

    root = Tk()

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

    frame6 = Frame(root)
    frame6.pack(fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    n = IntVar()

    radioButton1 = Radiobutton(frame1, text="College", variable=n, value=1)
    radioButton1.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton2 = Radiobutton(frame2, text="Student", variable=n, value=2)
    radioButton2.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton3 = Radiobutton(frame3, text="Company", variable=n, value=3)
    radioButton3.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton4 = Radiobutton(frame4, text="Academics", variable=n, value=4)
    radioButton4.pack(side=TOP, padx=10, pady=10, anchor=W)

    radioButton5 = Radiobutton(frame5, text="Internship", variable=n, value=5)
    radioButton5.pack(side=TOP, padx=10, pady=10, anchor=W)

    button1 = Button(frame6, text="Exit")
    button1.pack(side=LEFT, padx=10, pady=10)
    button1.bind("<Button-1>", lambda event: root.destroy)

    button2 = Button(frame6, text="Next")
    button2.pack(side=RIGHT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: deleteSelection(n))

    # print n.get()

    root.mainloop()

def showCompanyDetails(details):

    root = Tk()

    print details

    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameB = []
    logoB = []

    # scL2=["F:\csi\\randoms\imgres.jpg","F:\csi\\randoms\NIE Mysore.jpg"]

    scL1, scL2 = Backend.showCompany(details)

    for i, j in zip(scL1, scL2):
        #make Label here only including pack and biind and try
        l=Creation.MakeButton(frame1,j,showCollegeDetails())
        nameB.append(l)
        b=Creation.MakeButton(frame1,i,showCompanyDetails())
        logoB.append(b)
    '''
    for i, j in zip(nameB, logoB):
        i.pack(side=TOP, padx=10, pady=10)
        i.bind("<Button-1>", lambda event: showCollegeDetails())

        j.pack(side=TOP, padx=10, pady=10)
        j.bind("<Button-1>", lambda event: showCompanyDetails())
    '''

    root.title()

    root.mainloop()
def showCollegeDetails(name):
    mainList=Backend.collegeDetails(name)

    root = Tk()
    root.title("Additional College Details")
    frame1 = Frame(root)
    frame1.pack(side=LEFT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    arrList=[]

    for i in mainList:
        s=""
        for j in i:
            s=s+str(j)+"\t"
        arrList.append(Label(frame1, text=s))

    for i in arrList:
        i.pack(side=TOP, padx=10, pady=10)
        i.bind("<Button-1>", lambda event: showCollegeDetails())

    root.mainloop()

def updateSelection(n):
    root = Tk()

    root.title("Select College")

    frame1 = Frame(root)
    frame1.pack(side=LEFT,fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    frame2 = Frame(root)
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)

    nameB=[]
    logoB=[]

    #scL2=["F:\csi\\randoms\imgres.jpg","F:\csi\\randoms\NIE Mysore.jpg"]

    scL1,scL2=Backend.showCollege()

    for i,j in zip(scL1,scL2):

        #make Label here only including pack and biind and try
        l=Creation.MakeButton(frame1,j,showCollegeDetails())
        nameB.append(l)
        b=Creation.MakeButton(frame1,i,showCompanyDetails())
        logoB.append(b)

    '''
    for i in range (0,len(nameB)):
        print "in for"
        nameB[i].pack(side=TOP, padx=10, pady=10)
        nameB[i].bind("<Button-1>", lambda event: showCollegeDetails(nameB[i]))

        logoB[i].pack(side=TOP, padx=10, pady=10)
        print logoB[i].cget("text")
        logoB[i].bind("<Button-1>", lambda event: showCompanyDetails(logoB[i]))
    '''
    root.mainloop()

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
    button1.bind("<Button-1>", lambda event: updateSelection(1))

    button2 = Button(frame2, text="Branch")
    button2.pack(side=LEFT, padx=10, pady=10)
    button2.bind("<Button-1>", lambda event: updateSelection(2))

    button3 = Button(frame2, text="Company")
    button3.pack(side=LEFT, padx=10, pady=10)
    button3.bind("<Button-1>", lambda event: updateSelection(3))

    button4 = Button(frame2, text="Company Category")
    button4.pack(side=LEFT, padx=10, pady=10)
    button4.bind("<Button-1>", lambda event: updateSelection(4))

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