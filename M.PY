import sqlite3

# Create connection
connect= sqlite3.connect("Movie1.db")
cur=connect.cursor()

# Create a table 

com1="""CREATE TABLE IF NOT EXISTS
MOVIES( "MOVIENAME" varchar2(20),
    "ACTORNAME" varchar2(20),
    "ACTRESSNAME" varchar2(20),
    "YEAR" number(4),
    "DIRNAME" varchar(20))"""

cur.execute(com1)

print("Table MOVIE Created!!")
print(".............................................................")

# Insert values into the table 
cur.execute("INSERT INTO MOVIES VALUES('SHERSHAA','SID','KIARA',2019,'BATRA')")
cur.execute("INSERT INTO MOVIES VALUES('DHOOM3','AMIR','KAT',2016,'KARAH JOHAR')")
cur.execute("INSERT INTO MOVIES VALUES('RAAZI','VICKY','ALIA BHAT',2018,'MEGHANA GULZAR')")
cur.execute("INSERT INTO MOVIES VALUES('KRISH','HRITIK ROSHAN','PRIYANKA',2008,'ANUSHA')")
cur.execute("INSERT INTO MOVIES VALUES('MOJENJO DARO','HRITIK ROSHAN','ANUSHKA SHARMA',2014,'RAJKUMAR HIRANI')")
cur.execute("INSERT INTO MOVIES VALUES('3 IDIOTS','AAMIR KHAN','KAREENA',2009,'RAJKUMAR HIRANI')")
cur.execute("INSERT INTO MOVIES VALUES('STREET DANCER','VARUN','SHARDHA',2019,'REMO D ')")
cur.execute("INSERT INTO MOVIES VALUES('GANGUBAI','VARUN','AALIYA',2017,'KARAN JOHAR')")

# Query

cur.execute("SELECT * FROM MOVIES")
r=cur.fetchall()
print("Movie     Actor      Actress     Year     Director")
print("---------------------------------------------------")
for i in range(len(r)):
    print(str(r[i][0])+"  ||  "+str(r[i][1])+"  ||  "+str(r[i][2])+"  ||  "+str(r[i][3])+"  ||  "+str(r[i][4]))
    print(".............................................................")

# other Queries
print("The movies acted by varun are:::::")
print("----------------------------------------")
cur.execute("SELECT MOVIENAME,ACTORNAME,ACTRESSNAME,YEAR,DIRNAME FROM MOVIES WHERE ACTORNAME='VARUN'")

result=cur.fetchall()
print("Movie     Actor      Actress     Year     Director")
print("---------------------------------------------------")
for i in range(len(result)):
    print(str(result[i][0])+"  |  "+str(result[i][1])+"  |  "+str(result[i][2])+"  |  "+str(result[i][3])+"  |  "+str(result[i][4]))
    print(".............................................................")