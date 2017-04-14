import pymysql as p
from Tkinter import *
# Open database connection
db = p.connect("localhost","ankit","ankit123","placementdb",port=12345 )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

def collegeDetails(cn):
    #cn=button.cget("text")
    q1="SELECT * FROM college where College_logo=\""+cn+"\""
    r1=cursor.execute(q1)
    r=cursor.fetchall()
    arrList=[]

    for i in r:
        arrList.append(i)
        print i

    return arrList
    #print arrList

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

