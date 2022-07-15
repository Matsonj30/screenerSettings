import pyodbc
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
                    priceFound int,
                    day1 int,
                    day2 int,
                    day3 int,
                    day4 int,
                    day5 int,
                    day6 int,
                    day7 int,
                    day8 int,
                    day9 int,
                    day10 int,
                    day11 int,
                    day12 int,
                    day13 int,
                    day14 int,
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