#!/usr/bin/env python
#fichier qui insert l'activité dans la bd

import mysql.connector as mysql
from Activity_Equipement import Activity_Equipement

def actEquInsertBD(actEqu):
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()

        sql= """INSERT INTO E155693G.equip_act (id_equip, id_act) VALUES (%s, %s);"""


        cursor.execute(sql, (actEqu.numEqu, actEqu.numAct))
        print("ok")

        cursor.close()
        conn.commit()



    except:
        print("erreur / duplication d'id")

    finally:
        conn.close()
