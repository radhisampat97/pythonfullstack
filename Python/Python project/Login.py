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
