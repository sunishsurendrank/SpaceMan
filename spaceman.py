import random
import pygame
import time
import sys

"""
- Developer : Sunish Surendran Kannembath
- Reach Sunish in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
- Reach Sunish in Twitter : @sunishsurendran
"""


def CreatePipe():
    global score
    gap = 300
    pipe_color = (127,127,127)#(0,255,0)
    pipe_width = 50
    pygame.draw.rect(window,pipe_color,(pipe[0], 0, pipe_width, pipe[1]))
    pygame.draw.rect(window,pipe_color,(pipe[0], pipe[1]+gap, pipe_width, 720))
    pipe[0] = pipe[0] - 5
    if pipe[0] < -50:
        pipe[0] = 720
        pipe[1] = random.randint(0,380)
        score = score + 1

def SpaceBarEvent():
    global jump,start,y_axis,start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = 7
                if start == False:
                    y_axis = 400
                    start = True
                    time.sleep(1)

def Character():
    global y_axis,jump
    global window
    global character_image,start
    window.blit(character_image,(50,y_axis))
    y_axis = y_axis - jump
    jump = jump - 0.5

def HitCondition():
    global y_axis,pipe
    if (pipe[0] < 164 and pipe[0] > 14) and (y_axis+100 > pipe[1]+300 or y_axis < pipe[1]):
        return True


if __name__ == "__main__":


    pygame.init()
    window              = pygame.display.set_mode((620,620))
    clock               = pygame.time.Clock()
    pipe                = [620,random.randint(0,380)]
    y_axis              = 100
    jump                = 0
    score               = 0
    start               = True
    stop                = False
    title_font          = pygame.font.SysFont('Arial', 50)
    message_font        = pygame.font.SysFont('Arial', 20)
    score_font          = pygame.font.SysFont('Arial', 20)
    character_image     = pygame.image.load("./images/character2.png")
    gameover_image      = pygame.image.load("./images/gameover.png")
    background_image    = pygame.image.load("./images/background.jpg")

    while True:
        #check any spacebar press event happned
        SpaceBarEvent()
        
        #Start the Game
        if start:

            window.fill((120,120,255))
            window.blit(background_image,(0,0))
            Character()
            CreatePipe()
            window.blit(score_font.render('Score: ' + str(score), True, (255,255,255), None),(10,10))

        #Check Whether the charchter hit the pipe
        retrun_value = HitCondition()

        #If the character hit the pipe then show gameover
        if retrun_value:
            window.blit(gameover_image,(160,160))
            caption = message_font.render('Press spacebar to continue playing', True, (255,255,255), None)
            window.blit(caption,(180,320))
            start   = False
            stop    = True
            pipe[0] = 720

        #clock tick decised the frames per second
        clock.tick(60)
        pygame.display.flip()
