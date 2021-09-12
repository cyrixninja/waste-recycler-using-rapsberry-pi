import mysql.connector
from mysql.connector.constants import ClientFlag


config = {
    'user': 'root',
    'password': 'admin666',
    'host': '34.71.98.84',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}


config['database'] = 'pythondb'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()


cursor.execute("SELECT COUNT(wastetype) FROM wastedata WHERE wastetype = 'Organic'")
out = cursor.fetchall()
for row in out :
    organic=row[0]
cursor.execute("SELECT COUNT(wastetype) FROM wastedata WHERE wastetype = 'Recyclable'")
out1 = cursor.fetchall()
for row in out1 :
    recyclable=row[0]
cursor.execute("SELECT COUNT(wastetype) FROM wastedata WHERE wastetype = 'Electronic'")
out2 = cursor.fetchall()
for row in out2 :
    electronics=row[0]

