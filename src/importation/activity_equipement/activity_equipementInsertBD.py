#!/usr/bin/env python
#fichier qui insert l'Activity_Equipement dans la bd

import mysql.connector as mysql
from Activity_Equipement import Activity_Equipement

def actEquInsertBD(actEqu):
    try:

        #connexion à la bd
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()

        #exécution du sql (insertion dans la bd)
        sql= """INSERT INTO E155693G.equip_act (id_equip, id_act) VALUES (%s, %s);"""
        cursor.execute(sql, (actEqu.numEqu, actEqu.numAct))
        print("ok")

    except:
        print("erreur / duplication d'id")

    finally:
        cursor.close()
        conn.commit()
        conn.close()
