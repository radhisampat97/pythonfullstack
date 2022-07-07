import pymysql, datetime

con = pymysql.connect(host="localhost",user="root", password="",
                      database="worldcupdb")

##print(con)
print("Database connected.")
cur = con.cursor()

def insertData():
    insert_query = """insert into ttwc
(dateofMatch, Team1Name, Team1Captain, Team2Name, Team2Captain, Location)
values (%s,%s,%s,%s,%s,%s)"""
    insert_values = (input("Enter Match Date:"),
                     input("Team 1 Name:"), input("Captain 1 Name:"),
                     input("Team 2 Name:"), input("Captain 2 Name:"),
                     input("Enter Location:"))

    cur.execute(insert_query, insert_values)
    con.commit()

def updateData():
    viewData()
    srno = input("Which srno do you wanna modify:")
    select_query="select * from ttwc where srno = %s"
    cur.execute(select_query, (srno,))
    srno, dt,t1n,t1c,t2n,t2c,loc,toss,mat = cur.fetchone()
    print("""Enter nos that you wanna modify:
1. Date of Match
2. Team1 Name
3. Team 1 Captain
4. Team 2 Name
5. Team 2 Captain
6. Location
7. Toss Won
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
         elif int(i) ==6:
             loc = input("Enter location:")
         elif int(i)==7:
             toss = input("Enter who won the toss: 1. {} 2. {}".format(t1n, t2n))
         elif int(i)==8:
            mat = input("Enter who won the match: 1. {} 2. {}".format(t1n, t2n))
    update_query = """update ttwc set dateofMatch = %s, team1name =%s,
team1captain=%s, team2name =%s, team2captain=%s, location = %s,
toss_win = %s, match_win = %s where srno = %s;"""
    update_values = (dt, t1n, t1c, t2n, t2c, loc, toss, mat, srno)
    cur.execute(update_query, update_values)
    con.commit()

def deleteData():
    viewData()
    srno = input("Which srno do you wanna delete:")
    select_query="select * from ttwc where srno = %s"
    cur.execute(select_query, (srno,))
    srno, dt,t1n,t1c,t2n,t2c,loc,toss,mat = cur.fetchone()
    print("""Enter nos that you wanna delete:
1. Date of Match
2. Team1 Name
3. Team 1 Captain
4. Team 2 Name
5. Team 2 Captain
6. Location
7. Toss Won
8. Match Won""")
    
    
def viewData():
    select_query = "select * from ttwc;"
    cur.execute(select_query)
    for srno, dt, t1n, t1c, t2n, t2c, loc, toss, mat in cur.fetchall():
        print("{}. {} vs {} on {}".
              format(srno, t1n, t2n, dt.strftime('%d-%b-%Y')))

while True:
    print("""ENter choice:
1. Insert Record
2. Update Record
3. Delete Record
4. View Data
5. Quit""")
    ch = int(input("Enter your choice:"))
    if ch ==1:
        insertData()
    elif ch==2:
        updateData()
    elif ch==3:
        pass
    elif ch==4:
        viewData()
    elif ch == 5:
        break
    else:
        print("Wrong Input")
con.close()

     
