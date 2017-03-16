#!/usr/bin/env python
#fichier qui cherche les lignes dans le csv

import csv
from Activity import Activity

#ca marche!
def activityImport(fichier):
    file = open(fichier, "r")
    try:
        #on lit le fichier
        reader = csv.reader(file)

        #pour chaque ligne, on la transforme en activité et on l'insert dans la BD
        for row in reader:
            act = Activity(row[5],row[2])
            #print(act)
            #activityInsertBD(act)

    #except:
    #    print("erreur, pas normal!!!")

    finally:
        file.close()
