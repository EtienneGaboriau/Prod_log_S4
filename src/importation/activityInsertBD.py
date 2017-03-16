#!/usr/bin/env python
#fichier qui insert l'activité dans la bd

import mysql.connector as mysql
from Activity import Activity

def actInsertBD(act):
    #try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()


        sql= "INSERT INTO activites (id_act, nom) VALUES({1},{2})".format(act.num,act.name)
        #sql= "INSERT INTO activites (id_act, nom) VALUES(12345,'foot')"
        print(sql)
        cursor.execute(sql)


        conn.close()

    #except:
    #    print("pas content")
