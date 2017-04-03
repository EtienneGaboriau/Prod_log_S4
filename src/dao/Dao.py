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
        #test.append(instal[0][0])
        row=[]
        equip=[]
        #print (test[0])
        i=0
        while test is not None and i<len(test):
            #print (instal[0], test[0])
            test1 = str(test[i])
            #print(test1)
            sql= "SELECT nom, id_equip FROM E155693G.equipements where equipements.num_instal= "+test1+";"
            cursor.execute(sql)
            equip= equ = cursor.fetchall()
            #print(equip)
            i+=1

        equ=[]
        num_equip=[]

        if(len(equip)>0):
            i=0
            while equip is not None and i<len(equip):
                j=0
                while equip[i] is not None and j<len(equip[i]):
                    tes=equip[i][j]
                    #print(tes)
                    print (j)
                    print(i)
                    equ.insert(i,tes)
                    num_equip.insert(i,equip[i][j])
                    j+=1
                i+=1

        #print("ok")

        cursor.close()
        conn.commit()


    #except:
     #  print("erreur de connexion/requete")

    finally:
        conn.close()
