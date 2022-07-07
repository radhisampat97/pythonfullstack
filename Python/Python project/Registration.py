import bcrypt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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


    hashpwd = bcrypt.hashpw(password, bcrypt.gensalt())

    def otp():
        digits = "01234567890"
        OTP=""
        for i in range(6):
            OTP += digits[math.floor(random.random()*10)]
        otp = OTP + "This is your OTP"
        msg= OTP
        return msg


        
    if'@gmail.com' in email:
        print("Valid Email!")
        viewData()
        select_query="select * from user where email = %s"
        cur.execute(select_query, (email,))
        try:
            fname,lname,user_name,emailD,mobileD,password,registration_date = cur.fetchone()
            if emailD is not None:
                print("User already registered")
        except Exception as e:
            if password==confirm_password:
                            
                # Sending email to registered user
                msg = MIMEMultipart()
                msg['From'] = 'radhisampat97@gmail.com'
                msg['To'] = 'radhi23@gmail.com'
                msg['Subject'] = 'simple email in python'
                msg1 = otp()
                message = 'Verification code: {} '.format(msg1)
                msg.attach(MIMEText(message))
                mailserver = smtplib.SMTP('smtp.mailtrap.io',587)
                # identify ourselves to smtp gmail client
                mailserver.ehlo()
                # secure our email with tls encryption
                mailserver.starttls()
                # re-identify ourselves as an encrypted connection
                mailserver.ehlo()

                mailserver.login('8186bc4d47f727', '8cb4e77564841a')

                mailserver.sendmail('radhisampat97@gmail.com','radhi23@gmail.com',msg.as_string())

                mailserver.quit()

                c = 1
                for c in range(1,4):
                    b = input("\nEnter verification code: ")
                    if b == msg1:
                        print("\ncode is correct")
                        insert_query = """insert into user(fname, lname, user_name, email, mobile, password,registration_date)
                                           values (%s,%s,%s,%s,%s,%s,%s)"""
                               
                        user_info = (fname,lname,user_name,email,mobile,hashpwd, registration_date)
                        cur.execute(insert_query, user_info)
                        con.commit()
                        print("Registered successfully")
                        break
                    else:
                        print("Wrong code! Enter Again")
                        c +=1
                        continue
                    if c >= 3:
                        print("3 attempts over! Code expired")
            else:
                print("The password doesnot match.")                   

    else:
        print("Invalid Email")

                
            
    

def viewData():
    select_query = "select * from user;"
    cur.execute(select_query)
    
