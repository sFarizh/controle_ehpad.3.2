# -*- coding: utf-8 -*-
"""
Created on Mon Fev 20 14:38:45 2023

@author: mathieu.olivier
"""
import pandas as pd
import sqlite3
import os


# à déplacer dans modules/init_db/init_db.py
### Partie Création de la DB et ajout des tables

def checkIfDBExists(dbname):
    if os.path.exists(dbname + '.sqlite'):
        os.remove(dbname + '.sqlite')
        print('Ancienne base de donnée écrasée')

def _initDb(dbname):
    #Supprime l'ancienne base de donnée
    checkIfDBExists(dbname)
    #Crée la nouvelle base de donnée
    conn = sqlite3.connect(dbname + '.sqlite')
    conn
    print('Création de la base de donnée {}.sqlite '.format(dbname))
    return conn

def _connDb(dbname):
    conn = sqlite3.connect(dbname + '.sqlite')
    conn
    return conn

def _importSrcData(df, table_name, conn, dbname):
    df.to_sql(name=table_name, con=conn)
    print('La table {} a été ajouté à la base de donnée {}'.format(table_name,dbname))
    return 

'''
Update section
#Pour Update une table à partir d'un fichier
# Ca ne marche pas pour l'instant 
# En pause car pas nécessaire

def _updateTable(dbname, table_name, excelFilePath):
    try:
        sqliteConnection = sqlite3.connect(dbname+'.sqlite')
        cursor = sqliteConnection.cursor()
        print("Connected to {}".format(dbname))

        #sql_drop_table = "DROP TABLE {}".format(table_name)
        cursor.execute("DROP TABLE "+table_name)
        sqliteConnection.commit()
        print("Table {} dropped".format(table_name))
        _importSrcData(
            _cleanSrcData(
                _csvReader(
                    _convertXlsxToCsv(excelFilePath)
                )
            ),
            table_name
            )
        print("Table {} Updated".format(table_name))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
table_name = '20220624_Diamant_MS_Demande_BD'
_updateTable(dbname, table_name, "input/sources/20220624_Diamant_MS_Demande_BD.xlsx" )

Sources: 
    - input_xslx
    - input_csx
    - ref
'''
