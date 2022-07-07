import pymysql
import re
import bcrypt

con = pymysql.connect(host="localhost",user="root", password="",
                      database="userdb")

##print(con)
print("Database connected.")
cur = con.cursor()


##For registration
##1. first name
##2. last name
##3. Date
##4. user name
##5. email id
##6. mobile number
##7. password
##8. confirm password
def registration():
##
    insert_query = """insert into user
(fname, lname, user_name, email, mobile, password, confirm_password,registration_date)
values (%s,%s,%s,%s,%s,%s,%s,%s)"""

    

    fname = input("Enter your First name: ")
    lname = input("Enter your Last name: ")
    user_name = input("Enter User Name: ")
    email = input("Enter email id: ")
    mobile = input("Enter mobile number: ")
    password = input("Enter password: ")
    confirm_password = input("Enter Confirm password: ")
    registration_date = input("Enter DOB(yyyy-mm-dd): ")

    password = password.encode()
    confirm_password = confirm_password.encode()

    if'@gmail.com' in email:
        print("Valid Email!")
    else:
        print("Invalid Email")

    hashpwd = bcrypt.hashpw(password, bcrypt.gensalt())
    


    viewData()
##    email = input("Enter email id:")
    select_query="select * from user where email = %s"
    cur.execute(select_query, (email,))
    try:
        fname,lname,user_name,emailD,mobileD,password,registration_date = cur.fetchone()
        if email is not None:
           print("User already registered")
    except Exception as e:
        if password==confirm_password:
            insert_query = """insert into user(fname, lname, user_name, email, mobile, password,registration_date)
                           values (%s,%s,%s,%s,%s,%s,%s)"""
            user_info = (fname,lname,user_name,email,mobile,hashpwd, registration_date)
            cur.execute(insert_query,user_info)
            con.commit()
            print("Successfully registered")
        else:
            print("The password doesnot match.")
        


def login():
    print("Login")
    insert_query = """insert into login (new_email, new_password)
values(%s,%s)"""

    new_email = input("Enter email id: ")
    new_password = input("Enter password: ")

##    new_password = new_password.encode()


    select_query="select * from user where email = %s"
    cur.execute(select_query, (new_email,))

    try:
        fname,lname,user_name,emailD,mobileD,passwordD,registration_date = cur.fetchone()
##        print("Db password: ",passwordD)
##        print("User enter password: ",new_password)
####        try:
####            a= bcrypt.checkpw(new_password, passwordD)
####            print(a)
##        except Exception as e:
##            print("exception after bcrypt")
        if emailD is not None:
            if passwordD == new_password:
                print("Successful Login!")
            else:
                print("Enter correct password")
    except Exception as e:
        print(" Not a registered user! Sign up")
            


    





















##  def __init__(self, id, pas):
##        self.id = id
##        self.pas = pas
##
##    def check(self, id, pas):
##        print self.id
##        if self.id == id and self.pas == pas:
##            print "Login success!"
##
##log = login("admin", "admin")
##log.check(raw_input("Enter Login ID:"),
##          raw_input("Enter password: "))   
##
##
####
####  ##
####    if emailD==email and mobileD==mobile:
##        print("User already exists.")
##    else:
##        insert_query = """insert into user(fname,lname,user_name,email,mobile,password,confirm_password, registration_date)
##                           values (%s,%s,%s,%s,%s,%s,%s,%s)"""
##        cur.execute(insert_query, user_info)
##        print("Successfully registered")
##        con.commit()

##def name_check(fname,lname):
##    
##    if (fname.isalpha() and lname.isalpha()):
##        fname = fname.title()
##        lname = lname.title()
##        print("First Name: ",fname)
##        print("Last Name: ",lname)
##    else:
##        print(" ")
##        
##    name_check(fname, lname)
##
##def mobile_check():
##   if mobile.isdigit() and len(mobile) == 10:
##      print("Mobile number: ", mobile)
##   else:
##      print("Invalid Mobile number")
##   mobile_check()
##
##        
####
##def updateData():
##    viewData()
##    email = input("Which user do you wanna modify:")
##    select_query="select * from user where email = %s"
##    cur.execute(select_query, (email,))
##    fname,lname,user_name,emailD,mobileD,password,registration_date = cur.fetchone()
##
##    if emailD==email and mobileD==mobile:
##        print("User already exists.")
##    else:
##        insert_query = """fname,lname,user_name,email,mobile,password,confirm_password, registration_date"""
##        cur.execute(insert_query, user_info)
##        print("Successfully registered")
##
##    print("""Enter nos that you wanna modify:
##1. First name
##2. Last name
##3. User Name
##4. Email
##5. Mobile
##6. Password
##7. Registration_date""")
##    chstr = input("Enter your choice comma separated")
##    chlst = chstr.split(",")
##    for i in chlst:
##         if int(i)==1:
##             fname = input("Enter first name: ")
##         elif int(i)==2:
##             lname = input("Enter last name: ")
##         elif int(i)==3:
##             user_name = input("Enter user Name: ")
##         elif int(i)==4:
##             email = input("Enter email id: ")
##         elif int(i)==5:
##             mobile = input("Enter mobile number: ")
##         elif int(i) ==6:
##             password = input("Enter password: ")
##         elif int(i)==7:
##             registration_date = input("Enter DOB: ")
##    update_query = """update user set fname = %s, lname =%s,
##username=%s, emailD =%s, mobile =%s, password=%s, registration_date=%s where email = %s"""
##    update_values = (fname,lname,username,emailD,mobile,password,registration_date,email)
##
#

def viewData():
    select_query = "select * from user;"
    cur.execute(select_query)
    

##
##
####length,lower,upper,digit,special_character = 0,0,0,0,0
####
####password = input('Enter the password: ')
####
####if len(password)>= 8:
####    
####
####if length and lower and upper and digit:
####    print('That is a valid password.')
####else:
####    print('That password is not valid.')
##    
while True:
    print("""Enter choice:
1. Login
2. Register
3. Forgot password
4. Quit""")
    ch = int(input("Enter your choice:"))
    if ch ==1:
        login()
    elif ch==2:
        registration()
    elif ch==3:
        forgot_password()
    elif ch==4:
        break
    else:
        print("Enter correct credentials")
con.close()



