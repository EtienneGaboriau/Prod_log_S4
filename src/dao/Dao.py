#!/usr/bin/env python
#

import mysql.connector as mysql


def get_Installation(ville):
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()

        sql= "SELECT * FROM E155693G.installations (nom, num_instal) where installations.ville="+ville+";"


        cursor.execute(sql)
        if(len(cursor.fetchall)>0):
            insta = cursor.fetchone()
            while insta is not None:
                print (insta[0], insta[1])
                row = cur.fetchone()

        print("ok")

        cursor.close()
        conn.commit()


    #except:
    #    print("pas content")

    finally:
        conn.close()
