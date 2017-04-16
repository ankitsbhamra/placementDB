from Tkinter import *
import Backend
import ImageTk
import functools
from Tix import *

#path="Images"
#print path

#Add Images for everything and academic Details of students

def insert():
    pass

def update():
    pass

def delete():
    pass

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