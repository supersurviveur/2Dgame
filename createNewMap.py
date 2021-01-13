import os,json
os.chdir(os.path.dirname(os.path.realpath(__file__)))
largeur=int(input('largeur:'))
hauteur=int(input('hauteur:'))
l={"obstacle":0,"back":0,"decors":0,"utils":0}
t=[[0 for i in range(largeur)] for h in range(hauteur)]
l["obstacle"]=t
l["back"]=t
l["decors"]=t
l["utils"]=t
j=json.dumps(l)
open("./tempMap.json", "w").write(j)