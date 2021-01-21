# coding: utf8
import pygame
from pygame.locals import *
from math import *
import os,json,time,codecs
os.chdir(os.path.dirname(os.path.realpath(__file__)))
pygame.init()

######TODO######
#-WATER kill
#-change velocity and gravity with timestamp
######TODO######

######CPROFILE######
#python -m cProfile -s tottime 2Dgame.py
############

pygame.display.set_caption("2D game with pygame - super_surviveur")
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
screenWidth=screen.get_rect().width
screenHeight=screen.get_rect().height
police20 = pygame.font.Font("./assets/police.otf", 20)
police30 = pygame.font.Font("./assets/police.otf", 30)
police40 = pygame.font.Font("./assets/police.otf", 40)
###############################
#LARGEUR -> [0] HAUTEUR -> [1]#
###############################
lifeGradient=[(255,0,0),(255,255,0),(0,255,0)]
clock=pygame.time.Clock()
tileSize=48
tilesList=[
    "./textures/air.png",
    "./textures/background.png",
    "./textures/barrier.png",
    "./textures/barrier_left.png",
    "./textures/barrier_right.png",
    "./textures/big_chest.png",
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
    "./textures/epic_chest.png",
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

tiles=[pygame.transform.scale(pygame.image.load(i).convert_alpha(), (tileSize+1, tileSize)) for i in tilesList]
persoList=[
    ["./textures/characters/perso/wait.png", 21, 23],
    ["./textures/characters/perso/wait2.png", 21, 23],
    ["./textures/characters/perso/walk-0.png", 21, 23],
    ["./textures/characters/perso/walk-1.png", 21, 23],
    ["./textures/characters/perso/walk-2.png", 21, 23],
    ["./textures/characters/perso/walk-3.png", 21, 23],
    ["./textures/characters/perso/climb-0.png", 21, 23],
    ["./textures/characters/perso/climb-1.png", 21, 23],
    ["./textures/characters/perso/climb-2.png", 21, 23],
    ["./textures/characters/perso/climb-3.png", 21, 23],
]
perso=[pygame.transform.scale(pygame.image.load(i[0]).convert_alpha(), (ceil(tileSize/17*i[1]), ceil(tileSize*1.5))) for i in persoList]
talkList=[
    ["./textures/characters/talk/wait-0.png", 21, 23],
    ["./textures/characters/talk/wait-1.png", 21, 23],
]
talk=[pygame.transform.scale(pygame.image.load(i[0]).convert_alpha(), (ceil(tileSize/17*i[1]), ceil(tileSize*1.5))) for i in talkList]
snakeList=[
    ["./textures/characters/snake/snake0.png", 21, 23],
    ["./textures/characters/snake/snake1.png", 21, 23],
]
snake=[pygame.transform.scale(pygame.image.load(i[0]).convert_alpha(), (ceil(tileSize/17*i[1]), ceil(tileSize*1.5))) for i in snakeList]
heart=pygame.transform.scale(pygame.image.load("./textures/utils/heart.png").convert_alpha(), [52,48])
lifeBorder=pygame.transform.scale(pygame.image.load("./textures/utils/border.png").convert_alpha(), [208,36])
level=1
name="vous".upper()

class Levels:
    def __init__(self):
        self.backgroundImage=pygame.transform.scale(pygame.image.load("./textures/background.png"), (screen.get_rect().width, screen.get_rect().height))
        s=''
        for i in open("./map/level{}.json".format(level),"r").readlines():
            s+=i
        self.map=json.loads(s)

        self.obstacle=[i for i in self.map['obstacle']]
        self.back=[i for i in self.map['back']]
        self.decors=[i for i in self.map['decors']]
        self.utils=[i for i in self.map['utils']]
        self.pos=[-47,4]       #MIDDLE[-1,4]
        self.playerPos=[58,6]       #MIDDLE[12,7]
        self.pressed={}
        self.chute=0
        self.ground=True
        self.gravityAcceleration=1.06
        self.ladder=False
        self.talk=False

    def draw(self):
        screen.fill((38,167,173))
        pos1=self.pos[0]*tileSize
        pos2=self.pos[1]*tileSize
        ran=range(ceil(self.pos[0]-1),ceil(screenWidth//tileSize-self.pos[0]+1))
        for i in range(ceil(self.pos[1]*-1-1),ceil(screenHeight//tileSize-self.pos[1]+1)):
            for i2 in ran:
                pos=[pos1+tileSize*i2,pos2+tileSize*i]
                tBack=self.back[i][i2]
                tObstacle=self.obstacle[i][i2]
                tDecors=self.decors[i][i2]
                tUtils=self.utils[i][i2]
                if tBack!=0:
                    screen.blit(tiles[tBack],pos)
                if tObstacle!=0:
                    screen.blit(tiles[tObstacle],pos)
                if tDecors!=0:
                    screen.blit(tiles[tDecors],pos)
                if tUtils!=0:
                    screen.blit(tiles[tUtils],pos)

                    
    
    def move(self,velocity,player):
        player.move=False
        player.climb=False
        if self.talk==False:
            if self.pressed.get(pygame.K_RIGHT):
                bord=False
                if self.obstacle[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-0.9)]!=0 or self.obstacle[ceil(self.playerPos[1]-3)][ceil(self.playerPos[0]-0.9)]!=0 or (self.ground==False and self.obstacle[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-0.9)]!=0):
                    bord=True
                if bord==False:
                    self.pos[0]-=velocity/50
                    self.playerPos[0]+=velocity/50
                    player.lastDirection=0
                    player.move=True
            if self.pressed.get(pygame.K_LEFT):
                bord=False
                if self.obstacle[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.9)]!=0 or self.obstacle[ceil(self.playerPos[1]-3)][ceil(self.playerPos[0]-1.9)]!=0 or (self.ground==False and self.obstacle[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-1.9)]!=0):
                    bord=True

                if bord==False:
                    self.pos[0]+=velocity/50
                    self.playerPos[0]-=velocity/50
                    player.lastDirection=180
                    player.move=True
            if self.pressed.get(pygame.K_UP):
                if self.ladder:
                    self.pos[1]+=velocity/50
                    self.playerPos[1]-=velocity/50
                    player.climb=True
            if self.pressed.get(pygame.K_DOWN):
                if self.ladder and ("ladder" in tilesList[self.utils[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-1.2)]] or "ladder" in tilesList[self.utils[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-1.8)]]):
                    self.pos[1]-=velocity/50
                    self.playerPos[1]+=velocity/50
                    player.climb=True
            if self.pressed.get(pygame.K_SPACE):
                if self.ground:
                    self.chute=-0.75/3

        if self.chute!=0:
            tempX=self.playerPos[1]+self.chute
            self.pos[1]-=self.chute*PCspeed*2.4
            if self.chute<0:
                self.chute=(tempX-self.playerPos[1])/(self.gravityAcceleration*1.05)
            elif self.chute<0.14:
                self.chute=(tempX-self.playerPos[1])*self.gravityAcceleration
            self.playerPos[1]=self.playerPos[1]+self.chute*PCspeed*2.4
        
        temp=perso[0].get_rect()
        temp.top=(levels.playerPos[1]+levels.pos[1])*tileSize-temp.height-5
        temp.left=(levels.playerPos[0]+levels.pos[0])*tileSize-temp.width+15
        temp.width-=10
        temp.height+=5
        player.rect=temp

    def gravity(self):
        self.ground=False
        self.ladder=False
        try:
            top=ceil(self.playerPos[1]-1)
            decorsElement=tilesList[self.decors[top][ceil(self.playerPos[0]-1.2)]]
            decorsElement2=tilesList[self.decors[top][ceil(self.playerPos[0]-1.8)]]
            utilsElement=tilesList[self.utils[top][ceil(self.playerPos[0]-1.2)]]
            utilsElement2=tilesList[self.utils[top][ceil(self.playerPos[0]-1.8)]]
            if self.obstacle[top][ceil(self.playerPos[0]-1.2)]!=0 or self.obstacle[top][ceil(self.playerPos[0]-1.8)]!=0 or ((self.back[top][ceil(self.playerPos[0]-1.2)]!=0 or self.back[top][ceil(self.playerPos[0]-1.8)]!=0) and (self.back[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.2)]==0 and self.back[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.8)]==0)):
                self.ground=True
            if "water_top" in decorsElement or "water_top" in decorsElement2:
                self.ground=True
                self.water()
            if "ladder" in utilsElement or "ladder" in utilsElement2 or "ladder" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.2)]] or "ladder" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.8)]]:
                self.ladder=True
            if "sign" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.2)]]:
                if self.pressed.get(pygame.K_a):
                    sign.read([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.2)])
            if "sign" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.8)]]:
                if self.pressed.get(pygame.K_a):
                    sign.read([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)])
            
            character.isAtPos([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)])
            monster.isAtPos([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)])
        except:
            pass
        if self.ground or self.ladder:
            self.chute=0
        else:
            if round(self.chute,2)==0 and self.chute<=0:
                self.chute=0.005
            
    def water(self):
        if level==1:
            tuto.water()
        else:
            pass



class Player:
    def __init__(self):
        self.life=100
        self.maxLife=100
        self.img=perso
        self.lastDirection=0
        self.move=False
        self.climb=False
        self.talk=False
        self.invincible=False
        temp=perso[0].get_rect()
        temp.top=levels.playerPos[1]*tileSize
        temp.left=levels.playerPos[0]*tileSize
        self.rect=temp
        self.iter=0
        self.current=0

    def draw(self,levels):
        if self.move and levels.ground:
            if self.iter>2000:
                self.current=(self.current+1)%4+2
                self.iter=0
            else:
                self.iter+=vitesseAnimation
        elif self.climb:
            if self.iter>2000:
                self.current=(self.current+1)%4+6
                self.iter=0
            else:
                self.iter+=vitesseAnimation
        elif levels.ladder:
            self.current=6
        elif levels.ground:
            if self.iter>2000:
                self.current=(self.current+1)%2
                self.iter=0
            else:
                self.iter+=vitesseAnimation
        else:
            self.current=0
        if self.lastDirection==0:
            screen.blit(self.img[self.current], ((levels.playerPos[0]-1+levels.pos[0])*tileSize,(levels.playerPos[1]-1+levels.pos[1])*tileSize-25))
        else:
            screen.blit(pygame.transform.flip(self.img[self.current], True, False), ((levels.playerPos[0]-1+levels.pos[0])*tileSize,(levels.playerPos[1]-1+levels.pos[1])*tileSize-25))
        
        lifePercent=self.life/self.maxLife*3
        if lifePercent<1:
            color=(255,0,0)
        elif lifePercent<2:
            color=(255,255,0)
        else:
            color=(0,255,0)
        pygame.draw.rect(screen, color, [50,30,lifeBorder.get_rect().width/self.maxLife*self.life,lifeBorder.get_rect().height])
        screen.blit(lifeBorder, [50,30])
        screen.blit(heart, [20,23])

class Sign:
    def __init__(self):
        s=''
        for i in open("./map/sign{}.json".format(level),"r").readlines():
            s+=i
        self.sign=[i for i in json.loads(s)['sign']]
    
    def read(self,pos):
        for s in self.sign:
            if s[1]==pos[0] and s[0]==pos[1]:
                text=police30.render(s[2], False, pygame.Color("#FFFFFF"))
                rectText = text.get_rect()
                rectText.top = (s[1]-2.5+levels.pos[1])*tileSize
                rectText.left = (s[0]+0.5+levels.pos[0])*tileSize-rectText.width/2
                screen.blit(text, rectText)
                break

class Character:
    def __init__(self):
        s=''
        for i in codecs.open("./map/character{}.json".format(level),"r", "utf-8").readlines():
            s+=i
        self.character=[i for i in json.loads(s)['character']]
        self.img=talk
        self.talk=False
        self.name=['noname','noname']
        self.iter=0
        self.current=0
    
    def draw(self):
        if self.iter>3000:
            self.current=(self.current+1)%2
            self.iter=0
        else:
            self.iter+=vitesseAnimation
        for s in self.character:
            if s[0]<levels.playerPos[0]-1:
                screen.blit(self.img[self.current], ((s[0]+levels.pos[0])*tileSize,(s[1]+levels.pos[1])*tileSize))
            else:
                screen.blit(pygame.transform.flip(self.img[self.current], True, False), ((s[0]+levels.pos[0])*tileSize,(s[1]+levels.pos[1])*tileSize))
        if self.talk!=False:
            s=pygame.Surface((screenWidth/2,screenHeight/6), pygame.SRCALPHA)
            s.fill((130,130,130,200))
            screen.blit(s,[screenWidth/4,screenHeight/8*5.5])
            for i in [self.talk[self.talk[2]%2+3]]:
                for iterate,s in enumerate(i[floor(self.talk[2]/2)].split("\n")):
                    if iterate==0:
                        text=police20.render(self.name[self.talk[2]%2]+" > "+s, False, pygame.Color("#FFFFFF"))
                    else:
                        text=police20.render(s, False, pygame.Color("#FFFFFF"))
                    rectText = text.get_rect()
                    rectText.top = screenHeight/8*5.5+23*iterate
                    rectText.left = screenWidth/4+5
                    screen.blit(text, rectText)
            
    
    def isAtPos(self,pos):
        for s in self.character:
            if (s[1]>=pos[0] and s[1]<=pos[0]+2) or (s[1]>=pos[0]-2 and s[1]<=pos[0]):
                if (s[0]>=pos[1] and s[0]<=pos[1]+2) or (s[0]>=pos[1]-2 and s[0]<=pos[1]):
                    if levels.pressed.get(pygame.K_a):
                        levels.talk=True
                        player.talk=True
                        self.talk=s
                        self.name=[s[5],name]
                        if s[0]<levels.playerPos[0]-1:
                            player.lastDirection=180
                        else:
                            player.lastDirection=0
                    elif self.talk==False:
                        text=police30.render("SALUT !", False, pygame.Color("#FFFFFF"))
                        rectText = text.get_rect()
                        rectText.top = (s[1]-1+levels.pos[1])*tileSize
                        rectText.left = (s[0]+2+levels.pos[0])*tileSize-rectText.width/2
                        screen.blit(text, rectText)
                    break

    def change(self):
        if self.talk[2]+1==len(self.talk[4])+len(self.talk[3]):
            levels.talk=False
            player.talk=False
            for v,s in enumerate(self.character):
                if s[0]==self.talk[0] and s[1]==self.talk[1]:
                    self.character[v][2]=0
            self.talk=False
            self.name=['noname','noname']
        else:
            self.talk[2]+=1

class Text:
    def __init__(self):
        s=''
        for i in codecs.open("./map/text{}.json".format(level),"r", "utf-8").readlines():
            s+=i
        self.t=[i for i in json.loads(s)['text']]
        self.text=[police30.render(i[0], False, pygame.Color("#FFFFFF")) for i in self.t]
    
    def draw(self):
        for i,v in enumerate(self.text):
            rectText = v.get_rect()
            rectText.top = self.t[i][1]+levels.pos[1]*tileSize
            rectText.left = self.t[i][2]+levels.pos[0]*tileSize
            screen.blit(v, rectText)

class Monster:
    def __init__(self):
        s=''
        for i in codecs.open("./map/monster{}.json".format(level),"r", "utf-8").readlines():
            s+=i
        self.monster=[i for i in json.loads(s)['monster']]
        self.img=snake
        self.iter=0
        self.rect=[]
        for s in self.monster:
            temp=snake[0].get_rect()
            temp.top=s[3][1]*tileSize
            temp.left=s[3][0]*tileSize
            self.rect.append(temp)
        self.current=0
    
    def draw(self, vitesseAnimation):
        if self.iter>3000:
            self.current=(self.current+1)%2
            self.iter=0
        else:
            self.iter+=vitesseAnimation
        for m in self.monster:
            if m[4]==0:
                screen.blit(self.img[self.current], ((m[3][0]-1+levels.pos[0])*tileSize,(m[3][1]-1+levels.pos[1])*tileSize-25))
            else:
                screen.blit(pygame.transform.flip(self.img[self.current], True, False), ((m[3][0]-1+levels.pos[0])*tileSize,(m[3][1]-1+levels.pos[1])*tileSize-25))
            
    
    def gravity(self, PCspeed):
        tempList=[]
        for m in self.monster:
            ground=False
            try:
                top=ceil(m[3][1]-1)
                if levels.obstacle[top][ceil(m[3][0]-1.2)]!=0 or levels.obstacle[top][ceil(m[3][0]-1.8)]!=0 or ((levels.back[top][ceil(m[3][0]-1.2)]!=0 or levels.back[top][ceil(m[3][0]-1.8)]!=0) and (levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-1.2)]==0 and levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-1.8)]==0)):
                    ground=True
            except:
                pass
            if ground:
                m[6]=0
            else:
                if round(m[6],2)==0 and m[6]<=0:
                    m[6]=0.003

            if m[4]==0:
                if not(levels.obstacle[ceil(m[3][1]-2)][ceil(m[3][0]-0.9)]!=0 or levels.obstacle[ceil(m[3][1]-3)][ceil(m[3][0]-0.9)]!=0 or (ground==False and levels.obstacle[ceil(m[3][1]-1)][ceil(m[3][0]-0.9)]!=0)):
                    top=ceil(m[3][1]-1)
                    if levels.obstacle[top][ceil(m[3][0]-0.2)]!=0 or levels.obstacle[top][ceil(m[3][0]-0.8)]!=0 or ((levels.back[top][ceil(m[3][0]-0.2)]!=0 or levels.back[top][ceil(m[3][0]-0.8)]!=0) and (levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-0.2)]==0 and levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-0.8)]==0)):
                        m[3][0]+=m[5]*(PCspeed/20)
                    elif levels.obstacle[top+m[7]][ceil(m[3][0]-0.2)]!=0 or levels.obstacle[top+m[7]][ceil(m[3][0]-0.8)]!=0 or ((levels.back[top+m[7]][ceil(m[3][0]-0.2)]!=0 or levels.back[top+m[7]][ceil(m[3][0]-0.8)]!=0) and (levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-0.2)]==0 and levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-0.8)]==0)):
                        m[3][0]+=m[5]*(PCspeed/20)
                    else:
                        m[4]=180
                elif not(levels.obstacle[ceil(m[3][1]-2-m[7])][ceil(m[3][0]-0.9)]!=0 or levels.obstacle[ceil(m[3][1]-3-m[7])][ceil(m[3][0]-0.9)]!=0 or (ground==False and levels.obstacle[ceil(m[3][1]-1-m[7])][ceil(m[3][0]-0.9)]!=0)):
                    m[6]=-0.06*m[7]
                    m[3][0]+=m[5]*(PCspeed/20)
                else:
                    m[4]=180
            elif m[4]==180:
                if not(levels.obstacle[ceil(m[3][1]-2)][ceil(m[3][0]-1.9)]!=0 or levels.obstacle[ceil(m[3][1]-3)][ceil(m[3][0]-1.9)]!=0 or (ground==False and levels.obstacle[ceil(m[3][1]-1)][ceil(m[3][0]-1.9)]!=0)):
                    top=ceil(m[3][1]-1)
                    if levels.obstacle[top][ceil(m[3][0]-2.2)]!=0 or levels.obstacle[top][ceil(m[3][0]-2.8)]!=0 or ((levels.back[top][ceil(m[3][0]-2.2)]!=0 or levels.back[top][ceil(m[3][0]-2.8)]!=0) and (levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-2.2)]==0 and levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-2.8)]==0)):
                        m[3][0]-=m[5]*(PCspeed/20)
                    elif levels.obstacle[top+m[7]][ceil(m[3][0]-2.2)]!=0 or levels.obstacle[top+m[7]][ceil(m[3][0]-2.8)]!=0 or ((levels.back[top+m[7]][ceil(m[3][0]-2.2)]!=0 or levels.back[top+m[7]][ceil(m[3][0]-2.8)]!=0) and (levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-2.2)]==0 and levels.back[ceil(m[3][1]-2)][ceil(m[3][0]-2.8)]==0)):
                        m[3][0]-=m[5]*(PCspeed/20)
                    else:
                        m[4]=0
                elif not(levels.obstacle[ceil(m[3][1]-2-m[7])][ceil(m[3][0]-1.9)]!=0 or levels.obstacle[ceil(m[3][1]-3-m[7])][ceil(m[3][0]-1.9)]!=0 or (ground==False and levels.obstacle[ceil(m[3][1]-1-m[7])][ceil(m[3][0]-1.9)]!=0)):
                    m[6]=-0.06*m[7]
                    m[3][0]-=m[5]*(PCspeed/20)
                else:
                    m[4]=0

            if m[6]!=0:
                tempX=m[3][1]+m[6]
                if m[6]<0:
                    m[6]=(tempX-m[3][1])/(levels.gravityAcceleration*1.05)
                elif m[6]<0.14:
                    m[6]=(tempX-m[3][1])*levels.gravityAcceleration
                m[3][1]=tempX

            temp=snake[0].get_rect()
            temp.top=(m[3][1]+levels.pos[1])*tileSize-temp.height+25
            temp.left=(m[3][0]+levels.pos[0])*tileSize-temp.width+15
            temp.height-=25
            tempList.append(temp)
        self.rect.clear()
        for i in tempList:
            self.rect.append(i)
    
    def isAtPos(self,pos):
        if player.invincible==False:
            current=ceil(iteration/vitesseAnimation)%2
            for i,s in enumerate(self.monster):
                if self.rect[i].colliderect(player.rect):
                    player.life-=s[2]
                    player.invincible=True

class Camera:
    def __init__(self):
        self.animate=False
        self.iterZoom=0
        self.iterToMove=50
    
    def zoomTalk(self, screen, scale, pos):
        scale=scale/self.iterToMove*self.iterZoom+1
        pos[0]=pos[0]/self.iterToMove*self.iterZoom
        pos[1]=pos[1]/self.iterToMove*self.iterZoom
        if self.iterZoom!=self.iterToMove:
            self.iterZoom+=1
        screen.blit(pygame.transform.scale(screen, (ceil(scale*screenWidth),ceil(scale*screenHeight))), (pos[0],pos[1]))
    
    def invertedZoomTalk(self, screen, scale, pos):
        scale=scale/self.iterToMove*self.iterZoom+1
        pos[0]=pos[0]/self.iterToMove*self.iterZoom
        pos[1]=pos[1]/self.iterToMove*self.iterZoom
        if self.iterZoom!=0:
            self.iterZoom-=1
        screen.blit(pygame.transform.scale(screen, (ceil(scale*screenWidth),ceil(scale*screenHeight))), (pos[0],pos[1]))
         


class Tuto:
    def __init__(self):
        self.waterText=False
        self.waterTime=0
        self.attention=police40.render("FAIT ATTENTION !", False, pygame.Color("#FF0000"))
    
    def draw(self):
        if self.waterTime+5>time.time():
            rectText = self.attention.get_rect()
            rectText.centery = screenHeight/10*6
            rectText.centerx = screenWidth/2
            screen.blit(self.attention, rectText)

    def water(self):
        self.waterText=True
        self.waterTime=time.time()
        levels.pos=[-21,1]
        levels.playerPos=[32.5,10]

levels=Levels()
player=Player()
sign=Sign()
character=Character()
sign.read([1,1])
text=Text()
tuto=Tuto()
monster=Monster()
camera=Camera()
game=True
iteration=0
vitesseAnimation=20
timeStamp=time.time()-1
while game:
    PCspeed=(time.time()-timeStamp)*100
    timeStamp=time.time()
    #VARIABLE WITH TIMESTAMP#
    vitesseAnimation=100*PCspeed
    vitessePlayer=2*PCspeed
    levels.gravityAcceleration=1.008
    #########################
    levels.move(vitessePlayer,player)
    monster.gravity(PCspeed)
    levels.draw()
    text.draw()
    if level==1:
        tuto.draw()
    monster.draw(vitesseAnimation)
    player.draw(levels)
    levels.gravity()
    character.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        elif event.type==pygame.KEYDOWN:
            #DEPLACEMENT DE LA CAMERA#
            if event.key==pygame.K_p:
                print("player:"+str(levels.playerPos)+"\nlevel:"+str(levels.pos))
            elif event.key==pygame.K_a and levels.talk:
                character.change()
            else:
                levels.pressed[event.key]=True
        elif event.type==pygame.KEYUP:
            levels.pressed[event.key]=False
        elif event.type == VIDEORESIZE:
            tileSize=ceil(event.w/(screenWidth/tileSize))
            tiles=[pygame.transform.scale(pygame.image.load(i).convert_alpha(), (tileSize+1, tileSize)) for i in tilesList]
    
    if player.talk:
        camera.zoomTalk(screen,0.5,[-screenWidth*0.25,-screenHeight*0.4])
    elif camera.iterZoom!=0:
        camera.invertedZoomTalk(screen,0.5,[-screenWidth*0.25,-screenHeight*0.4])
    
    
    pygame.display.flip()
    iteration+=1
    if iteration/vitesseAnimation>10:
        iteration=0