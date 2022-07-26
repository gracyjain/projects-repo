# importing pygame as pg
import pygame as pg
# importing sys
import sys
# importing time
import time
# to generate random numbers
import random
# initializing pygame
pg.init()
# creating a screen


width=800
hight=800

screen=pg.display.set_mode((width,hight))
clock=pg.time.Clock()
color=(0,0,0)
box=pg.rect.Rect((width/2-40,770,100,20))
ball=[box.x+50,hight-40]
speed=10
last_time=time.time()
dt=0
target_fps=60
game_started=False
ball_speed=pg.Vector2((10,10))
game_lost=False
font=pg.font.Font("ARIALNB.TTF",20)
label_text=font.render("SCORE:0",(0,0,0),(0,0,0))
label_rect=label_text.get_rect()
label_rect.center=(80,20)

font2=pg.font.Font("ARIALNB.TTF",80)
over_text=font2.render("Game Over",(0,0,0),(255,0,0))
over_rect=over_text.get_rect()
over_rect.center=(400,400)

bg_img=pg.transform.scale(pg.image.load("greybg.jpg"),(800,800))
bg_rect=bg_img.get_rect()

score=0

def gameOver():
    screen.blit(over_text,over_rect)
    
    pg.display.update()
    pg.time.delay(5000)


def checkBallCollision(ball):
    global score
    global game_lost
    global label_text
    if ball[1]<=0:
        ball_speed.y=-ball_speed.y
    if ball[0]<=0 or ball[0]>=width:
        ball_speed.x=-ball_speed.x
    if (ball[0]>=box.x and ball[0]<=box.x+100) and (ball[1]>box.y-10):
        ball_speed.y=-ball_speed.y
        if game_started==True:
            score+=1
            label_text=font.render(f"SCORE:{score}",(0,0,0),(0,0,0))
    if ball[1]+10>=hight:
        game_lost=True
        gameOver()

while True:
    if game_lost==True:
       pg.time.delay(5000)
       break
    new_time=time.time()
    dt=new_time-last_time
    last_time=new_time 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE and game_started==False:
                game_started=True
                ball_speed.y=-ball_speed.y
                flag=random.randint(0,1)
                ball_speed.x=random.randint(5,10)
                if flag==0:
                    ball_speed.x=-ball_speed.x
                   


   
    
    
    # box.x+=speed*dt*target_fps
    keys=pg.key.get_pressed()
    # if keys[pg.K_UP]:
    #      box.y-=speed*dt*target_fps
    # if keys[pg.K_DOWN]:
    #      box.y+=speed*dt*target_fps
    if box.x>0:
        if keys[pg.K_LEFT]:
            box.x-=speed*dt*target_fps
            
    if box.x+80<width:       
        if keys[pg.K_RIGHT]:
            box.x+=speed*dt*target_fps
    
    if game_started==False:
        ball[0]=box.x+50

    else:
        ball[1]+=ball_speed.y*dt*target_fps
        ball[0]+=ball_speed.x*dt*target_fps

    checkBallCollision(ball)
    
    screen.blit(bg_img,bg_rect)
    screen.blit(label_text,label_rect)
    # screen.fill((255,255,255))
    
    pg.draw.circle(screen,(102,0,51),ball,10)
    pg.draw.rect(screen,color,box) 
    
    pg.display.update()
    # always use clock.tick in pygame
    clock.tick(60)  

        
            
