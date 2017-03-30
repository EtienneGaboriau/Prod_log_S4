#!/usr/bin/env python
#fichier qui prend les lignes dans le csv et les insert

import csv
from Installation import Installation
from installationInsertBD import instalInsertBD

#ca marche!
def instalImport(fichier):
    file = open(fichier, "r")
    try:
        #on lit le fichier
        reader = csv.reader(file)

        i = 0

        #pour chaque ligne, on la transforme en Installation et on l'insert dans la BD
        for row in reader:
            #on ignore la première ligne qui contient les en-tetes
            if(i != 0):
                instal = Installation(row[1], row[0], row[4], row[2], row[9], row[10])
                print(instal)
                instalInsertBD(instal)
            i += 1

    except:
        print("erreur / duplication d'id")

    finally:
        file.close()
