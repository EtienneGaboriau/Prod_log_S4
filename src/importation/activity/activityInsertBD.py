#!/usr/bin/env python
#fichier qui insert l'activité dans la bd

import mysql.connector as mysql
from Activity import Activity

def actInsertBD(act):
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()

        sql= """INSERT INTO E155693G.activites (id_act, nom) VALUES (%s, %s);"""


        cursor.execute(sql, (act.num, act.name))
        print("ok")

        cursor.close()
        conn.commit()


    except:
        print("pas content")

    finally:
        conn.close()
