#!/usr/bin/env python
#fichier qui cherche les lignes dans le csv

import csv
from Activity_Equipement import Activity_Equipement
from activity_equipementInsertBD import actEquInsertBD

#ca marche!
def activityEquImport(fichier):
    file = open(fichier, "r")
    try:
        #on lit le fichier
        reader = csv.reader(file)

        i = 0

        #pour chaque ligne, on la transforme en activité et on l'insert dans la BD
        for row in reader:
            #on ignore la première ligne qui contient les en-tetes
            if(i != 0):
                actEqu = Activity_Equipement(row[4], row[2])
                print(actEqu)
                actEquInsertBD(actEqu)
            i += 1

    except:
        print("erreur, pas normal!!!")

    finally:
        file.close()
