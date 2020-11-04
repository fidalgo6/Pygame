import pygame, sys
from pygame.locals import *
from gameobjects.vector2 import Vector2
import math
import random 

pygame.init()

FPS = 30 
fpsClock = pygame.time.Clock()


screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption('Salve o Mundo')

font = pygame.font.SysFont('sans',80)
font2 = pygame.font.SysFont('sans',40)
placar = 0

WHITE = (255, 255, 255)
BLUE = (0, 51, 204)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)




lstElementos = ['Oxigenio','Bario','Helio','Potassio','Rubdio','Cesio','Francio','Hidrogenio','Litio','Sodio']


john = pygame.image.load('johny.png').convert_alpha()
john = pygame.transform.scale(john, (180, 120))
johnX = 10
johnY = 200

lstElementosFotos = []

for item in range(3):
      valor = random.randint(0, 9)
      lstElementosFotos.append([pygame.transform.scale(pygame.image.load(lstElementos[valor] + '.png').convert_alpha(),(100,60)),900,0,lstElementos[valor]])

     


class Player:
      def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio
      def update(self,x,y):
        self.x = x
        self.y = y

class Nave:
      def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio
      def update(self,x,y):
        self.x = x
        self.y = y        

class Bateria:
      def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio
      def update(self,x,y):
        self.x = x
        self.y = y

class Bala:
      def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio
      def update(self,x,y):
        self.x = x
        self.y = y          

class Enemy:
      def __init__(self,x,y,raio,nomeElemento):
        self.x = x
        self.y = y
        self.raio = raio
        self.nomeElemento = nomeElemento
      def update(self,x,y):
        self.x = x
        self.y = y        
        
def colisao(ast1, ast2):
    distancia =  math.sqrt( ((ast1.x-ast2.x)**2)+((ast1.y-ast2.y)**2) )
    if (ast1.raio + ast2.raio) >= distancia:
        print('Bateu')
        return True
    else:
        return False

class Background():
      def __init__(self):
            self.background = pygame.image.load('back.jpg')
            self.bgimage = pygame.transform.scale(self.background, (1000, 600))
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = 0
            self.bgX2 = self.rectBGimg.width
 
            self.moving_speed = 15
         
      def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
             
      def render(self):
         screen.blit(self.bgimage, (self.bgX1, self.bgY1))
         screen.blit(self.bgimage, (self.bgX2, self.bgY2))


back_ground = Background()

player = Player(johnX,johnY,20)

dicElementoEnemy = dict()


for item in lstElementosFotos:
      enemy = Enemy(item[1],item[2],15,item[3])
      dicElementoEnemy[item[3]] = enemy
      
elementoAmigo = lstElementos[random.randint(0,9)]

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execução a cada 1 segundo
temporizador = 120
temporizadorInimigos = 110

enviarAjuda = False


bateria = pygame.image.load('bateria.png').convert_alpha()
bateria = pygame.transform.scale(bateria, (140, 120))
bateriaX = 900
bateriaY = random.randint(0,500)
ajuda = Bateria(bateriaX,bateriaY,40)

naveInimiga = pygame.image.load('nave-inimiga.png').convert_alpha()
naveInimiga = pygame.transform.scale(naveInimiga, (80, 60))
naveInimigaX = 875
naveInimigaY = 102
nave = Nave(naveInimigaX,naveInimigaY,40)

naveInimiga2 = pygame.image.load('nave-inimiga.png').convert_alpha()
naveInimiga2 = pygame.transform.scale(naveInimiga2, (80, 60))
naveInimiga2X = 875
naveInimiga2Y = 500
nave2 = Nave(naveInimiga2X,naveInimiga2Y,40)

balaInimiga = pygame.image.load('bala.png').convert_alpha()
balaInimiga = pygame.transform.scale(balaInimiga, (50, 50))
balaInimigaX = 875
balaInimigaY = 0
bala = Bala(balaInimigaX,balaInimigaY,20)

balaInimiga2 = pygame.image.load('bala.png').convert_alpha()
balaInimiga2 = pygame.transform.scale(balaInimiga2, (50, 50))
balaInimiga2X = 875
balaInimiga2Y = 0
bala2 = Bala(balaInimiga2X,balaInimiga2Y,20)
      

while True: # the main game loop


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLOCKTICK:
            temporizador = temporizador -1
      
    if(placar >= 0 and temporizador >= 0):
          back_ground.update()
          back_ground.render()


          keys = pygame.key.get_pressed()
          if keys[pygame.K_UP]:
              johnY -= 5
              if johnY < -10:
                  johnY += 5      
          if keys[pygame.K_DOWN]:
              johnY += 5
              if johnY > 515:
                  johnY -= 5              
          if keys[pygame.K_LEFT]:
              johnX -= 5
              if johnX < -10:
                  johnX += 5         
          if keys[pygame.K_RIGHT]:
              johnX += 5
              if johnX > 900:
                  johnX -= 5

          score = font2.render('Placar: ' + str(placar), True, (WHITE))
          screen.blit(score, (800, 50))

          timer1 = font2.render('Tempo: ' + str(temporizador), True, (YELLOW))
          screen.blit(timer1, (50, 50))

          elementoACapturar = font2.render('Capture: ' + elementoAmigo, True, (WHITE))
          screen.blit(elementoACapturar, (350, 50))

          if(len(lstElementosFotos) == 0):
            for item in range(3):
                  valor = random.randint(0, 9)
                  lstElementosFotos.append([pygame.transform.scale(pygame.image.load(lstElementos[valor] + '.png').convert_alpha(),(100,60)),900,0,lstElementos[valor]])
            for item in lstElementosFotos:
                  enemy = Enemy(item[1],item[2],20,item[3])
                  dicElementoEnemy[item[3]] = enemy            

          for item in lstElementosFotos:
                  if(item[2] == 0):
                        item[2] = random.randint(0,500)
                  if(item[1] < 0):
                        lstElementosFotos = []
                        item[1] = 900
                        item[2] = 0
                  item[1] -= 5
                  screen.blit(item[0], (item[1], item[2]))
                  dicElementoEnemy.get(item[3]).update(item[1],item[2])

                  if(colisao(player,dicElementoEnemy.get(item[3]))):
                        if(dicElementoEnemy.get(item[3]).nomeElemento == elementoAmigo):
                              placar += 10
                              item[1] = 900                        
                              item[2] = 0
                              elementoAmigo = lstElementos[random.randint(0,1)]
                              lstElementosFotos = []
                              score = font2.render('Placar: ' + str(placar), True, (BLUE))
                              screen.blit(score, (800, 50))
                              pygame.mixer.music.load('catch.mp3')
                              pygame.mixer.music.play(0)                              
                        else:
                              placar -= 10
                              item[1] = 900                        
                              item[2] = 0                                        
                              score = font2.render('Placar: ' + str(placar), True, (RED))
                              screen.blit(score, (800, 50))

          if(temporizador < 58):
            bateriaX -= 5
            if(bateriaX < 0):
                  bateriaX = 900
                  bateriaY = random.randint(0,500)
            enviarAjuda = True

          if(enviarAjuda == True):
            ajuda.update(bateriaX,bateriaY)
            if(colisao(player,ajuda)):
                  temporizador += 2
                  bateria = pygame.image.load('bateria.png').convert_alpha()
                  bateria = pygame.transform.scale(bateria, (140, 120))
                  bateriaX = 900
                  bateriaY = random.randint(0,500)
                  ajuda = Bateria(bateriaX,bateriaY,40)                
            screen.blit(bateria,(bateriaX,bateriaY))
            enviarAjuda = False

          player.update(johnX,johnY)
          screen.blit(john, (johnX, johnY))




          if(naveInimigaY > 600):
                naveInimigaY = 0
          if(balaInimigaY > 600):
                balaInimigaY = naveInimigaY
                balaInimigaX = naveInimigaX
          if(temporizador < temporizadorInimigos):
                balaInimigaX -= 10
                balaInimigaY += 5
                naveInimigaY += 5                 
                screen.blit(naveInimiga, (naveInimigaX,naveInimigaY))
                screen.blit(balaInimiga, (balaInimigaX, naveInimigaY))
                bala.update(balaInimigaX,balaInimigaY)
                nave.update(naveInimigaX,naveInimigaY)

          if(colisao(player,bala)):
                placar -= 10               
                screen.blit(balaInimiga, (balaInimigaX, naveInimigaY))
                bala.update(balaInimigaX,balaInimigaY)


          if(naveInimiga2Y < 0):
                naveInimiga2Y = 500
          if(balaInimiga2Y < 0):
                balaInimiga2Y = naveInimiga2Y
                balaInimiga2X = naveInimiga2X
          if(temporizador < temporizadorInimigos):
                balaInimiga2X -= 10
                balaInimiga2Y -= 5
                naveInimiga2Y -= 5                 
                screen.blit(naveInimiga2, (naveInimiga2X,naveInimiga2Y))
                screen.blit(balaInimiga2, (balaInimiga2X, naveInimiga2Y))
                bala2.update(balaInimiga2X,balaInimiga2Y)
                nave2.update(naveInimiga2X,naveInimiga2Y)

          if(colisao(player,bala2)):
                placar -= 10               
                screen.blit(balaInimiga2, (balaInimiga2X, naveInimiga2Y))
                bala2.update(balaInimiga2X,balaInimiga2Y)                 
                
    
    else:
      background_image = pygame.image.load("back.jpg").convert()
      background_image = pygame.transform.scale(background_image, (1000, 600))
      screen.blit(background_image, [0, 0])
      textoFim = 'Fim de Jogo'
      textoPlacar = 'Placar final: '
      textoFinal = font.render(textoFim, True, (WHITE))
      placarFinal = font2.render(textoPlacar + str(placar) , True, (WHITE))
      screen.blit(textoFinal, (300, 120))
      screen.blit(placarFinal, (380, 320))
   
    


    pygame.display.update()
    fpsClock.tick(FPS)
