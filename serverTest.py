import pyodbc
server = 'jaredsdb.database.windows.net'
database = 'jaredsdb'
username = 'matsonj2013@gmail.com'
driver= '{SQL Server}'

file = open("D:\Programming\SecretKeysandPass\serverTest.txt")
password = file.readline()

connect = pyodbc.connect('DRIVER={SQL Server};SERVER=jaredsdb.database.windows.net;DATABASE=jaredDateBase;UID=matsonj2013@gmail.com@jaredsdb;PWD='+password) #DATABASE != servername
cursor = connect.cursor() #THIS WORKS
cursor.execute("SELECT * FROM Persons")
row = cursor.fetchone()     
print(row)