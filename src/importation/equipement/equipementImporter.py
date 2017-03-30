#!/usr/bin/env python
#fichier qui prend les lignes dans le csv et les insert

import csv
from Equipement import Equipement
from equipementInsertBD import equInsertBD

#ca marche!
def equipementImport(fichier):
    file = open(fichier, "r")
    try:
        #on lit le fichier
        reader = csv.reader(file)

        i = 0

        #pour chaque ligne, on la transforme en Equipement et on l'insert dans la BD
        for row in reader:
            #on ignore la première ligne qui contient les en-tetes
            if(i != 0):
                eq = Equipement(row[4],row[5], row[2])
                print(eq)
                equInsertBD(eq)
            i += 1

    except:
        print("erreur / duplication d'id")

    finally:
        file.close()
