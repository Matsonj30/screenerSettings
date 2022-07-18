import pyodbc

#FILE to test basic DB commands in python


server = 'jaredsdb.database.windows.net'
database = 'jaredsdb'
username = 'matsonj2013@gmail.com'
driver= '{SQL Server}'

file = open("D:\Programming\SecretKeysandPass\serverTest.txt")
password = file.readline()

connect = pyodbc.connect('DRIVER={SQL Server};SERVER=jaredsdb.database.windows.net;DATABASE=jaredDateBase;UID=matsonj2013@gmail.com@jaredsdb;PWD='+password) #DATABASE != servername
cursor = connect.cursor() #THIS WORKS

def createTables():
    cursor.execute("DROP TABLE highVolume")
    cursor.execute('''CREATE TABLE highVolume(
                    ticker varchar(8) primary key,
                    industry varchar(30),
                    dateFound varchar(15),
                    volume int,
                    mktCap varchar(10),
                    priceFound float(2),
                    day1 float(2),
                    day2 float(2),
                    day3 float(2),
                    day4 float(2),
                    day5 float(2),
                    day6 float(2),
                    day7 float(2),
                    day8 float(2),
                    day9 float(2),
                    day10 float(2),
                    day11 float(2),
                    day12 float(2),
                    day13 float(2),
                    day14 float(2),
                    changeWhenFound varchar(10),
                    highSinceFound int,
                    upSinceFound BIT
                    )
                    ''')
   
    connect.commit()

def selectElements():
    return

def addToTable(): #we want to do this every day from the finviz screener
#row = cursor.fetchone() TO GET SELECTS
    
    cursor.execute('''INSERT INTO highVolume(ticker, industry, dateFound, volume, mktCap, priceFound
                    VALUES ()
                    )                
                    ''')
createTables()