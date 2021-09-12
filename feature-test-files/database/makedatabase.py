import mysql.connector
from mysql.connector.constants import ClientFlag
import datetime
now = datetime.datetime.now()
date=(now.strftime('"%Y-%m-%d"'))

config = {
    'user': 'root',
    'password': 'admin666',
    'host': '34.71.98.84',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}

config['database'] = 'pythondb'  
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()



cursor.execute("CREATE TABLE wastedata ("
              "date varchar(255),"
               "wastetype VARCHAR(255) )")

cnxn.commit()  