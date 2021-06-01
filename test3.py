from pygame import *
from random import randint
from time import sleep
 
window = display.set_mode((700, 500))
display.set_caption("Поймай яблоко")
background = transform.scale(image.load("c:\\test\\background.jpg"), (700, 500))

font.init()
font1=font.Font(None,36)
font2=font.Font(None,150)
lost=0
score=0
 
#Стртовые координаты
x1 = 100
y1 = 300
 
x2 = 300
y2 = 300
 
sprite1 = transform.scale(image.load('c:\\test\\Grisha.png'), (100, 100))
sprite2 = transform.scale(image.load('c:\\test\\apple.png'), (100, 100))
ts1=sprite1.get_rect()
ts1.x=x1
ts1.y=y1
ts2=sprite2.get_rect()
ts2.x=x2
ts2.y=y2
speed = 10
 
#игровой цикл
run = True
clock = time.Clock()
FPS = 60
 
while run:
   window.blit(background,(0, 0))
   window.blit(sprite1, ts1)
   window.blit(sprite2, ts2)
 
   for e in event.get():
       if e.type == QUIT:
           run = False
 
   keys_pressed = key.get_pressed()
 
   if keys_pressed[K_LEFT] and x1 > 5:
       x1 -= speed
   if keys_pressed[K_RIGHT] and x1 < 695:
       x1 += speed
   if keys_pressed[K_UP] and y1 > 5:
       y1 -= speed
   if keys_pressed[K_DOWN] and y1 < 495:
       y1 += speed
  
   y2=y2+10  # падение яблока
   #--------------------Проверка падения блока-----------------------------
   if y2>500:
       y2=0
       x2=randint(10,600)
       lost+=1
    #-------------------Проверка столкновения------------------------------------
   if ts1.colliderect(ts2):
       y2=0
       x2=randint(10,600)
       score+=1
    #--------------------------------------------------------------
   ts1.x=x1
   ts1.y=y1
   ts2.x=x2
   ts2.y=y2
   score_t=font1.render("Поймано:"+str(score),1,(0,0,0))
   window.blit(score_t,(10,20))
   lost_t=font1.render("Пропушено:"+str(lost),1,(0,0,0))
   window.blit(lost_t,(10,50))
   #------------------Ситуация выигрыша------------------------
   if score>=1:
      window.fill((255,255,255))
      win=font2.render("Победа!",1,(0,255,0))
      window.blit(win,(150,200))
      run=False
   #------------------Ситуация проигрыша------------------------
   if lost>=3:
      los=font2.render("Ты проиграл",1,(255,0,0))
      window.fill((0,0,0))
      window.blit(los,(20,200))
      run=False

   display.update()
   clock.tick(FPS)
sleep(3)

 
