#! /usr/bin/python

# -*- coding: utf-8 -*-

# Affichage d'un formulaire HTML simplifié :

print "Content-Type: text/html\n"

print """<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 <meta http-equiv="Content-Language" content="fr" />
 <title>
  Installations Sportives en Pays de Loire
 </title>
</head>
<body>
  <form>
    <div>Ville</div>
    <input name="ville"/>
    <div>Activité</div>
    <input name="act"/></br></br>
    <input type=button name="rechercher" value="rechercher"/>
  </form>
</body>
</html>"""
