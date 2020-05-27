from ExcelCalc import year, TouristsPerYear, country2011, value2011, countries, values, TransportArray, transport
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def insert_values(conn,insert):
    sql = """ INSERT INTO touristsperyear(year,tourists) VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql,insert)
    return cur.lastrowid
def insert_values1(conn,insert):
    sql = """ INSERT INTO topcountries(year,tourists,country) VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql,insert)
    return cur.lastrowid
def insert_values2(conn,insert):
    sql = """ INSERT INTO touristsTransported(year,tourists,Transport) VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, insert)
    return cur.lastrowid
def main():
    database = r"Touristes.db"
    sql_create_touristsperyear_table =  """ CREATE TABLE IF NOT EXISTS touristsperyear(
                                     year integer,
                                     tourists integer 
                                     ); """
    sql_create_topcountries_table = """ CREATE TABLE IF NOT EXISTS topcountries(
                                    year integer,
                                    tourists integer,
                                    country text 
                                    ); """
    sql_create_touristsTransported_table = """CREATE TABLE IF NOT EXISTS touristsTransported(
                                                year integer,
                                                tourists integer,
                                                Transport text
    );"""
    conn = create_connection(database)

    if conn is not None:
        create_table(conn,sql_create_touristsperyear_table)
        create_table(conn,sql_create_topcountries_table)
        create_table(conn,sql_create_touristsTransported_table)
    else:
        print('Error ! cannot create database')
    with conn:
        for i in range(len(TouristsPerYear)):
            insert_values(conn,[year[i], TouristsPerYear[i]])
        for z in range(len(year)):
            for i in range(len(country2011)):
                insert_values1(conn,[year[z],values[z][i],countries[z][i]])
        for r in range(4):
            for o in range(4):
                insert_values2(conn,[year[r], transport[o], TransportArray[r][o]])

if __name__ == '__main__':
    main()