import mysql.connector
from mysql.connector import errorcode

# Create a connection config dictionary
config = {
    'user': 'root',
    'password': 'gtrhalo2',
    'host': '127.0.0.1',
    'database': 'menagerie',
    'raise_on_warnings': True,
}

try:
    '''
    cnx = mysql.connector.connect(user='root', password='gtrhalo2',
                              host='127.0.0.1', database='menagerie')
    '''
    cnx = mysql.connector.connect(**config)

    print("You are now connected to the "+ str(config['database']) +" database of the MYSQL Server.")

except mysql.connector.Error as sqlErr:

    if sqlErr.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif sqlErr.errno == errorcode.ER_BAD_DB_ERROR:
        print("The requested database does not exist.")
    else:
        print(sqlErr)

else:
    cnx.close()