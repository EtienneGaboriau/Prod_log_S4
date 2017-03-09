import mysql.connector as mysql

try:
    conn = mysql.connect(user='E155693G',password='E155693G',host='infoweb', database='E155693G')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS installation (\
                        id int(10) NOT NULL AUTO_INCREMENT,\
                        nom varchar(50) DEFAULT NULL,\
                        code_postal int(5) DEFAULT NULL,\
                        ville varchar(40) DEFAULT NULL,\
                        latitude decimal(23,20) DEFAULT NULL,\
                        longitude decimal(25,20) DEFAULT NULL,\
                        PRIMARY KEY(id)\
                    )")
    cursor.execute("CREATE TABLE IF NOT EXISTS equipements (\
                        id int(10) NOT NULL AUTO_INCREMENT,\
                        nom varchar(50) DEFAULT NULL,\
                        num_instal int(5) DEFAULT NULL,\
                        PRIMARY KEY(id),\
                        FOREIGN KEY(num_instal)\
                    )")
    cursor.execute("CREATE TABLE IF NOT EXISTS activites (\
                        id int(10) NOT NULL AUTO_INCREMENT,\
                        nom varchar(50) DEFAULT NULL,\
                        PRIMARY KEY(id)\
                    )")
    cursor.execute("CREATE TABLE IF NOT EXISTS equip_act (\
                        id_equip int(10) NOT NULL AUTO_INCREMENT,\
                        id_act int(10) DEFAULT NULL,\
                        PRIMARY KEY(id_equip, id_act),\
                        FOREIGN KEY(id_equip) REFERENCES equipements(id),\
                        FOREIGN KEY(id_act) REFERENCES activites(id)\
                    )")
#except:
#    print ("pas content")

finally:
    cursor.close()
    conn.close()
