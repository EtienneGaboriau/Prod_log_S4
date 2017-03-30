#!/usr/bin/env python
#fichier qui insert l'activité dans la bd

import mysql.connector as mysql
from Installation import Installation

def instalInsertBD(instal):
    try:

        #connexion à la bd
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()

        #exécution du sql (insertion dans la bd)
        sql= """INSERT INTO E155693G.installations (num_instal, nom, code_postal, ville, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s);"""
        cursor.execute(sql, (instal.num, instal.nom, instal.code_postal, instal.ville, instal.latitude, instal.longitude))
        print("ok")

    except:
        print("erreur / duplication d'id")

    finally:
        cursor.close()
        conn.commit()
        conn.close()
