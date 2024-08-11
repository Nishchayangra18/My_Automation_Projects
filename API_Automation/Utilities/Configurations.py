import configparser

import mysql.connector
from mysql.connector import Error


def Get_Config():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config


connect_config = {
    'user': Get_Config()['SQL']['user'],
    'password': Get_Config()['SQL']['password'],
    'host': Get_Config()['SQL']['host'],
    'database': Get_Config()['SQL']['database']

}


def getPassword():
    return "Nish_2418"


def get_Database_Connection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = get_Database_Connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    row1 = cursor.fetchone()
    row2 = cursor.fetchone()
    row3 = cursor.fetchone()
    conn.close()
    return row3
