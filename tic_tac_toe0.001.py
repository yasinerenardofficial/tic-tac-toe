import pygame,sys,random,time,moviepy
from pygame import *
pygame.font.init() 
pygame.init()
pygame.display.set_caption("press R to reset")

#variables
screenwidth=800
screenhight=800
screencentrex=screenwidth/2
screencentrey=screenhight/2
screen_centre=(screencentrex,screencentrey)
event = pygame.event.get()
surface = pygame.display.set_mode((screenwidth,screenhight))
texte= pygame.font.SysFont('Comic Sans MS', 50)
texte_b= pygame.font.SysFont('Comic Sans MS', 50)
timer=pygame.time.Clock()
keys=pygame.key.get_pressed()
mousex,mousey=pygame.mouse.get_pos()
chrono=0
stagegeneration=0
game_win=0
controls_on=1
match_is_won=0

#1=blocs 
#2=bacterie
#3=carre
#4=morpion
game=4
MOUSEBUTTONisDOWN=0
MOUSEBUTTONisUP=0
fpshow=0


#blocs variables
rows=3
columns=3
ecart=2
startposition=0#(screenhight-screenwidth)//2
surfacedeblocsx,surfacedeblocsy=screenwidth,screenhight
generationx=0
generationy=startposition
generationencoure=1
blocsagenerer=rows*columns
blocsizex=(surfacedeblocsx//rows)-ecart
blocsizey=(surfacedeblocsy//columns)-ecart

#sounds
wind_sound=("Jeux/You Win.mp3")

run=True
score=0
bgcolor = (0, 0, 0)
blocsnombre=0
debug=0
player=1
drawable=[]
class mort(): 0
class carre():
    all=[]
    def __init__(self, x, y):
        global blocsnombre
        self.rect = pygame.Rect(x, y, blocsizex, blocsizey)
        carre.all.append(self)
        drawable.append(self)
        self.random_color = random.choices(range(256), k=3)
        #blocsnombre+=1
    def draw(self):
        pygame.draw.rect(surface, self.random_color, self.rect)

def carresetup():
    global screenwidth,startposition,surfacedeblocsx,generationx,generationy,generationencoure
    if blocsnombre<blocsagenerer and generationencoure!=0:    
        for target in range(0,blocsagenerer):
            new_carre=carre(generationx,generationy)
            generationx+=blocsizex+ecart
            if generationx>surfacedeblocsx-1:
                generationx=0
                generationy+=blocsizey+ecart
    else:
        generationencoure=0

class button(pygame.sprite.Sprite):
    all=[]
    def __init__(self,type,image,xy,width_screen,height_screen):
        global screenwidth,screenhight,screencentrex,screencentrey,drawable
        super().__init__()
        self.vie=1
        self.state=0
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int(screenwidth / width_screen), int(screenhight / height_screen)))
        self.original_image = self.image
        self.x,self.y = xy
        self.surf = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.rect = self.surf.get_rect(center=(screencentrex, screencentrey))
        self.width_screen,self.height_screen=width_screen,height_screen
        self.type=type
        button.all.append(self)
        #drawable.append(self)
        
    
    def draw(self):
        global ballecouleur,menu
        if self.vie==1:
            if run :
                surface.blit(self.image, self.rect)
                self.do()

    def do(self):
        if self.type == 1:0
        else:
            for _ in pygame.event.get():
                if _.type == KEYDOWN:
                    if _.key == K_ESCAPE:
                            0
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    if _.type == MOUSEBUTTONDOWN:1
                        #self.image=pygame.image.load("sousou/startbutton2.png")
                        #self.image = pygame.transform.scale(self.image, (self.image.get_width() / (self.image.get_width() / screenwidth)//self.width_screen, self.image.get_height() / (self.image.get_height() / screenhight)//self.height_screen)) 
                    elif _.type == pygame.MOUSEBUTTONUP:
                        menu=1
                else :
                    self.image=pygame.image.load(self.image)
                    #self.image = pygame.transform.scale(self.image, (self.image.get_width() / (self.image.get_width() / screenwidth)//self.width_screen, self.image.get_height() / (self.image.get_height() / screenhight)//self.height_screen)) 

    def reset(self):
        self.vie=0

button1=button(1,"you_win.png",screen_centre,5,5)

def guivetimefrom(value):
    sec=value//60
    min=sec//60
    secb=sec-(min*60)
    seca=('{0:02d}'.format(secb))
    mina=('{0:02d}'.format(min))
    #if sec>60: sec=0
    return f"{mina}:{seca}"

class blocs():
    all=[]
    def __init__(self,x,y,w,h):
        global blocsnombre,blocsizex,blocsizey,keys
        self.vie=1
        self.x=x
        self.y=y
        if w==0:
            self.width=blocsizex
        else : 
            self.width=w
        if h==0:    
            self.height=blocsizey
        else : 
            self.height=h
        self.tag=blocsnombre
        blocsnombre+=1
        self.color=(255,255,255)
        self.modifiable=0
        self.team=0
        self.random_color = random.choices(range(256), k=3)
        self.modified_color=["white","blue","red","green","yellow"]
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        

        #action to execute
        blocs.all.append(self)
        drawable.append(self)

    def draw(self):
        global blocsnombre,blocsizex,blocsizey,debug,keys,player,MOUSEBUTTONisDOWN,MOUSEBUTTONisUP
        if self.vie==1:
            if self.modifiable==0:self.color="white"
            if self.modifiable==1:self.color="grey"
            if self.modifiable>1:
                self.color=self.modified_color[self.team]
            pygame.draw.rect(surface,self.color,self.rect)
            if debug ==1: 
                text_surface = texte.render(f"{self.rect.center}", True, (255,0,0))
                surface.blit(text_surface, ((self.rect.centerx-15),(self.rect.centery-35)))
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if  MOUSEBUTTONisDOWN==1:
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        if self.modifiable==0:
                            self.modifiable=1
                if MOUSEBUTTONisUP==1:
                    if self.modifiable==1:
                        pygame.mixer.music.load('point1.mp3')
                        pygame.mixer.music.play()
                        self.team=player
                        if player==2:player=1
                        else:player+=1
                        self.modifiable=2
                        check_win()
                        
            elif self.modifiable==1:
                    self.modifiable=0
            if keys [K_r]:
                self.reset()

    def reset(self):
        self.vie=1
        self.modifiable=0
        self.team=0

def check_win():
        global blocsizex,blocsizey,blocsnombre,controls_on,match_is_won
        for obj in blocs.all:
            for obj_b in blocs.all:
                for obj_c in blocs.all:
                    if obj is not obj_b :
                        if  obj.rect.collidepoint(obj_c.rect.midright[0]+obj_c.rect.width//2 , obj_c.rect.centery) and\
                            obj_b.rect.collidepoint(obj_c.rect.midleft[0]-obj_c.rect.width//2 , obj_c.rect.centery) or\
                            obj.rect.collidepoint(obj_c.rect.centerx , obj_c.rect.midtop[1]-obj_c.rect.height//2) and \
                            obj_b.rect.collidepoint(obj_c.rect.centerx , obj_c.rect.midbottom[1]+obj_c.rect.height//2) or\
                            obj.rect.collidepoint(obj_c.rect.midright[0]+obj_c.rect.width//2 ,obj_c.rect.midtop[1]-obj_c.rect.height//2 ) and\
                            obj_b.rect.collidepoint(obj_c.rect.midleft[0]-obj_c.rect.width//2 ,obj_c.rect.midbottom[1]+obj_c.rect.height//2 ) or\
                            obj.rect.collidepoint(obj_c.rect.midright[0]+obj_c.rect.width//2 ,obj_c.rect.midbottom[1]+obj_c.rect.height//2 ) and\
                            obj_b.rect.collidepoint(obj_c.rect.midleft[0]-obj_c.rect.width//2 ,obj_c.rect.midtop[1]-obj_c.rect.height//2 ) :
                                if obj.team==obj_b.team==obj_c.team and obj.team >0 and match_is_won==0 :
                                    
                                    line=linetogrow((0,0,0),(obj.rect.center),(obj_b.rect.center),10,180)
                                    match_is_won=1

def checkwinglobal():
    if match_is_won==1:
        if game==4:
            button1.draw()      

def morpionsetup():
    global rows,columns,ecart,startposition,generationx,generationy,generationencoure,blocsagenerer,blocsizex,blocsizey
    rows=3
    columns=3
    ecart=2
    startposition=(screenhight-screenwidth)//2
    surfacedeblocsx,surfacedeblocsy=min(screenwidth,screenhight),min(screenwidth,screenhight)
    generationx=0
    generationy=startposition
    generationencoure=1
    blocsagenerer=rows*columns
    blocsizex=(surfacedeblocsx//rows)-ecart
    blocsizey=(surfacedeblocsy//columns)-ecart
    blocsetup()

def blocsetup():
    global screenwidth,startposition,surfacedeblocsx,generationx,generationy,generationencoure,rows
    if blocsnombre<blocsagenerer and generationencoure!=0:    
        for target in range(0,blocsagenerer):
            new_bloc=blocs(generationx,generationy,0,0)
            generationx+=blocsizex+ecart
            if generationx>surfacedeblocsx-((surfacedeblocsx%rows)+1):
                generationx=0
                generationy+=blocsizey+ecart

class linetogrow():
    all=[]
    def __init__(self,color,start_point, end_point,thickness, duration_frames):
        global drawable
        
        self.start_point = start_point
        self.end_point = end_point
        self.duration_frames = duration_frames
        self.frame=1
        self.color=color
        self.thickness=thickness
        self.vie=1
        self.current_length = []
        linetogrow.all.append(self)
        drawable.append(self)
        #self.draw_growing_line()

    def draw_growing_line(self):
        global controls_on
        if self.vie==1:
            # Calculate the direction vector from self.start_point to self.end_point
            direction = pygame.Vector2(self.end_point) - pygame.Vector2(self.start_point)
            desired_length = direction.length() # Calculate the desired final line length
            direction.normalize_ip()  # Normalize the vector
            
            length_increment =  desired_length/self.duration_frames # Calculate the line length increment per frame

            # Main animation loop
            # Calculate the current line length
            if self.frame<self.duration_frames:
                current_length = (length_increment * self.frame)

            # Calculate the new endpoint based on the current line length
                new_end_point = pygame.Vector2(self.start_point) + (direction * current_length)

            # Draw the line
                if self.frame < self.duration_frames : 
                    controls_on=0
                    pygame.draw.line(surface, self.color, self.start_point, new_end_point,self.thickness );self.frame +=1
            else: 
                pygame.draw.line(surface, self.color, self.start_point, self.end_point,self.thickness )
                controls_on=1
    def draw(self):
        self.draw_growing_line
    def reset(self):
        self.vie=0

class bacterie():
    all=[]
    def __init__(self,x,y,w,h):
        global blocsnombre,blocsizex,blocsizey,keys,chrono,drawable
        self.vie=1
        if w==0:
            self.width=blocsizex+1
        else : 
            self.width=w
        if h==0:    
            self.height=blocsizey+1
        else : 
            self.height=h
        self.tag=blocsnombre
        blocsnombre+=1
        self.random_color = random.choices(range(256), k=3)
        self.color=[]
        self.modifiable=0
        self.team=1
        self.birthcount = 0
        self.birthend = random.randint(30,180)
        self.modified_color=[]
        self.rect=pygame.Rect(x,y,self.width,self.height)
        
        self.gavebirth=0
        collisions=[]

        drawable.append(self)

        #action to execute
        bacterie.all.append(self)

    def draw(self):
        global blocsnombre,blocsizex,blocsizey,debug,keys,player,MOUSEBUTTONisDOWN,MOUSEBUTTONisUP,\
        mousex,mousey
        if self.vie==1:
            if self.modifiable==0:self.color="white"
            if self.modifiable==1:self.color="grey"
            if self.modifiable==2:self.color,self.modified_color=self.modified_color,self.color
            if self.team==1:self.modified_color="blue"
            if self.team==2:self.modified_color="red"
            if self.team==3:self.modified_color="green"
            if self.team==4:self.modified_color="yellow"
            pygame.draw.rect(surface,self.color,self.rect)
            if self.modifiable==3:    
                self.guivebirth()
            if debug ==1:
                text_surface = texte.render(f"{self.tag}", False, (255,0,0))
                surface.blit(text_surface, ((self.rect.centerx-15),(self.rect.centery-35)))
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                    if MOUSEBUTTONisDOWN==1:
                        if self.rect.collidepoint(pygame.mouse.get_pos()):
                            if self.modifiable==0:
                                self.modifiable=1
                    if MOUSEBUTTONisUP==1:
                        if self.modifiable==1:
                            pygame.mixer.music.load("point1.mp3")
                            pygame.mixer.music.play()
                            self.color,self.modified_color=self.modified_color,self.color
                            self.team=player
                            if player==4:player=1
                            else:player+=1
                            self.modifiable=3
            elif self.modifiable==1:
                    self.modifiable=0
        if self.vie==2:
            blocsnombre-=1
            self.vie=0
            self=mort()
                
    def reset(self):
        self.vie=1
        self.modifiable=0
        self.color="white"
        self.modified_color="white"
        self.gavebirth=0

    def guivebirth(self):
        global blocsizex,blocsizey,blocsnombre
        if self.gavebirth==0:
            if self.birthcount>self.birthend :
                for obj in bacterie.all :
                    if obj is not self:
                        if obj.rect.collidepoint(self.rect.midright[0]+self.rect.width//2 ,self.rect.midtop[1]-self.rect.height//2 ) :
                            self.topright_obj=obj
                        if obj.rect.collidepoint(self.rect.midleft[0]-self.rect.width//2 ,self.rect.midbottom[1]+self.rect.height//2 ):
                            self.bottomleft_obj=obj 
                        if obj.rect.collidepoint(self.rect.midright[0]+self.rect.width//2 ,self.rect.midbottom[1]+self.rect.height//2 ):
                            self.bottomright_obj=obj
                        if obj.rect.collidepoint(self.rect.midleft[0]-self.rect.width//2 ,self.rect.midtop[1]-self.rect.height//2 ) :
                            self.topleft_obj=obj 
                            if self in bacterie.all :
                                obj.modifiable=3
                                self.vie=2
                                self.gavebirth=1
                                newself=carre(self.rect.x,self.rect.y)
            else : self.birthcount+=1

def bacteriesetup():
    global screenwidth,startposition,surfacedeblocsx,generationx,generationy,generationencoure
    if blocsnombre<blocsagenerer and generationencoure!=0:    
        for target in range(0,blocsagenerer):
            new_bloc=bacterie(generationx,generationy,0,0)
            generationx+=blocsizex+ecart
            if generationx>surfacedeblocsx-1:
                generationx=0
                generationy+=blocsizey+ecart
    else:
        generationencoure=0

def stage_generation():
    global stagegeneration
    checkwinglobal()
    if stagegeneration==0:
        if game==1:
            for _ in carre.all:
                _.draw()
            blocsetup()
        if game==2:
            bacteriesetup()
            for _ in carre.all:
                _.draw()
        if game==3:
            carresetup()
        if game==4:
            morpionsetup()
        stagegeneration=1
    for _ in drawable:
        _.draw()
    for _ in linetogrow.all:
        _.draw_growing_line()

while run:
    
    chrono+=1
    timer.tick(60)
    keys=pygame.key.get_pressed()
    surface.fill(bgcolor)
    stage_generation()
    if controls_on==1:
        if keys[K_ESCAPE]:
            run=False
        if keys[K_SPACE]:
            score+=1
        if keys [K_r]:
            for _ in drawable:
                _.reset()
            match_is_won=0
        if keys[K_t]:
            checkwinglobal()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYUP:
            if event.key==K_F3:
                if debug!=2:
                    debug+=1
                else: debug=0
            if event.key==K_F1:
                if fpshow==1: 
                    fpshow=0
                else : fpshow=1
        if controls_on==1:
            if event.type == MOUSEBUTTONDOWN:
                MOUSEBUTTONisDOWN=1
            else:
                MOUSEBUTTONisDOWN=0
            if event.type == MOUSEBUTTONUP:
                MOUSEBUTTONisUP=1
            else:
                MOUSEBUTTONisUP=0
    checkwinglobal()
    pygame.display.flip()
pygame.quit()