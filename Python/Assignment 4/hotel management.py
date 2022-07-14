import pymysql
import math
import random
import names

# Connection to database 
con = pymysql.connect(host="localhost",user="root", password="",
                      database="hotel_management")


#print(con)
print("Connected to Database.!!")
print()
cur = con.cursor()              # Cursor() method used to retrieve data



##def reservation():
####
##    insert_query = """insert into guest
##(fname, lname, email, mobile)
##values (%s,%s,%s,%s,%s,%s,%s,%s)"""
##
##    fname = input("Enter your First name: ")
##    lname = input("Enter your Last name: ")
##    email = input("Enter email id: ")
##    mobile = input("Enter mobile number: ")


# To add random names in the database

for i in range(50):
    print(names.get_full_name())






##while True:
##    print("*******Welcome to Hotel Taj!!*******")
##    print("""Enter choice:
##1. Reservation
##2. Room Info
##3. Payment
##4. Records
##5. Quit""")
##    ch = int(input("Enter your choice:"))
##    if ch ==1:
##        reservation()
##    elif ch==2:
##        room_info()
##    elif ch==3:
##        payment()
##    elif ch==4:
##        records()
##    elif ch==5:
##        break
##    else:
##        print("Enter correct credentials")
##con.close()

