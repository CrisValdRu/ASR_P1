import os
import sqlite3
import json
from sqlite3 import Error

database_name = '/agentes.db'

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Erros as e:
        print(e)
    return None

def execute_statement(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def create_database():
    database  = os.path.dirname(os.path.abspath(__file__))+database_name 

    if not os.path.isfile(database): 
        sql_agente = 'CREATE TABLE IF NOT EXISTS agentes (id_agente INTEGER PRIMARY KEY,host_name TEXT NOT NULL,version TEXT,port INTEGER,comunidad TEXT);'
        sql_archivo = 'CREATE TABLE IF NOT EXISTS archivos(id_archivo INTEGER PRIMARY KEY,path TEXT,tipo INTEGER,id_agente_fk INGTEGER, FOREIGN KEY(id_agente_fk) REFERENCES agentes(id_agente));'
    
        conn = create_connection(database)
        if conn is not None:
            execute_statement(conn, sql_agente)
            execute_statement(conn, sql_archivo)
            conn.close()    
        else:
            print("Error, la BD no pudo ser creada")

def create_agente():
    show_agentes()
    print()
    database  = os.path.dirname(os.path.abspath(__file__))+database_name 
    conn = create_connection(database)
    with conn:
        host_name = input('Host (ej. 10.100.73.18): ')
        version = input('Version (ej. 2c): ')
        port = input('Port (ej. 1024): ')
        comunidad = input('Comunidad (ej. grupo4cm1): ')

        print(host_name + " " +version + " " + port + " " + comunidad)

        sql = 'INSERT INTO agentes(host_name,version,port,comunidad) VALUES(?,?,?,?)'
        cursor = conn.cursor()
        cursor.execute(sql, (host_name,version,port,comunidad))

        return cursor.lastrowid

def show_agentes():
    database  = os.path.dirname(os.path.abspath(__file__))+database_name 
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM agentes")

        rows = cur.fetchall()
        for row in rows:
            print(row)
        return json.dumps(rows)

def delete_agente():
    database  = os.path.dirname(os.path.abspath(__file__))+database_name 
    conn = create_connection(database)
    with conn:
        show_agentes()
        id = input("Ingrese ID: ")
        sql = 'DELETE FROM agentes WHERE id_agente=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))

def menu_agentes():
    create_database()
    continua_flag = True

    while continua_flag:
        print("\n ---- Menu Agentes ----")
        print("1. Agregar ")
        print("2. Consultar Agentes")
        print("3. Eliminar ")
        print("4. Salir ")

        opcion = input("Elige una opción: ")

        if int(opcion) == 1:
            create_agente()        
        elif int(opcion) == 2:
            show_agentes()
        elif int(opcion) == 3:
            delete_agente()
        else:
            print("Adiós")
            return None

        aux = input("¿Continuar? 1-Yes 0-No : ")
        if int(aux) == 1:
            continua_flag = True
        else:
            continua_flag = False
    print("Saliendo menu agentes")

if __name__ == '__main__':
    menu_agentes()