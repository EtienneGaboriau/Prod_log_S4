#!/usr/bin/env python
#fichier qui insert l'activité dans la bd

import mysql.connector
from Activity import Activity

def activityInsertBD(act):
    conn = mysql.connector.connect(host="localhost",user="root",password="XXX", database="test1")
    cursor = conn.cursor()

    #tester ce truc
    activity = {"name" : act.name, "num" : act.num}

    #compléter celui la
    #cursor.execute("""INSERT INTO users (name, age) VALUES(%(name)s, %(age)s)""", user)


    conn.close()
