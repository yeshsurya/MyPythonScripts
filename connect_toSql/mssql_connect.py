import pyodbc
server = 'Server-Name'
database = 'DB-Name'
username = 'sa'
password = 'abc-123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("select top 10 * from Action;")
row = cursor.fetchone()
while row:
    print (row[0],row[1])
    row = cursor.fetchone()
