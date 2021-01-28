import os
path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(path+"/textures")
for f in files:
    print('"./textures/{}",'.format(f))