#!/usr/bin/env python
#

import mysql.connector as mysql


def get_Installation(ville):
    #fonction de récupération d'instalklation en fonction d'une ville
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()
        sql= "SELECT nom, num_instal FROM E155693G.installations where installations.ville=\'"+ville+"\';"
        cursor.execute(sql)
        data = cursor.fetchall()
        #tableau avesc les données sélectionnées
        insta=[]
        num_instal=[]
        test=None
        if(len(data)>0):
            #on verifie que le tableau possède quelquechose, puis, on le parcours tant qu'il y a quelquechose, et que l'indice est inférieur a sa taille.
            i=0
            while data is not None and i<len(data):
                j=0
                while j<len(data):
                    test=data[i][0]
                    insta.insert(i,test)
                    #tableau avec les noms
                    num_instal.insert(i,data[i][1])
                    #tableau avec les numeros d'installations
                i+=1


        cursor.close()
        conn.commit()
        return insta, num_instal
    except:     #gestion des erreurs
       print("erreur de connexion/requete")
    finally:
        conn.close()

def get_Equipement(ville):
    #fonction qui récupères les équipements en fonction des installations
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()
        instal, test = get_Installation(ville)
        #récupération des installations concernées
        row=[]
        equip=[]
        i=0
        while test is not None and i<len(test):
            test1 = str(test[i])
            sql= "SELECT nom, id_equip FROM E155693G.equipements where equipements.num_instal= "+test1+";"
            ##on parcours le tableau de numeros d'installtions, puis on selectionne les équipements associés a chaque installations dans un tableau.
            cursor.execute(sql)
            equip.insert(i,cursor.fetchall())
            #une ligne= equipements pour une installation.
            i+=1

        equ=[]

        if(len(equip)>0):
            #on verifie que le tableau possède quelquechose, puis, on le parcours tant qu'il y a quelquechose, et que l'indice est inférieur a sa taille.

            k=0
            while equip is not None and k<len(equip):
                j=0
                while equip[k] is not None and j<len(equip[k]):
                    tes=equip[k][0]
                    equ.insert(k,tes)
                    #tableau de résultat
                    j+=2
                k+=1
        cursor.close()
        conn.commit()
        return equ

    except:    #gestio des erreurs
     print("erreur de connexion/requete")

    finally:
        conn.close()

def get_activite(ville):
    #fonction qui récupère les activités en fonction des equipements.
    #Avec cette fonction, on récupère directement en fonction de la ville, puisque les focntions d'installations et d'équipement sont appelées, indrectement
    try:
        conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
        cursor = conn.cursor()
        equ = get_Equipement(ville)
        #on récuềre les équipements concernés
        act=[]
        i=0
        while equ is not None and i<len(equ):
            #on parcours les equipements, et on récupère dans la BD les activites concernés par l'équipement
            test1 = str(equ[i][1])
            print (test1)
            sql= "SELECT nom, activites.id_act FROM E155693G.equip_act, E155693G.activites where equip_act.id_equip= "+test1+" AND equip_act.id_act=activites.id_act;"
            cursor.execute(sql)
            act.insert(i,cursor.fetchall())
            i+=1

        acti=[]

        if(len(act)>0):
        #on verifie que le tableau possède quelquechose, puis, on le parcours tant qu'il y a quelquechose, et que l'indice est inférieur a sa taille.
            k=0
            while act is not None and k<len(act):
                j=0
                while act[k] is not None and j<len(act[k]):
                    tes=act[k][0],equ[k][0]
                    acti.insert(k,tes)
                    #on place dans un tableau, le nom de chaque activigte, avec son id et on associe le tout avec le nom de l'équipement.
                    j+=2
                k+=1
        cursor.close()
        conn.commit()
        return acti

    except:     #gestion des erreurs
        print("erreur de connexion/requete")

    finally:
        conn.close()
