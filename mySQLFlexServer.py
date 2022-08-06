import mysql.connector
from mysql.connector import errorcode

file = open("D:\Programming\SecretKeysandPass\serverTest.txt")
password = file.readline()

config = {
    'host':'practicerelationsdb.mysql.database.azure.com',
    'user':'matsonj2013',
    'password':password,
    'database':'test'
}
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

cursor.execute('''CREATE TABLE highVolume(
                ticker varchar(8) primary key,
                industry varchar(50),
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

conn.commit()