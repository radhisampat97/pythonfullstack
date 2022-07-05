import pymysql, datatime

con = pymysql.connect(host="localhost",user="root", password="",
                      database="worldcupdb")

##print(con)
print("Database connected.")
cur = con.sursor()

def insertData():
    insert_query = """insert into ttwc
(dateofMatch, Team1Name, Team1Captain, Team2Name, Team2Captain, Location)
values (%s,%s,%s,%s,%s,%s)"""
    insert_values = (input("Enter Match Date:")
                     input("Team 1 Name:"), input("Captain 1 Name:")
                     input("Team 2 Name:"), input("Captain 2 Name:")
                     input("Enter Location:"))

    cur.execute(insert_query, insert_values)
    con.commit()

def updateData():
    viewData()
    srno = input("Which srno do you wanna 

















8. Match Won""")
     chstr = input("Enter your choice comma separated")
     chlst = chstr.split(",")
     for i in chlst:
         if int(i)==1:
             dt = input("Match Date:")
         elif int(i)==2:
             tln = input("Team 1 Name:")
         elif int(i)==3:
             tlc = input("Team 1 Captain Name:")
         elif int(i)==4:
             t2n = input("Team 2 Name:")
         elif int(i)==5:
             t2c = input("Team 2 Captain Name:")
             
     
