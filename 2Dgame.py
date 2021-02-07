# coding: utf8
import pygame
from pygame.locals import *
from math import *
import os,json,time,codecs
os.chdir(os.path.dirname(os.path.realpath(__file__)))
pygame.init()

######TODO######
#-WATER kill
#-invincibilty when take damage
#-death in the tuto
######TODO######

######CPROFILE######
#python -m cProfile -s tottime 2Dgame.py
############

cursorList = (#sized 24x24
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "........................",
  "........................",
  "........................",
  "........................",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ",
  "          ....          ")

pygame.display.set_caption("2D game with pygame - super_surviveur")
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
screenWidth=screen.get_rect().width
screenHeight=screen.get_rect().height

cursor = pygame.cursors.compile(cursorList, black='X', white='.', xor='o')
pygame.mouse.set_cursor((24,24),(12,12),*cursor)

police20 = pygame.font.Font("./assets/police.otf", 20)
police30 = pygame.font.Font("./assets/police.otf", 30)
police40 = pygame.font.Font("./assets/police.otf", 40)
police60 = pygame.font.Font("./assets/police.otf", 60)
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
itemList=[
    "./textures/item/stone_sword.png",
    "./textures/item/bow.png",
]
itemImg=[pygame.transform.scale(pygame.image.load(i).convert_alpha(), (80, 80)) for i in itemList]
itemHandList=[
    "./textures/item/hand/stone_sword.png",
    "./textures/item/hand/bow.png",
]
itemHandImg=[pygame.transform.scale(pygame.image.load(i).convert_alpha(), (64, 64)) for i in itemHandList]
guiList=[
    "./textures/inventory/inventory.png",
    "./textures/inventory/slot.png",
    "./textures/inventory/chest.png",
]
gui=[]
pixel=5
# INVENTORY
gui.append(pygame.transform.scale(pygame.image.load(guiList[0]).convert_alpha(), (420, 420)))
# SLOT
gui.append(pygame.transform.scale(pygame.image.load(guiList[1]).convert_alpha(), (110, 110)))
# CHEST
gui.append(pygame.transform.scale(pygame.image.load(guiList[2]).convert_alpha(), (550, 550)))
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
        for i in codecs.open("./map/level{}.json".format(level),"r").readlines():
            s+=i
        self.map=json.loads(s)

        self.obstacle=[i for i in self.map['obstacle']]
        self.back=[i for i in self.map['back']]
        self.decors=[i for i in self.map['decors']]
        self.utils=[i for i in self.map['utils']]
        self.pos=[-80,0]       #MIDDLE[-1,4]
        self.playerPos=[-self.pos[0]+screenWidth/tileSize/2+0.4,10]       #MIDDLE[12,7]screenWidth/tileSize/2
        self.pressed={}
        self.chute=0
        self.ground=True
        self.jumpVelocity=-1
        self.isJump=False
        self.ladder=False
        self.talk=False

    def draw(self):
        screen.fill((38,167,173))
        pos1=self.pos[0]*tileSize
        pos2=self.pos[1]*tileSize
        ran=range(ceil(self.pos[0]-1),ceil(screenWidth//tileSize-self.pos[0]+1))
        for i in range(ceil(self.pos[1]*-1-1),ceil(screenHeight//tileSize-self.pos[1]+1)):
            t=pos2+tileSize*i
            tB=self.back[i]
            tO=self.obstacle[i]
            tD=self.decors[i]
            tU=self.utils[i]
            for i2 in ran:
                pos=[pos1+tileSize*i2,t]
                tBack=tB[i2]
                tObstacle=tO[i2]
                tDecors=tD[i2]
                tUtils=tU[i2]
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
            if self.pressed.get(pygame.K_d):
                if not(self.obstacle[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-0.9)]!=0 or self.obstacle[ceil(self.playerPos[1]-3)][ceil(self.playerPos[0]-0.9)]!=0 or (self.ground==False and self.obstacle[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-0.9)]!=0)):
                    self.pos[0]-=velocity/50
                    self.playerPos[0]+=velocity/50
                    player.lastDirection=0
                    player.move=True
            if self.pressed.get(pygame.K_q):
                if not(self.obstacle[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.9)]!=0 or self.obstacle[ceil(self.playerPos[1]-3)][ceil(self.playerPos[0]-1.9)]!=0 or (self.ground==False and self.obstacle[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-1.9)]!=0)):
                    self.pos[0]+=velocity/50
                    self.playerPos[0]-=velocity/50
                    player.lastDirection=180
                    player.move=True
            if self.pressed.get(pygame.K_z):
                if self.ladder:
                    self.pos[1]+=velocity/50
                    self.playerPos[1]-=velocity/50
                    player.climb=True
            if self.pressed.get(pygame.K_s):
                if self.ladder and ("ladder" in tilesList[self.utils[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-1.2)]] or "ladder" in tilesList[self.utils[ceil(self.playerPos[1]-1)][ceil(self.playerPos[0]-1.8)]]):
                    self.pos[1]-=velocity/50
                    self.playerPos[1]+=velocity/50
                    player.climb=True
            if self.pressed.get(pygame.K_SPACE):
                if self.ground:
                    self.isJump=True
                    self.jumpVelocity=16

        if self.isJump:
            if self.jumpVelocity<0:
                F = (0.0005 * (self.jumpVelocity**2))
            else:
                F = -(0.0005 * (self.jumpVelocity**2))
            if self.jumpVelocity<-12:
                self.jumpVelocity+=0.2*PCspeed*1.4
            self.jumpVelocity-=0.2*PCspeed*1.4
            self.playerPos[1]+=F*PCspeed*1.4
            self.pos[1]-=F*PCspeed*1.4
        else:
            self.jumpVelocity=-2

        
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

            if self.pressed.get(pygame.K_a):
                if "sign" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.2)]]:
                    [s.read([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.2)]) for s in sign]

                if "sign" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.8)]]:
                    [s.read([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)]) for s in sign]

                if "chest" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.2)]]:
                    [c.openChest([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.2)]) for c in chest]
                    self.pressed[pygame.K_a]=False

                if "chest" in tilesList[self.utils[ceil(self.playerPos[1]-2)][ceil(self.playerPos[0]-1.8)]]:
                    [c.openChest([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)]) for c in chest]
                    self.pressed[pygame.K_a]=False
            
            [c.isAtPos([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)]) for c in character]
            [m.isAtPos([ceil(self.playerPos[1]-1),ceil(self.playerPos[0]-1.8)]) for m in monster]
        except:
            pass
        if (self.ground and self.jumpVelocity<=0) or self.ladder:
            self.isJump=False
        else:
            self.isJump=True
            
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
        self.invincibleTime=time.time()
        self.invincibleIter=0
        temp=perso[0].get_rect()
        temp.top=levels.playerPos[1]*tileSize
        temp.left=levels.playerPos[0]*tileSize
        self.rect=temp
        self.iter=0
        self.current=0

    def draw(self,levels):
        if self.move and levels.ground:
            if self.iter>3000:
                self.current=(self.current+1)%4+2
                self.iter=0
            else:
                self.iter+=vitesseAnimation
        elif self.climb:
            if self.iter>3000:
                self.current=(self.current+1)%4+6
                self.iter=0
            else:
                self.iter+=vitesseAnimation
        elif levels.ladder:
            self.current=6
        elif levels.ground:
            if self.iter>3000:
                self.current=(self.current+1)%2
                self.iter=0
            else:
                self.iter+=vitesseAnimation
        else:
            self.current=0
        if self.invincible:
            invincibilityTimeLeft=self.invincibleTime-time.time()
            if invincibilityTimeLeft<=0:
                self.invincibleIter=0
                self.invincible=False
            else:
                self.invincibleIter+=2-invincibilityTimeLeft/1.5
        if self.lastDirection==0:
            if ceil(self.invincibleIter)%30<=14:
                # if inventory.inventory[8]-1>=0:
                #     screen.blit(itemHandImg[item.item[inventory.inventory[8]-1][2]], ((levels.playerPos[0]-0.4+levels.pos[0])*tileSize,(levels.playerPos[1]-0.7+levels.pos[1])*tileSize-25))
                screen.blit(self.img[self.current], ((levels.playerPos[0]-1+levels.pos[0])*tileSize,(levels.playerPos[1]-1+levels.pos[1])*tileSize-25))
        else:
            if ceil(self.invincibleIter)%30<=14:
                # if inventory.inventory[8]-1>=0:
                #     screen.blit(pygame.transform.flip(itemHandImg[item.item[inventory.inventory[8]-1][2]], True, False), ((levels.playerPos[0]-1.67+levels.pos[0])*tileSize,(levels.playerPos[1]-0.7+levels.pos[1])*tileSize-25))
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
    def __init__(self,sign):
        self.sign=sign
    
    def read(self,pos):
        if self.sign[1]==pos[0] and self.sign[0]==pos[1]:
            text=police30.render(self.sign[2], False, pygame.Color("#FFFFFF"))
            rectText = text.get_rect()
            rectText.top = (self.sign[1]-2.5+levels.pos[1])*tileSize
            rectText.left = (self.sign[0]+0.5+levels.pos[0])*tileSize-rectText.width/2
            screen.blit(text, rectText)

class Chest:
    def __init__(self,chest):
        self.chest=chest
    
    def openChest(self,pos):
        if self.chest[0][1]==pos[0] and self.chest[0][0]==pos[1]+1:
            inventory.chest=True
            inventory.chestInventory=self.chest[1]
            if not("void" in tilesList[levels.utils[pos[0]-1][pos[1]]]):
                levels.utils[pos[0]-1][pos[1]]=[i for i,v in enumerate(tilesList) if "/open_chest.png" in v][0]
    
    def changeChest(self,pos):
        if self.chest[0][1]==pos[0] and self.chest[0][0]==pos[1]+1:
            use=[True for i in inventory.chestInventory if i!=0]
            if True in use:
                levels.utils[pos[0]-1][pos[1]]=[i for i,v in enumerate(tilesList) if "/open_chest.png" in v][0]
            else:
                levels.utils[pos[0]-1][pos[1]]=[i for i,v in enumerate(tilesList) if "/void_chest.png" in v][0]

class Character:
    def __init__(self,character):
        self.character=character
        self.img=talk
        self.talk=False
        self.name=['noname','noname']
        self.iter=0
        self.current=0
    
    def draw(self, vitesseAnimation):
        if self.iter>3000:
            self.current=(self.current+1)%2
            self.iter=0
        else:
            self.iter+=vitesseAnimation
        if self.character[0]<levels.playerPos[0]-1:
            screen.blit(self.img[self.current], ((self.character[0]+levels.pos[0])*tileSize,(self.character[1]+levels.pos[1])*tileSize))
        else:
            screen.blit(pygame.transform.flip(self.img[self.current], True, False), ((self.character[0]+levels.pos[0])*tileSize,(self.character[1]+levels.pos[1])*tileSize))
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
        if (self.character[1]>=pos[0] and self.character[1]<=pos[0]+2) or (self.character[1]>=pos[0]-2 and self.character[1]<=pos[0]):
            if (self.character[0]>=pos[1] and self.character[0]<=pos[1]+2) or (self.character[0]>=pos[1]-2 and self.character[0]<=pos[1]):
                if levels.pressed.get(pygame.K_a):
                    levels.talk=True
                    player.talk=True
                    self.talk=self.character
                    self.name=[self.character[5],name]
                    if s[0]<levels.playerPos[0]-1:
                        player.lastDirection=180
                    else:
                        player.lastDirection=0
                elif self.talk==False:
                    text=police30.render("SALUT !", False, pygame.Color("#FFFFFF"))
                    rectText = text.get_rect()
                    rectText.top = (self.character[1]-1+levels.pos[1])*tileSize
                    rectText.left = (self.character[0]+2+levels.pos[0])*tileSize-rectText.width/2
                    screen.blit(text, rectText)

    def change(self):
        if self.talk!=False:
            if self.talk[2]+1==len(self.talk[4])+len(self.talk[3]):
                levels.talk=False
                player.talk=False
                if self.character[0]==self.talk[0] and self.character[1]==self.talk[1]:
                    self.character[2]=0
                self.talk=False
                self.name=['noname','noname']
            else:
                self.talk[2]+=1

class Text:
    def __init__(self,text):
        self.t=text
        self.text=police30.render(self.t[0], False, pygame.Color("#FFFFFF"))
    
    def draw(self):
        rectText = self.text.get_rect()
        rectText.top = self.t[1]+levels.pos[1]*tileSize
        rectText.left = self.t[2]+levels.pos[0]*tileSize
        screen.blit(self.text, rectText)

class Monster:
    def __init__(self,monster):
        self.monster=monster
        self.img=snake
        self.iter=0
        self.rect=snake[0].get_rect()
        self.rect.top=self.monster[3][1]*tileSize
        self.rect.left=self.monster[3][0]*tileSize
        self.current=0
        self.jumpVelocity=-1
        self.isJump=False
    
    def draw(self, vitesseAnimation):
        if self.iter>3000:
            self.current=(self.current+1)%2
            self.iter=0
        else:
            self.iter+=vitesseAnimation
        if self.monster[4]==0:
            screen.blit(self.img[self.current], ((self.monster[3][0]-1+levels.pos[0])*tileSize,(self.monster[3][1]-1+levels.pos[1])*tileSize-25))
        else:
            screen.blit(pygame.transform.flip(self.img[self.current], True, False), ((self.monster[3][0]-1+levels.pos[0])*tileSize,(self.monster[3][1]-1+levels.pos[1])*tileSize-25))
        pygame.draw.rect(screen, (50,50,50), [(self.monster[3][0]-1+levels.pos[0])*tileSize,(self.monster[3][1]-1+levels.pos[1])*tileSize-25+10, self.rect.width, 7], 0, 2)
        pygame.draw.rect(screen, (42,135,31), [(self.monster[3][0]-1+levels.pos[0])*tileSize,(self.monster[3][1]-1+levels.pos[1])*tileSize-25+10, self.rect.width/self.monster[1]*self.monster[9], 7], 0, 2)

    
    def gravity(self, PCspeed):
        rect=True
        if self.monster[10]==0:
            ground=False
            try:
                top=ceil(self.monster[3][1]-1)
                if levels.obstacle[top][ceil(self.monster[3][0]-1.2)]!=0 or levels.obstacle[top][ceil(self.monster[3][0]-1.8)]!=0 or ((levels.back[top][ceil(self.monster[3][0]-1.2)]!=0 or levels.back[top][ceil(self.monster[3][0]-1.8)]!=0) and (levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-1.2)]==0 and levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-1.8)]==0)):
                    ground=True
            except:
                pass
            if ground and self.monster[8]<=0:
                self.monster[7]=False
            else:
                self.monster[7]=True

            if self.monster[4]==0:
                if not(levels.obstacle[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-0.9)]!=0 or levels.obstacle[ceil(self.monster[3][1]-3)][ceil(self.monster[3][0]-0.9)]!=0 or (ground==False and levels.obstacle[ceil(self.monster[3][1]-1)][ceil(self.monster[3][0]-0.9)]!=0)):
                    top=ceil(self.monster[3][1]-1)
                    if levels.obstacle[top][ceil(self.monster[3][0]-0.2)]!=0 or levels.obstacle[top][ceil(self.monster[3][0]-0.8)]!=0 or ((levels.back[top][ceil(self.monster[3][0]-0.2)]!=0 or levels.back[top][ceil(self.monster[3][0]-0.8)]!=0) and (levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-0.2)]==0 and levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-0.8)]==0)):
                        self.monster[3][0]+=self.monster[5]*(PCspeed/20)
                    elif levels.obstacle[top+self.monster[6]][ceil(self.monster[3][0]-0.2)]!=0 or levels.obstacle[top+self.monster[6]][ceil(self.monster[3][0]-0.8)]!=0 or ((levels.back[top+self.monster[6]][ceil(self.monster[3][0]-0.2)]!=0 or levels.back[top+self.monster[6]][ceil(self.monster[3][0]-0.8)]!=0) and (levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-0.2)]==0 and levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-0.8)]==0)):
                        self.monster[3][0]+=self.monster[5]*(PCspeed/20)
                    else:
                        self.monster[4]=180
                elif not(levels.obstacle[ceil(self.monster[3][1]-2-self.monster[6])][ceil(self.monster[3][0]-0.9)]!=0 or levels.obstacle[ceil(self.monster[3][1]-3-self.monster[6])][ceil(self.monster[3][0]-0.9)]!=0 or (ground==False and levels.obstacle[ceil(self.monster[3][1]-1-self.monster[6])][ceil(self.monster[3][0]-0.9)]!=0)):
                    self.monster[7]=True
                    self.monster[8]=10.5
                    self.monster[3][0]+=self.monster[5]*(PCspeed/20)
                else:
                    self.monster[4]=180
            elif self.monster[4]==180:
                if not(levels.obstacle[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-1.9)]!=0 or levels.obstacle[ceil(self.monster[3][1]-3)][ceil(self.monster[3][0]-1.9)]!=0 or (ground==False and levels.obstacle[ceil(self.monster[3][1]-1)][ceil(self.monster[3][0]-1.9)]!=0)):
                    top=ceil(self.monster[3][1]-1)
                    if levels.obstacle[top][ceil(self.monster[3][0]-2.2)]!=0 or levels.obstacle[top][ceil(self.monster[3][0]-2.8)]!=0 or ((levels.back[top][ceil(self.monster[3][0]-2.2)]!=0 or levels.back[top][ceil(self.monster[3][0]-2.8)]!=0) and (levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-2.2)]==0 and levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-2.8)]==0)):
                        self.monster[3][0]-=self.monster[5]*(PCspeed/20)
                    elif levels.obstacle[top+self.monster[6]][ceil(self.monster[3][0]-2.2)]!=0 or levels.obstacle[top+self.monster[6]][ceil(self.monster[3][0]-2.8)]!=0 or ((levels.back[top+self.monster[6]][ceil(self.monster[3][0]-2.2)]!=0 or levels.back[top+self.monster[6]][ceil(self.monster[3][0]-2.8)]!=0) and (levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-2.2)]==0 and levels.back[ceil(self.monster[3][1]-2)][ceil(self.monster[3][0]-2.8)]==0)):
                        self.monster[3][0]-=self.monster[5]*(PCspeed/20)
                    else:
                        self.monster[4]=0
                elif not(levels.obstacle[ceil(self.monster[3][1]-2-self.monster[6])][ceil(self.monster[3][0]-1.9)]!=0 or levels.obstacle[ceil(self.monster[3][1]-3-self.monster[6])][ceil(self.monster[3][0]-1.9)]!=0 or (ground==False and levels.obstacle[ceil(self.monster[3][1]-1-self.monster[6])][ceil(self.monster[3][0]-1.9)]!=0)):
                    self.monster[7]=True
                    self.monster[8]=10.5
                    self.monster[3][0]-=self.monster[5]*(PCspeed/20)
                else:
                    self.monster[4]=0

            if self.monster[7]:
                if self.monster[8]<0:
                    F = (0.0005 * (self.monster[8]**2))
                else:
                    F = -(0.0005 * (self.monster[8]**2))
                if self.monster[8]<-12:
                    self.monster[8]+=0.2*PCspeed/1.4
                self.monster[8]-=0.2*PCspeed/1.4
                self.monster[3][1]+=F*PCspeed/1.4
            else:
                self.monster[8]=-2

        else:
            if self.monster[8]<0:
                F = (0.0005 * (self.monster[8]**2))
            else:
                F = -(0.0005 * (self.monster[8]**2))
            self.monster[8]-=0.2*PCspeed/1.4
            self.monster[3][1]+=F*PCspeed/1.4
            if self.monster[3][1]>len(levels.obstacle):
                for i,m in enumerate(monster):
                    if m==self:
                        del monster[i]
                rect=False

        if rect:
            self.rect=snake[0].get_rect()
            self.rect.top=(self.monster[3][1]+levels.pos[1])*tileSize-self.rect.height+25
            self.rect.left=(self.monster[3][0]+levels.pos[0])*tileSize-self.rect.width+15
            self.rect.height-=25

    
    def isAtPos(self,pos):
        if player.invincible==False:
            current=ceil(iteration/vitesseAnimation)%2
            if self.monster[10]==0:
                if pygame.mask.from_surface(self.img[self.current]).overlap(pygame.mask.from_surface(player.img[player.current]), (self.rect.left-player.rect.left, self.rect.top-player.rect.top)) != None:
                    player.life-=self.monster[2]
                    player.invincible=True
                    player.invincibleTime=time.time()+3
    
    def hitMonster(self,pos,damage):
        if self.rect.top<pos[1] and self.rect.bottom>pos[1]:
            if self.rect.left<pos[0] and self.rect.right>pos[0]:
                if self.monster[10]==0:
                    self.monster[9]-=damage
                    if self.monster[9]<=0:
                        self.monster[10]=1
                        self.monster[8]=10
    

class Item:
    def __init__(self):
        s=''
        for i in codecs.open("./map/item.json", "r", "utf-8").readlines():
            s+=i
        self.item=[i for i in json.loads(s)['item']]

class Inventory:
    def __init__(self):
        s=''
        for i in codecs.open("./map/inventory.json", "r", "utf-8").readlines():
            s+=i
        self.inventory=[i for i in json.loads(s)['inventory']]
        self.open=False
        self.chest=False
        self.chestInventory=[]
        self.select=None

    def draw(self):
        if not(player.talk):
            screen.blit(gui[1], (screenWidth/2-gui[1].get_width()/2,(screenHeight/8)*7-gui[1].get_height()/2))
            if self.inventory[8]-1>=0:
                screen.blit(itemImg[self.inventory[8]-1], (screenWidth/2-gui[1].get_width()/2+pixel*3,(screenHeight/8)*7-gui[1].get_height()/2+pixel*3))
            if self.open:
                top=screen.get_height()/2-gui[0].get_height()/2
                left=screen.get_width()/2-gui[0].get_width()/2
                screen.blit(gui[0],(left, top))
                for i,e in enumerate(self.inventory):
                    if e!=0:
                        if not(self.select==i):
                            if i!=8:
                                screen.blit(itemImg[item.item[e-1][2]],(left+pixel*7+(pixel*18*(i%4)), top+pixel*14+(pixel*18*(i//4))))
                            else:
                                screen.blit(itemImg[item.item[e-1][2]],(left+pixel*7, top+pixel*54))
                
                pos=pygame.mouse.get_pos()
                if pos[0]>left+pixel*7 and pos[0]<left+pixel*77:
                    if pos[1]>top+pixel*14 and pos[1]<top+pixel*48:
                        case=[ceil((pos[0]-(left+pixel*6))/pixel-1)//18 , ceil((pos[1]-(top+pixel*14))/pixel-1)//18]
                        s=pygame.Surface((pixel*16,pixel*16), pygame.SRCALPHA)
                        s.fill((200,200,200,150))
                        screen.blit(s,[left+pixel*7+case[0]*pixel*18,top+pixel*14+case[1]*pixel*18])
                    elif pos[1]>top+pixel*54 and pos[1]<top+pixel*70 and pos[0]<left+pixel*23:
                        s=pygame.Surface((pixel*16,pixel*16), pygame.SRCALPHA)
                        s.fill((200,200,200,150))
                        screen.blit(s,[left+pixel*7,top+pixel*54])
                        
                if self.select!=None:
                    screen.blit(itemImg[item.item[self.inventory[self.select]-1][2]],(pos[0]-pixel*8,pos[1]-pixel*8))

            elif self.chest:
                top=screen.get_height()/2-gui[2].get_height()/2
                left=screen.get_width()/2-gui[2].get_width()/2
                screen.blit(gui[2],(left, top))
                for i,e in enumerate(self.chestInventory):
                    if e!=0:
                        if not(self.select==i):
                            screen.blit(itemImg[item.item[e-1][2]],(left+pixel*20+(pixel*18*(i%4)), top+pixel*7+(pixel*18*(i//4))))
                for i,e in enumerate(self.inventory):
                    if e!=0:
                        if not(self.select==i+8):
                            if i!=8:
                                screen.blit(itemImg[item.item[e-1][2]],(left+pixel*20+(pixel*18*(i%4)), top+pixel*47+(pixel*18*(i//4))))
                            else:
                                screen.blit(itemImg[item.item[e-1][2]],(left+pixel*20, top+pixel*87))
                
                pos=pygame.mouse.get_pos()
                if pos[0]>left+pixel*20 and pos[0]<left+pixel*90:
                    if pos[1]>top+pixel*7 and pos[1]<top+pixel*41:
                        case=[ceil((pos[0]-(left+pixel*19))/pixel-1)//18 , ceil((pos[1]-(top+pixel*7))/pixel-1)//18]
                        s=pygame.Surface((pixel*16,pixel*16), pygame.SRCALPHA)
                        s.fill((200,200,200,150))
                        screen.blit(s,[left+pixel*20+case[0]*pixel*18,top+pixel*7+case[1]*pixel*18])
                    elif pos[1]>top+pixel*47 and pos[1]<top+pixel*81:
                        case=[ceil((pos[0]-(left+pixel*19))/pixel-1)//18 , ceil((pos[1]-(top+pixel*47))/pixel-1)//18]
                        s=pygame.Surface((pixel*16,pixel*16), pygame.SRCALPHA)
                        s.fill((200,200,200,150))
                        screen.blit(s,[left+pixel*20+case[0]*pixel*18,top+pixel*47+case[1]*pixel*18])
                    elif pos[1]>top+pixel*87 and pos[1]<top+pixel*103 and pos[0]<left+pixel*36:
                        s=pygame.Surface((pixel*16,pixel*16), pygame.SRCALPHA)
                        s.fill((200,200,200,150))
                        screen.blit(s,[left+pixel*20,top+pixel*87])

                if self.select!=None:
                    if self.select<8:
                        screen.blit(itemImg[item.item[self.chestInventory[self.select]-1][2]],(pos[0]-pixel*8,pos[1]-pixel*8))
                    else:
                        screen.blit(itemImg[item.item[self.inventory[self.select-8]-1][2]],(pos[0]-pixel*8,pos[1]-pixel*8))
    
    def hit(self,pos):
        if inventory.inventory[8]-1>=0:
            mid=[round(player.rect.left+player.rect.width/2),round(player.rect.top+player.rect.height/2)]
            distance=sqrt((pos[0]-mid[0])**2+(pos[1]-mid[1])**2)/tileSize
            weapon=item.item[inventory.inventory[8]-1]
            if distance<=weapon[4]:
                [m.hitMonster(pos, weapon[1]) for m in monster]


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
        self.attention=police30.render("FAIT ATTENTION !", False, pygame.Color("#FF0000"))
    
    def draw(self):
        if self.waterTime+5>time.time():
            rectText = self.attention.get_rect()
            rectText.centery = screenHeight/10*6
            rectText.centerx = screenWidth/2
            screen.blit(self.attention, rectText)

    def water(self):
        self.waterText=True
        self.waterTime=time.time()
        levels.pos=[levels.pos[0]+1,levels.pos[1]+1]
        levels.playerPos=[levels.playerPos[0]-1,levels.playerPos[1]-1]


def inventoryEvenements(key):
    global timeStamp,game
    pause=True
    while pause:
        levels.draw()
        text.draw()
        [m.draw(vitesseAnimation) for m in monster]
        player.draw(levels)
        [c.draw(0) for c in character]
        inventory.draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                pause=False
                break
            elif event.type==pygame.KEYDOWN:
                for k in key:
                    if k==event.key:
                        pause=False
                        break
            elif event.type==pygame.KEYUP:
                levels.pressed[event.key]=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                if inventory.open:
                    top=screen.get_height()/2-gui[0].get_height()/2
                    left=screen.get_width()/2-gui[0].get_width()/2
                    if pos[0]>left+pixel*7 and pos[0]<left+pixel*77:
                        if pos[1]>top+pixel*14 and pos[1]<top+pixel*48:
                            case=[ceil((pos[0]-(left+pixel*7))/pixel-1)//18 , ceil((pos[1]-(top+pixel*14))/pixel-1)//18]
                            select=case[0]+case[1]*4
                            if inventory.select==None:
                                if inventory.inventory[select]!=0:
                                    inventory.select=select
                            else:
                                if inventory.inventory[select]==0 or inventory.select==select:
                                    inventory.inventory[inventory.select], inventory.inventory[select]=inventory.inventory[select],inventory.inventory[inventory.select]
                                    inventory.select=None
                                else:
                                    inventory.inventory[inventory.select], inventory.inventory[select]=inventory.inventory[select],inventory.inventory[inventory.select]
                        elif pos[1]>top+pixel*54 and pos[1]<top+pixel*70 and pos[0]<left+pixel*23:
                            case=[0,2]
                            select=8
                            if inventory.select==None:
                                if inventory.inventory[select]!=0:
                                    inventory.select=select
                            else:
                                if inventory.inventory[select]==0 or inventory.select==select:
                                    inventory.inventory[inventory.select], inventory.inventory[select]=inventory.inventory[select],inventory.inventory[inventory.select]
                                    inventory.select=None
                                else:
                                    inventory.inventory[inventory.select], inventory.inventory[select]=inventory.inventory[select],inventory.inventory[inventory.select]
                elif inventory.chest:
                    top=screen.get_height()/2-gui[2].get_height()/2
                    left=screen.get_width()/2-gui[2].get_width()/2
                    if pos[0]>left+pixel*20 and pos[0]<left+pixel*90:
                        if pos[1]>top+pixel*7 and pos[1]<top+pixel*41:
                            case=[ceil((pos[0]-(left+pixel*19))/pixel-1)//18 , ceil((pos[1]-(top+pixel*7))/pixel-1)//18]
                            select=case[0]+case[1]*4
                            if inventory.select==None:
                                if inventory.chestInventory[select]!=0:
                                    inventory.select=select
                            else:
                                if inventory.select<8:
                                    if inventory.chestInventory[select]==0 or inventory.select==select:
                                        inventory.chestInventory[inventory.select], inventory.chestInventory[select]=inventory.chestInventory[select],inventory.chestInventory[inventory.select]
                                        inventory.select=None
                                    else:
                                        inventory.chestInventory[inventory.select], inventory.chestInventory[select]=inventory.chestInventory[select],inventory.chestInventory[inventory.select]
                                else:
                                    if inventory.chestInventory[select]==0:
                                        inventory.inventory[inventory.select-8], inventory.chestInventory[select]=inventory.chestInventory[select],inventory.inventory[inventory.select-8]
                                        inventory.select=None
                                    else:
                                        inventory.inventory[inventory.select-8], inventory.chestInventory[select]=inventory.chestInventory[select],inventory.inventory[inventory.select-8]
                                

                        elif pos[1]>top+pixel*47 and pos[1]<top+pixel*81:
                            case=[ceil((pos[0]-(left+pixel*19))/pixel-1)//18 , ceil((pos[1]-(top+pixel*47))/pixel-1)//18]
                            select=case[0]+case[1]*4+8
                            if inventory.select==None:
                                if inventory.inventory[select-8]!=0:
                                    inventory.select=select
                            else:
                                if inventory.select<8:
                                    if inventory.inventory[select-8]==0:
                                        inventory.chestInventory[inventory.select], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.chestInventory[inventory.select]
                                        inventory.select=None
                                    else:
                                        inventory.chestInventory[inventory.select], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.chestInventory[inventory.select]
                                else:
                                    if inventory.inventory[select-8]==0 or inventory.select==select:
                                        inventory.inventory[inventory.select-8], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.inventory[inventory.select-8]
                                        inventory.select=None
                                    else:
                                        inventory.inventory[inventory.select-8], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.inventory[inventory.select-8]
                        
                        elif pos[1]>top+pixel*87 and pos[1]<top+pixel*103 and pos[0]<left+pixel*36:
                            select=16
                            if inventory.select==None:
                                if inventory.inventory[select-8]!=0:
                                    inventory.select=select
                            else:
                                if inventory.select<8:
                                    if inventory.inventory[select-8]==0:
                                        inventory.chestInventory[inventory.select], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.chestInventory[inventory.select]
                                        inventory.select=None
                                    else:
                                        inventory.chestInventory[inventory.select], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.chestInventory[inventory.select]
                                else:
                                    if inventory.inventory[select-8]==0 or inventory.select==select:
                                        inventory.inventory[inventory.select-8], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.inventory[inventory.select-8]
                                        inventory.select=None
                                    else:
                                        inventory.inventory[inventory.select-8], inventory.inventory[select-8]=inventory.inventory[select-8],inventory.inventory[inventory.select-8]
                    
                    [c.changeChest([ceil(levels.playerPos[1]-1),ceil(levels.playerPos[0]-1.8)]) for c in chest]
                    [c.changeChest([ceil(levels.playerPos[1]-1),ceil(levels.playerPos[0]-1.2)]) for c in chest]

        pygame.display.flip()
    timeStamp=time.time()-0.001

levels=Levels()
player=Player()

s=''
for i in codecs.open("./map/sign{}.json".format(level),"r").readlines():
    s+=i
sign=[Sign(i) for i in json.loads(s)['sign']]
s=''
for i in codecs.open("./map/chest{}.json".format(level),"r").readlines():
    s+=i
chest=[Chest(i) for i in json.loads(s)['chest']]
s=''
for i in codecs.open("./map/character{}.json".format(level),"r", "utf-8").readlines():
    s+=i
character=[Character(i) for i in json.loads(s)['character']]
s=''
for i in codecs.open("./map/text{}.json".format(level),"r", "utf-8").readlines():
    s+=i
text=[Text(i) for i in json.loads(s)['text']]
s=''
for i in codecs.open("./map/monster{}.json".format(level),"r", "utf-8").readlines():
    s+=i

monster=[Monster(i) for i in json.loads(s)['monster']]
tuto=Tuto()
item=Item()
inventory=Inventory()
camera=Camera()
game=True
iteration=0
vitesseAnimation=20
timeStamp=time.time()-1
while game:
    if inventory.chest:
        inventoryEvenements([pygame.K_e, pygame.K_a, pygame.K_ESCAPE])
        inventory.chest=False
        inventory.chestInventory=[]
    if inventory.open:
        inventoryEvenements([pygame.K_e, pygame.K_a, pygame.K_ESCAPE])
        inventory.open=False
    PCspeed=(time.time()-timeStamp)*100
    timeStamp=time.time()
    #VARIABLE WITH TIMESTAMP#
    vitesseAnimation=100*PCspeed
    vitessePlayer=2*PCspeed
    #########################
    levels.move(vitessePlayer,player)
    [m.gravity(PCspeed) for m in monster]
    levels.draw()
    [t.draw() for t in text]
    [m.draw(vitesseAnimation) for m in monster]
    player.draw(levels)
    if level==1:
        tuto.draw()
    levels.gravity()
    [c.draw(vitesseAnimation) for c in character]
    inventory.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        elif event.type==pygame.KEYDOWN:
            #DEPLACEMENT DE LA CAMERA#
            if event.key==pygame.K_p:
                print("player:"+str(levels.playerPos)+"\nlevel:"+str(levels.pos))
            elif event.key==pygame.K_e and not(inventory.chest):
                inventory.open=not(inventory.open)
            elif event.key==pygame.K_a and levels.talk:
                [c.change() for c in character]
            else:
                levels.pressed[event.key]=True
        elif event.type==pygame.KEYUP:
            levels.pressed[event.key]=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            inventory.hit(event.pos)
        elif event.type==pygame.VIDEORESIZE:
            oldTileSize=tileSize
            tileSize=round(event.w/(screenWidth/tileSize))
            levels.pos[1]+=((screenWidth-event.w)/2-(screenHeight-event.h)/2)/tileSize
            tiles=[pygame.transform.scale(pygame.image.load(i).convert_alpha(), (tileSize+1, tileSize)) for i in tilesList]
            screenWidth=screen.get_rect().width
            screenHeight=screen.get_rect().height
                
    if player.talk:
        camera.zoomTalk(screen,0.5,[-screenWidth*0.25,-screenHeight*0.4])
    elif camera.iterZoom!=0:
        camera.invertedZoomTalk(screen,0.5,[-screenWidth*0.25,-screenHeight*0.4])
    
    
    pygame.display.flip()
    iteration+=1
    if iteration/vitesseAnimation>10:
        iteration=0