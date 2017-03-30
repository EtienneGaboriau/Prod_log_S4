import mysql.connector as mysql

try:
    #connexion à la bd
    conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
    cursor = conn.cursor()

    #creation de la table installations
    cursor.execute("CREATE TABLE installations (\
                        num_instal int(20) DEFAULT NULL,\
                        nom varchar(500) DEFAULT NULL,\
                        code_postal int(5) DEFAULT NULL,\
                        ville varchar(40) DEFAULT NULL,\
                        latitude decimal(23,20) DEFAULT NULL,\
                        longitude decimal(25,20) DEFAULT NULL,\
                        PRIMARY KEY(num_instal)\
                    )")

    #creation de la table equipements
    cursor.execute("CREATE TABLE equipements (\
                        id_equip int(20) DEFAULT NULL,\
                        nom varchar(50) DEFAULT NULL,\
                        num_instal int(20) DEFAULT NULL,\
                        PRIMARY KEY(id_equip),\
                        FOREIGN KEY(num_instal) REFERENCES installations(num_instal)\
                    )")

    #creation de la table activites
    cursor.execute("CREATE TABLE activites (\
                        id_act int(20) DEFAULT NULL,\
                        nom varchar(500) DEFAULT NULL,\
                        PRIMARY KEY(id_act)\
                    )")

    #creation de la table de jointure equip_act
    cursor.execute("CREATE TABLE equip_act (\
                        id_equip int(20) DEFAULT NULL,\
                        id_act int(20) DEFAULT NULL,\
                        PRIMARY KEY(id_equip, id_act),\
                        FOREIGN KEY(id_equip) REFERENCES equipements(id_equip),\
                        FOREIGN KEY(id_act) REFERENCES activites(id_act)\
                    )")


finally:
    cursor.close()
    conn.close()
