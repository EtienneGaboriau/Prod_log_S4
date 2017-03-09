import mysql.connector as mysql

try;

    conn = mysql.connector.connect(host="infoweb",user="E155693G",password="E155693G", database="E155693G")
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS installation (
    id int(5) NOT NULL AUTO_INCREMENT,
    nom varchar(50) DEFAULT NULL,
    code_postal int(5) DEFAULT NULL,
    ville varchar(40) DEFAULT NULL,
    latitude decimal(23,20) DEFAULT NULL,
    longitude decimal(25,20) DEFAULT NULL,
    PRIMARY KEY(id)
);
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS equipements (
    id int(5) NOT NULL AUTO_INCREMENT,
    nom varchar(50) DEFAULT NULL,
    num_instal int(5) DEFAULT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(num_instal)
);
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS activites (
    id int(5) NOT NULL AUTO_INCREMENT,
    nom varchar(50) DEFAULT NULL,
    PRIMARY KEY(id)
);
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS equip_act (
    id_equip int(5) NOT NULL AUTO_INCREMENT,
    id_act int(5) DEFAULT NULL,
    PRIMARY KEY(id_equip, id_act),
    FOREIGN KEY(id_equip),
    FOREIGN KEY(id_act)
);
""")

    conn.close()

#table equip_act -id_equip (FK) : int -id_act (FK) : int => id_equip, id_act (PK)
