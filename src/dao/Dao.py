#!/usr/bin/env python
#

import mysql.connector as mysql


def get_Installation(ville):
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()
        sql= "SELECT nom, num_instal FROM E155693G.installations where installations.ville=\'"+ville+"\';"
        cursor.execute(sql)
        data = cursor.fetchall()
        insta=[]
        num_instal=[]
        test=None
        if(len(data)>0):
            i=0
            while data is not None and i<len(data):
                j=0
                while j<len(data):
                    test=data[i][0]
                    insta.insert(i,test)
                    num_instal.insert(i,data[i][1])
                    data.remove(data[i])
                i+=1


        cursor.close()
        conn.commit()
        return insta, num_instal
    #except:
     #  print("erreur de connexion/requete")
    finally:
        conn.close()

def get_Equipement(ville):
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()
        instal, test = get_Installation(ville)
        row=[]
        equip=[]
        i=0
        while test is not None and i<len(test):
            test1 = str(test[i])
            sql= "SELECT nom, id_equip FROM E155693G.equipements where equipements.num_instal= "+test1+";"
            cursor.execute(sql)
            equip.insert(i,cursor.fetchall())
            i+=1

        equ=[]
        num_equip=[]

        if(len(equip)>0):
            k=0
            while equip is not None and k<len(equip):
                j=0
                while equip[k] is not None and j<len(equip[k]):
                    tes=equip[k][0]
                    equ.insert(k,tes)
                    j+=2
                k+=1
        cursor.close()
        conn.commit()
        return equ

    #except:
     #  print("erreur de connexion/requete")

    finally:
        conn.close()




"""def Villecomplete(mot):
    try:
        res=[]
        userCo, passwordCO, hostCo, databaseCo = getConnexion()
        cnx = mysql.connect(user=userCo, password=passwordCO, host=hostCo, database=databaseCo)
        # on récupère toutes les villes qui correspondent à ce que la personne vient de taper
        cursor = cnx.cursor()
        cursor.execute("SELECT `ville` FROM `installations` WHERE `ville` LIKE \'"+mot+"%\' ")
        listeville=cursor.fetchall()
        for ville in listeville:
            if ville[0] not in res:
                res.append(ville[0])
        # on retourne la liste des villes qui correspondent
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
cnx.close()"""
