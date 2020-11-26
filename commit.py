import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DESKTOP-DQHM2SB;'
                      'DATABASE=WideWorldImporters-Full;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute('Select * from Fourniseur')
for row in cursor:
    print(row)

cursor.execute("""UPDATE Fourniseur SET email ='fouadmerad@gmail.com' WHERE nom ='Fouad' """)
conn.commit()
print('\n')
cursor.execute('Select * from Fourniseur')
for row in cursor:
    print(row)
conn.close()

