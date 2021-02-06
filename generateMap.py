import pygame
from pygame.locals import *
from math import *
import os,json
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.chdir(os.path.dirname(os.path.realpath(__file__)))
pygame.init()

pygame.display.set_caption("2D game with pygame - super_surviveur")
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
police = pygame.font.Font("./assets/police.otf", 30)
###############################
#LARGEUR -> [0] HAUTEUR -> [1]#
###############################
tileSize=48
tiles=[
    "./textures/air.png",
    "./textures/background.png",
    "./textures/barrier.png",
    "./textures/barrier_left.png",
    "./textures/barrier_right.png",
    "./textures/void_chest.png",
    "./textures/big_stone.png",
    "./textures/big_white_flower.png",
    "./textures/big_yellow_flower.png",
    "./textures/black_barrier.png",
    "./textures/black_barrier_left.png",
    "./textures/black_barrier_right.png",
    "./textures/black_rich_sign.png",
    "./textures/black_sign.png",
    "./textures/black_sign_arrow.png",
    "./textures/block_background.png",
    "./textures/blue.png",
    "./textures/bluegrass_blue.png",
    "./textures/bluegrass_top.png",
    "./textures/bluegrass_top_left.png",
    "./textures/bluegrass_top_right.png",
    "./textures/blue_background.png",
    "./textures/blue_bluegrass.png",
    "./textures/blue_left.png",
    "./textures/blue_left_right.png",
    "./textures/blue_right.png",
    "./textures/blue_top_left.png",
    "./textures/blue_top_left_right.png",
    "./textures/blue_top_right.png",
    "./textures/chest.png",
    "./textures/crate.png",
    "./textures/dirt.png",
    "./textures/dirt_background.png",
    "./textures/dirt_grass.png",
    "./textures/dirt_left.png",
    "./textures/dirt_left_right.png",
    "./textures/dirt_right.png",
    "./textures/dirt_top_left.png",
    "./textures/dirt_top_left_right.png",
    "./textures/dirt_top_right.png",
    "./textures/open_chest.png",
    "./textures/floor0.png",
    "./textures/floor1.png",
    "./textures/floor100.png",
    "./textures/floor16.png",
    "./textures/floor17.png",
    "./textures/floor18.png",
    "./textures/floor19.png",
    "./textures/floor2.png",
    "./textures/floor20.png",
    "./textures/floor21.png",
    "./textures/floor3.png",
    "./textures/floor34.png",
    "./textures/floor35.png",
    "./textures/floor36.png",
    "./textures/floor4.png",
    "./textures/floor5.png",
    "./textures/floor51.png",
    "./textures/floor52.png",
    "./textures/floor53.png",
    "./textures/floor6.png",
    "./textures/floor67.png",
    "./textures/floor68.png",
    "./textures/floor69.png",
    "./textures/floor83.png",
    "./textures/floor84.png",
    "./textures/floor99.png",
    "./textures/floornew11.png",
    "./textures/floornew2.png",
    "./textures/floornew3.png",
    "./textures/floornew4.png",
    "./textures/floornew5.png",
    "./textures/grass_dirt.png",
    "./textures/grass_top.png",
    "./textures/grass_top_left.png",
    "./textures/grass_top_right.png",
    "./textures/ladder_bottom.png",
    "./textures/ladder_middle.png",
    "./textures/ladder_top.png",
    "./textures/lawn.png",
    "./textures/rich_sign.png",
    "./textures/roof_bacground2.png",
    "./textures/roof_background.png",
    "./textures/roof_blackground.png",
    "./textures/roof_bottom.png",
    "./textures/roof_left.png",
    "./textures/roof_left_bottom.png",
    "./textures/roof_left_top.png",
    "./textures/roof_right.png",
    "./textures/roof_right_bottom.png",
    "./textures/roof_right_top.png",
    "./textures/roof_round_left_bottom.png",
    "./textures/roof_round_left_top.png",
    "./textures/roof_round_right_bottom.png",
    "./textures/roof_round_right_top.png",
    "./textures/roof_top.png",
    "./textures/sheet.png",
    "./textures/sign.png",
    "./textures/sign_arrow.png",
    "./textures/stone.png",
    "./textures/water.png",
    "./textures/water_top.png",
    "./textures/white_flower.png",
    "./textures/yellow_flower.png",
    "./textures/torch.png",
]
tiles=[pygame.transform.scale(pygame.image.load(i).convert_alpha(), (tileSize, tileSize)) for i in tiles]

class Levels:
    def __init__(self):
        self.background=pygame.transform.scale(pygame.image.load("./textures/background.png"), (screen.get_rect().width, screen.get_rect().height))
        s=''
        for i in open("./map/level1.json","r").readlines():
            s+=i
        self.map=json.loads(s)
        self.obstacle=[i for i in self.map['obstacle']]
        self.back=[i for i in self.map['back']]
        self.decors=[i for i in self.map['decors']]
        self.utils=[i for i in self.map['utils']]
        self.pos=[0,0]
        self.pressed={}
        self.tilePos=0
        self.select=0
        self.value='obstacle'
        self.ver=False
    def draw(self):
        screen.blit(self.background,(0,0))
        for i in range(ceil(self.pos[1]*-1-1),ceil(screen.get_rect().height//tileSize-self.pos[1]+1)):
            for i2 in range(ceil(self.pos[0]*-1-1),ceil(screen.get_rect().width//tileSize-self.pos[0]+1)):
                if self.ver and self.value=="background":
                    if tiles[self.back[i][i2]]!=0:
                        screen.blit(tiles[self.back[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                if self.ver and self.value=="obstacle":
                    if tiles[self.obstacle[i][i2]]!=0:
                        screen.blit(tiles[self.obstacle[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                if self.ver and self.value=="decors":
                    if tiles[self.decors[i][i2]]!=0:
                        screen.blit(tiles[self.decors[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                if self.ver and self.value=="utils":
                    if tiles[self.utils[i][i2]]!=0:
                        screen.blit(tiles[self.utils[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                if self.ver==False:
                    if tiles[self.back[i][i2]]!=0:
                        screen.blit(tiles[self.back[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                    if tiles[self.obstacle[i][i2]]!=0:
                        screen.blit(tiles[self.obstacle[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                    if tiles[self.decors[i][i2]]!=0:
                        screen.blit(tiles[self.decors[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])
                    if tiles[self.utils[i][i2]]!=0:
                        screen.blit(tiles[self.utils[i][i2]],[self.pos[0]*tileSize+tileSize*i2 , self.pos[1]*tileSize+tileSize*i])

    def move(self,velocity):
        if iteration%4==0:
            if self.pressed.get(pygame.K_RIGHT):
                self.pos[0]-=1
            if self.pressed.get(pygame.K_LEFT):
                self.pos[0]+=1
            if self.pressed.get(pygame.K_UP):
                self.pos[1]+=1
            if self.pressed.get(pygame.K_DOWN):
                self.pos[1]-=1
    def tile(self):
        pygame.draw.rect(screen,(240,240,240),[0,screen.get_rect().height-tileSize,screen.get_rect().width,tileSize])
        pygame.draw.rect(screen,(240,240,240),[0,0,screen.get_rect().width,tileSize])
        t=["OBSTACLE","BACKGROUND","DECORS","UTILS"]
        for i in range(4):
            if self.value=="obstacle" and i==0:
                pygame.draw.rect(screen,(200,200,200),[i*screen.get_rect().width/4,0,screen.get_rect().width/4,tileSize])
            elif self.value=="background" and i==1:
                pygame.draw.rect(screen,(200,200,200),[i*screen.get_rect().width/4,0,screen.get_rect().width/4,tileSize])
            elif self.value=="decors" and i==2:
                pygame.draw.rect(screen,(200,200,200),[i*screen.get_rect().width/4,0,screen.get_rect().width/4,tileSize])
            elif self.value=="utils" and i==3:
                pygame.draw.rect(screen,(200,200,200),[i*screen.get_rect().width/4,0,screen.get_rect().width/4,tileSize])
            pygame.draw.line(screen,(200,200,200),[(screen.get_rect().width/4)*i,0],[(screen.get_rect().width/4)*i,tileSize-1],2)
            text = police.render(t[i], False, pygame.Color("#000000"))
            rectText = text.get_rect()
            rectText.midleft = (((screen.get_rect().width/4)*i)+(screen.get_rect().width/4-rectText.width)/2,tileSize/2)
            screen.blit(text, rectText)
            
        for t in enumerate(tiles):
            screen.blit(t[1],[t[0]*tileSize+self.tilePos,screen.get_rect().height-tileSize])
    def save(self):
        d={"obstacle":self.obstacle}
        d["decors"]=self.decors
        d["back"]=self.back
        d["utils"]=self.utils
        j=json.dumps(d)
        open("./map/level1.json","w").write(j)

    def setTile(self,x,y):
        if self.value=="obstacle":
            self.obstacle[x][y]=self.select
        elif self.value=="background":
            self.back[x][y]=self.select
        elif self.value=="decors":
            self.decors[x][y]=self.select
        elif self.value=="utils":
            self.utils[x][y]=self.select
        self.save()
    
    def setAir(self,x,y):
        if self.value=="obstacle":
            self.obstacle[x][y]=0
        elif self.value=="background":
            self.back[x][y]=0
        elif self.value=="decors":
            self.decors[x][y]=0
        elif self.value=="utils":
            self.utils[x][y]=0
        self.save()

    def click(self):
        if event.type!=pygame.KEYDOWN or event.type!=pygame.KEYUP:
            try:
                if self.pressed.get(pygame.BUTTON_RIGHT):
                    if event.pos[1]>screen.get_rect().height-tileSize:
                        for t in enumerate(tiles):
                            if event.pos[0]>=t[0]*tileSize+levels.tilePos and event.pos[0]<=(t[0]+1)*tileSize+levels.tilePos:
                                levels.select=t[0]
                    elif event.pos[1]<tileSize:
                        t=['obstacle','background','decors','utils']
                        levels.value=t[ceil(event.pos[0]//(screen.get_rect().width/4))]
                    else:
                        levels.setAir(ceil(ceil(event.pos[1]//tileSize)-levels.pos[1]),ceil(ceil(event.pos[0]//tileSize)-levels.pos[0]))
                elif self.pressed.get(pygame.BUTTON_LEFT):
                    if event.pos[1]>screen.get_rect().height-tileSize:
                        for t in enumerate(tiles):
                            if event.pos[0]>=t[0]*tileSize+levels.tilePos and event.pos[0]<=(t[0]+1)*tileSize+levels.tilePos:
                                levels.select=t[0]
                    elif event.pos[1]<tileSize:
                        t=['obstacle','background','decors','utils']
                        levels.value=t[ceil(event.pos[0]//(screen.get_rect().width/4))]
                    else:
                        levels.setTile(ceil(ceil(event.pos[1]//tileSize)-levels.pos[1]),ceil(ceil(event.pos[0]//tileSize)-levels.pos[0]))
                elif self.pressed.get(pygame.BUTTON_MIDDLE):
                    if event.pos[1]>screen.get_rect().height-tileSize:
                        for t in enumerate(tiles):
                            if event.pos[0]>=t[0]*tileSize+levels.tilePos and event.pos[0]<=(t[0]+1)*tileSize+levels.tilePos:
                                levels.select=t[0]
                    elif event.pos[1]<tileSize:
                        t=['obstacle','background','decors','utils']
                        levels.value=t[ceil(event.pos[0]//(screen.get_rect().width/4))]
                    else:
                        x,y=ceil(ceil(event.pos[1]//tileSize)-levels.pos[1]),ceil(ceil(event.pos[0]//tileSize)-levels.pos[0])
                        if self.value=="obstacle":
                            self.select=self.obstacle[x][y]
                        elif self.value=="background":
                            self.select=self.back[x][y]
                        elif self.value=="decors":
                            self.select=self.decors[x][y]
                        elif self.value=="utils":
                            self.select=self.utils[x][y]
            except:
                pass

levels=Levels()
game=True
iteration=0
while game:
    levels.draw()
    levels.move(0.9)
    levels.tile()
    if levels.pressed.get(pygame.BUTTON_RIGHT) or levels.pressed.get(pygame.BUTTON_LEFT) or levels.pressed.get(pygame.BUTTON_MIDDLE):
        levels.click()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        elif event.type==pygame.KEYDOWN:
            #DEPLACEMENT DE LA CAMERA#
            if event.key==pygame.K_RIGHT:
                levels.pressed[event.key]=True
            elif event.key==pygame.K_LEFT:
                levels.pressed[event.key]=True
            elif event.key==pygame.K_UP:
                levels.pressed[event.key]=True
            elif event.key==pygame.K_DOWN:
                levels.pressed[event.key]=True
            elif event.key==pygame.K_RETURN:
                levels.save()
                game=False
            elif event.key==pygame.K_LALT or event.key==pygame.K_RALT:
                if levels.ver:
                    levels.ver=False
                else:
                    levels.ver=True
        elif event.type==pygame.KEYUP:
            levels.pressed[event.key]=False
        elif event.type==pygame.MOUSEWHEEL:
            if event.y>0:
                if levels.tilePos<0:
                    levels.tilePos+=30
            if event.y<0:
                if levels.tilePos>-len(tiles)*tileSize:
                    levels.tilePos-=30
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button!=pygame.BUTTON_WHEELDOWN and event.button!=pygame.BUTTON_WHEELUP and event.button!=4 and event.button!=6 and event.button!=7 and event.button!=10:
                levels.pressed[event.button]=True
        elif event.type==pygame.MOUSEBUTTONUP:
            levels.pressed[event.button]=False
    pygame.display.flip()
    iteration+=1