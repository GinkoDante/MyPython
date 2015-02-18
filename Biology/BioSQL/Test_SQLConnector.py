__author__ = 'Bill Lee'

import mysql.connector

cnx = mysql.connector.connect(user='root', password='gtrhalo2',
                              host='localhost',
                              database='bioseqdb')
cnx.close()