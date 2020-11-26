import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=DESKTOP-DQHM2SB;'
                          'DATABASE=WideWorldImporters-Full;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('Select * from Produit')
    for row in cursor:
        print(row)

    cursor.execute("""UPDATE Produit SET nomProd ='tomate' WHERE idProd =1 """)
    conn.commit()
    print('\n')

    # commit changes to the database

    # update successful message
    print("Database Updated !")
    print('\n')

    cursor.execute('Select * from Produit')
    for row in cursor:
        print(row)
except :

    # update failed message as an error
    print("Database Update Failed !: {}")

    # reverting changes because of exception
    conn.rollback()

    # Disconnecting from the database
conn.close()