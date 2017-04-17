import pymysql as p
from Tkinter import *
# Open database connection
db = p.connect("localhost","root","Ankit201195","placementdb",port=12345 )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

def collegeDetails(cn):
    #cn=button.cget("text")
    q1="SELECT * FROM college where CollegeName=\""+cn+"\""
    r1=cursor.execute(q1)
    r=cursor.fetchall()
    arrList=[]

    for i in r:
        arrList.append(i)
        print i

    return arrList
    #print arrList

def companyDetails(name):
    q="select *from company where CompanyName=\""+name+"\""
    r1=cursor.execute(q)
    r=cursor.fetchall()
    arrList=[]

    for i in r:
        arrList.append(i)
        print i

    return arrList

def internshipDetails(name):
    q = "select * from internship where usn in (select usn from Student where StudentName=\"" + name + "\")"
    r1 = cursor.execute(q)
    r = cursor.fetchall()
    arrList = []

    for i in r:
        arrList.append(i)
        # print i
    print r
    return arrList


def academicDetails(name):
    q="select * from academics where usn in (select usn from Student where StudentName=\""+name+"\")"
    r1=cursor.execute(q)
    r=cursor.fetchall()
    arrList=[]

    for i in r:
        arrList.append(i)
        #print i
    print r
    return arrList

def studentDetails(name):
    q="Select * from Student where StudentName = \""+name+"\""
    r1=cursor.execute(q)
    r=cursor.fetchall()
    arrList=[]
    for i in r:
        arrList.append(i)
        print i

    return arrList



def studentInCompany(name):
    q1="select StudentName,photo from student where companyCode in (select CompanyId from company where CompanyName=\""+name+" \")"
    r1 = cursor.execute(q1)
    r = cursor.fetchall()
    a1 = []
    a2 = []
    for i in r:
        print i
        a1.append(i[0])
        a2.append(i[1])
    print a1, a2
    return a1, a2


def showBranch(name):
    q1="Select branch from student where CollegeCode =(Select CollegeCode from college where CollegeName=\""+name+"\")"
    r1=cursor.execute(q1)
    r=cursor.fetchall()
    d={}
    for i in r:
        for j in i:
            if j in d:
                d[j]+=1
            else:
                d[j]=1

    print d.keys(),d.values()
    return d.keys(),d.values()

def companyByCategory(prof):
    q="Select CompanyName,Logo from company where CompanyProfile = \""+prof+"\""
    r1 = cursor.execute(q)
    r = cursor.fetchall()
    nameL=[]
    logoL=[]
    for i in r:
        nameL.append(i[0])
        logoL.append(i[1])
    print nameL,logoL
    return nameL,logoL

def companyCategory():
    q="Select CompanyProfile from company"
    r1 = cursor.execute(q)
    r = cursor.fetchall()
    d = {}
    for i in r:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1

    print d.keys(), d.values()
    return d.keys(), d.values()


def showStudentInBranch(cname,bname):
    q="select StudentName,photo from student where branch=\""+bname+"\" and  CollegeCode=(Select CollegeCode from college where CollegeName= \""+cname+"\")"
    r1=cursor.execute(q)
    r=cursor.fetchall()
    name=[]
    pic=[]
    for i in r:
        #for j in i:
        name.append(i[0])
        pic.append(i[1])
    return name,pic
def showCompany(cn):
    #cn=button.cget("text")
    q1="select CompanyName,logo from company where CollegeCode in (select CollegeCode from college where CollegeName=\""+cn+"\")"
    print q1
    r1=cursor.execute(q1)
    r=cursor.fetchall()
    a1 = []
    a2 = []
    for i in r:
        print i
        a1.append(i[0])
        a2.append(i[1])
    print a1,a2
    return a1, a2

def company():
    q="Select CompanyName,logo from company "
    r1=cursor.execute(q)
    r=cursor.fetchall()
    a1 = []
    a2 = []
    for i in r:
        print i
        a1.append(i[0])
        a2.append(i[1])
    print a1, a2
    return a1, a2

def showCollege():
    q1="select CollegeName,College_logo from college"
    r1=cursor.execute(q1)
    r=cursor.fetchall()
    a1=[]
    a2=[]
    for i in r:
        a1.append(i[0])
        a2.append(i[1])
    return a1,a2

#showStudentInBranch("SJCE","is")

#companyByCategory("Mass")


def insertAcademics(e1,e2,e3,e4,e5,e6):
    e3=str(e3)
    e4=str(e4)
    e5=str(e5)
    try:
        q="INSERT INTO academics(usn,project,12Marks,10Marks,cgpa,extraCurricular) VALUES(\""+e1+"\",\""+e2+"\","+e3+","+e4+","+e5+",\""+e6+"\")"
        r1=cursor.execute(q)
        r=cursor.fetchall()
        return r
    except Exception as e:
        return e

def insertCollege(e1,e2,e3,e4,e5,e6,e7,e8):
    e1=str(e1)
    e4 = str(e4)
    e7 = str(e7)
    try:
        q="INSERT INTO college(CollegeCode,CollegeName,address,PhoneNumber,ContactInfo,affiliation,established,College_logo) VALUES("+e1+",\""+e2+"\",\""+e3+"\","+e4+",\""+e5+"\",\""+e6+"\","+e7+",\""+e8+"\")"
        r1=cursor.execute(q)
        r=cursor.fetchall()
        return r
    except Exception as e:
        return e

def insertCompany(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,frame8):

    e1=str(e1)
    e3=str(e3)
    e5=str(e5)
    e8=str(e8)
    try:
        q="INSERT INTO company (CompanyId,CompanyName,CutOff,CompanyProfile,package,jobProfile,CompanyAddress,CollegeCode,ContactInfo,Logo) VALUES("+e1+",\""+e2+"\","+e3+",\""+e4+"\","+e5+",\""+e6+"\",\""+e7+"\","+e8+",\""+e9+"\",\""+e10+"\")"
        r1=cursor.execute(q)
        r=cursor.fetchall()
        return r
    except Exception as e:
        return e

def insertInternship(e1,e2,e3,e4,e5):
    e3=str(e3)
    e5=str(e5)
    try:
        q="INSERT INTO internship VALUES(\""+e1+"\",\""+e2+"\","+e3+",\""+e4+"\","+e5+",\"None\")"
        r1=cursor.execute(q)
        r=cursor.fetchall()
        return r
    except Exception as e:
        return e

def insertStudent(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,frame8):
    e3=str(e3)
    e9=str(e9)
    e10=str(e10)

    try:
        q = "INSERT INTO college(CollegeCode,CollegeName,address,PhoneNumber,ContactInfo,affiliation,established,College_logo) VALUES(\"" + e1 + "\",\"" + e2 + "\"," + e3 + ",\"" + e4 + "\",\"" + e5 + "\",\"" + e6 + "\",\"" + e7 + "\",\"" + e8 + "\","+e9+","+e10+",\""+e11+"\")"
        r1 = cursor.execute(q)
        r = cursor.fetchall()
        return r
    except Exception as e:
        return e

def updateAcademics(e1,j,i):
        q="UPDATE academics set "+j+"= \""+i+"\" where USN=\""+e1+"\""
        print q
        r1=cursor.execute(q)
        r=cursor.fetchall()
        return r
