#!/usr/bin/env python
#fichier qui insert l'activité dans la bd

import mysql.connector as mysql
from Equipement import Equipement

def equInsertBD(act):
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()

        sql= """INSERT INTO E155693G.equipement (id_act, nom) VALUES (%s, %s);"""


        cursor.execute(sql, (act.num, act.name))
        print("ok")

        cursor.close()
        conn.commit()


    except:
        print("pas content/surement id dupliqué")

    finally:
        conn.close()
