import os,json
os.chdir(os.path.dirname(os.path.realpath(__file__)))
largeur=int(input('colonne to add:'))
file=input('file:')
s=''
for i in open("./map/"+file+".json","r").readlines():
    s+=i
m=json.loads(s)
obstacle=[i for i in m['obstacle']]
back=[i for i in m['back']]
decors=[i for i in m['decors']]
utils=[i for i in m['utils']]
for i in obstacle:
    [i.append(0) for a in range(largeur)] 
for i in utils:
    [i.append(0) for a in range(largeur)] 
for i in back:
    [i.append(0) for a in range(largeur)] 
for i in decors:
    [i.append(0) for a in range(largeur)] 

d={"obstacle":obstacle}
d["decors"]=decors
d["back"]=back
d["utils"]=utils
j=json.dumps(d)
open("./tempMap.json", "w").write(j)