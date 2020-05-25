import pygame, sys
from pygame.locals import *
from easygui import *
import random #in this program to randomly select a position in 4*4 list

# set up the window
DISPLAYSURF = ''

 # set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
YELLOW1= (  0,   255, 100)
NAVY_BLUE=(0,0,128)
LIME=(0,128,0)
MAROON=(128,0,0)
AQUA=(0,0,192)
FUCHSIA=(255,255,0)
YELLOW=(0,255,255)
PURPLE=(255,0,255)
GRAY=(128,128,128)
SILVER=(192,192,192)
BASICFONT = ''

#----------Game Initialization section begins----------
points = 0
game_box = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #initially making the 4*4 array's value 0 or "nothing" for all positions
first_position_list = [0,1,2,3]
first_row_to_begin = random.choice(first_position_list)
first_column_to_begin = random.choice(first_position_list)
while True:
        second_row_to_begin = random.choice(first_position_list)
        second_column_to_begin = random.choice(first_position_list)
        if second_row_to_begin!=first_row_to_begin and second_column_to_begin!=first_column_to_begin:
                game_box[second_row_to_begin][second_column_to_begin]=2
                break
game_box[first_row_to_begin][first_column_to_begin] = 2 
f=open('score.txt','r')

highscore=0
for line in f:
        highscore=int(line)

#----------Game Initialization Completes----------
 
#----------left movement function begins----------
def left_movement(game_box): #function for left movement
    i=0
    moved=False
    for j in range(0,4): #looping through all the rows
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0: 
            if game_box[i][j]==0: 
                while game_box[i][j] == 0: 
                    game_box[i][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
                    moved=True
                     
            if game_box[i+1][j]==0 and (game_box[i+2][j]!=0 or game_box[i+3][j]!=0): 
                while game_box[i+1][j]==0: 
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
                    moved=True
                    
            if game_box[i+2][j] == 0 and game_box[i+3][j]!=0: 
                while game_box[i+2][j]==0: 
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
                    moved=True
    return moved

#----------left movement function ends----------
 
#----------Addition function after left movement begins----------
def left_addition(game_box,points): #function for left addition after left movement
    i=0
    added=False
    for j in range(0,4): #looping through all the rows
        if game_box[i][j]==game_box[i+1][j] and game_box[i][j]!=0: 
            game_box[i][j]=game_box[i][j]+game_box[i+1][j]
            points += game_box[i][j] * 2 
            game_box[i+1][j]=game_box[i+2][j] 
            game_box[i+2][j]=game_box[i+3][j] 
            game_box[i+3][j]=0 
            added=True
            
        if game_box[i+1][j]==game_box[i+2][j] and game_box[i+1][j]!=0: 
            game_box[i+1][j]=game_box[i+1][j]+game_box[i+2][j] 
            points += game_box[i+1][j] * 2 
            game_box[i+2][j]=game_box[i+3][j] 
            game_box[i+3][j]=0 
            added=True
            
        if game_box[i+2][j]==game_box[i+3][j] and game_box[i+2][j]!=0: 
            game_box[i+2][j]=game_box[i+2][j]+game_box[i+3][j] 
            points += game_box[i+2][j] * 2 
            game_box[i+3][j]=0 
            added=True
    
    return points,added
 
#----------Addition function after right movement ends----------
                                         
#----------right movement function begins----------
 
def right_movement(game_box): #function for right movement
    i=0
    moved=False
    for j in range(0,4): #looping through all the rows
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0: 
            if game_box[i+3][j]==0: 
                while game_box[i+3][j]==0: 
                    game_box[i+3][j]=game_box[i+2][j]
                    game_box[i+2][j]=game_box[i+1][j]
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
                    moved=True
                    
            if game_box[i+2][j]==0 and (game_box[i+1][j]!=0 or game_box[i][j]!=0): 
                while game_box[i+2][j]==0: 
                    game_box[i+2][j]=game_box[i+1][j]
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
                    moved=True
                    
            if game_box[i+1][j]==0 and game_box[i][j]!=0: 
                while game_box[i+1][j]==0: 
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
                    moved=True
    return moved
#----------right movement function ends----------
                                         
#----------Addition function after right movement begins----------
 
def right_addition(game_box,points): #function for right addition after right movement
    i=0
    added=False
    for j in range(0,4): #looping through all the rows
        if game_box[i+3][j]==game_box[i+2][j] and game_box[i+3][j]!=0: 
            game_box[i+3][j]=game_box[i+3][j] + game_box[i+2][j] 
            points += game_box[i+3][j] * 2 
            game_box[i+2][j]=game_box[i+1][j] 
            game_box[i+1][j]=game_box[i][j] 
            game_box[i][j]=0 
            added=True
            
        if game_box[i+2][j]==game_box[i+1][j] and game_box[i+2][j]!=0: 
            game_box[i+2][j]=game_box[i+2][j]+game_box[i+1][j] 
            points += game_box[i+2][j] * 2 
            game_box[i+1][j]=game_box[i][j] 
            game_box[i][j]=0 
            added=True
            
        if game_box[i+1][j]==game_box[i][j] and game_box[i+1][j]!=0: 
            game_box[i+1][j]=game_box[i+1][j]+game_box[i][j] 
            points += game_box[i+1][j] * 2 
            game_box[i][j]=0 
            added=True
            
    return points,added
 
#----------Addition function after right movement ends----------
 
#----------upward movement function begins----------
 
def up_movement(game_box): #function for up movement
    j=0
    moved=False
    for i in range(0,4): #looping through all the columns
 
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0: 
            if game_box[i][j]==0: 
                while game_box[i][j]==0: 
                    game_box[i][j]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3]=0
                    moved=True
                    
            if game_box[i][j+1]==0 and (game_box[i][j+2]!=0 or game_box[i][j+3]!=0): 
                while game_box[i][j+1]==0: 
                    game_box[i][j+1]=game_box[i][j+2]
                    game_box[i][j+2]=game_box[i][j+3]
                    game_box[i][j+3]=0
                    moved=True
                    
            if game_box[i][j+2]==0 and (game_box[i][j+3]!=0): 
                while game_box[i][j+2]==0: 
                    game_box[i][j+2]=game_box[i][j+3]
                    game_box[i][j+3]=0
                    moved=True
    return moved  
#----------up movement function ends----------
                                         
#----------Addition function after up movement begins----------
                                         
def up_addition(game_box,points): #function for up addition after up movement
    j=0
    added=False
    for i in range(0,4): #looping through all the columns
        if game_box[i][j]==game_box[i][j+1] and game_box[i][j]!=0: 
            game_box[i][j]=game_box[i][j]+game_box[i][j+1] 
            points += game_box[i][j] * 2 
            game_box[i][j+1]=game_box[i][j+2] 
            game_box[i][j+2]=game_box[i][j+3] 
            game_box[i][j+3]=0 
            added=True
            
        if game_box[i][j+1]==game_box[i][j+2] and game_box[i][j+1]!=0: 
            game_box[i][j+1]=game_box[i][j+1]+game_box[i][j+2] 
            points += game_box[i][j+1] * 2 
            game_box[i][j+2]=game_box[i][j+3] 
            game_box[i][j+3]=0 
            added=True
            
        if game_box[i][j+2]==game_box[i][j+3] and game_box[i][j+2]!=0: 
            game_box[i][j+2]=game_box[i][j+2]+game_box[i][j+3] 
            points += game_box[i][j+2] * 2 
            game_box[i][j+3]=0 
            added=True
            
    return points,added
                                         
#----------Addition function after up movement ends----------
                                         
#----------downward movement function begins----------
 
def down_movement(game_box): #function for down movement
    j=0
    moved=False
    for i in range(0,4): #looping through all the columns
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0: 
            if game_box[i][j+3]==0: 
                while game_box[i][j+3]==0: 
                    game_box[i][j+3]=game_box[i][j+2]
                    game_box[i][j+2]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
                    moved=True
                    
            if game_box[i][j+2]==0 and (game_box[i][j+1]!=0 or game_box[i][j]!=0): 
                while game_box[i][j+2]==0: 
                    game_box[i][j+2]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
                    moved=True
 
            if game_box[i][j+1]==0 and game_box[i][j]!=0: 
                while game_box[i][j+1]==0: 
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
                    moved=True
    return moved
 
#----------down movement function ends----------
                                 
#----------Addition function after down movement begins----------
 
def down_addition(game_box,points): #function for down addition after down movement
    j=0
    added=False
    for i in range(0,4): #looping through all the columns
        if game_box[i][j+3]==game_box[i][j+2] and game_box[i][j+3]!=0: 
            game_box[i][j+3]=game_box[i][j+3] + game_box[i][j+2] 
            points += game_box[i][j+3] * 2 
            game_box[i][j+2]=game_box[i][j+1] 
            game_box[i][j+1]=game_box[i][j] 
            game_box[i][j]=0 
            added=True
            
        if game_box[i][j+2]==game_box[i][j+1] and game_box[i][j+2]!=0: 
            game_box[i][j+2]=game_box[i][j+2]+game_box[i][j+1] 
            points += game_box[i][j+2] * 2 
            game_box[i][j+1]=game_box[i][j] 
            game_box[i][j]=0 
            added=True
            
        if game_box[i][j+1]==game_box[i][j] and game_box[i][j+1]!=0: 
            game_box[i][j+1]=game_box[i][j+1]+game_box[i][j] 
            points += game_box[i][j+1] * 2 
            game_box[i][j]=0 
            added=True
            
    return points,added                                    
#----------Addition function after down movement ends----------
 
def check(game_box):
    for i in range(4):
        for j in range(4):
            if i==0 and j==0:
                if game_box[i][j]==game_box[i+1][j] or game_box[i][j]==game_box[i][j+1]:
                    return True
            if i==0 and j==3:
                if game_box[i][j]==game_box[i+1][j] or game_box[i][j]==game_box[i][j-1]:
                    return True
            if i==3 and j==0:
                if game_box[i][j]==game_box[i-1][j] or game_box[i][j]==game_box[i][j+1]:
                    return True
            if i==3 and j==3:
                if game_box[i][j]==game_box[i-1][j] or game_box[i][j]==game_box[i][j-1]:
                    return True
            if i==0 and j>0 and j<3:
                if game_box[i][j]==game_box[i+1][j] or game_box[i][j]==game_box[i][j-1] or game_box[i][j]==game_box[i][j+1]:
                    return True
            if j==0 and i>0 and i<3:
                if game_box[i][j]==game_box[i-1][j] or game_box[i][j]==game_box[i+1][j] or game_box[i][j]==game_box[i][j+1]:
                    return True
            if i==3 and j>0 and j<3:
                if game_box[i][j]==game_box[i-1][j] or game_box[i][j]==game_box[i][j-1] or game_box[i][j]==game_box[i][j+1]:
                    return True
            if j==3 and i>0 and i<3:
                if game_box[i][j]==game_box[i-1][j] or game_box[i][j]==game_box[i+1][j] or game_box[i][j]==game_box[i][j-1]:
                    return True
            if j>0 and j<3 and i>0 and i<3:
                if game_box[i][j]==game_box[i-1][j] or game_box[i][j]==game_box[i+1][j] or game_box[i][j]==game_box[i][j-1] or game_box[i][j]==game_box[i][j+1]:
                    return True
    return False


def drawboard(gamebox,DISPLAYSURF,BASICFONT):
    j=0
    COLOR=[GRAY,AQUA,RED,NAVY_BLUE,MAROON,YELLOW1,PURPLE,YELLOW,LIME,FUCHSIA,GREEN,WHITE]
    pygame.draw.rect(DISPLAYSURF, BLACK, (50,50,380,380),2)
    for x in range(4):
        for y in range(4):
            if gamebox[x][y]==0:
                j=0
            else:
                for i in range(1,12):
                    if gamebox[x][y]==2**i:
                        j=i
                        break
            pygame.draw.rect(DISPLAYSURF, COLOR[j], (70+(x*90), 70+(y*90), 70, 70))
            # Select the font to use, size, bold, italics
            font = pygame.font.SysFont('Calibri', 25, True, False)
            s=""
            if gamebox[x][y]>0:
                s=str(gamebox[x][y])
            text = font.render(s,True,BLACK)
            # Put the image of the text on the screen
            DISPLAYSURF.blit(text, [80+(x*90), 85+(y*90)])
    

def drawscore(points,highscore,DISPLAYSURF,BASICFONT):
    DISPLAYSURF.fill(SILVER, (450, 100, 300, 400))
    scoreImg = BASICFONT.render("Score:"+str(points), False, BLACK)
    DISPLAYSURF.blit(scoreImg, [500,100])
    if highscore<points:
        highscore=points
    highscoreImg = BASICFONT.render("High Score:"+str(highscore), False, BLACK)
    DISPLAYSURF.blit(highscoreImg, [450,300])

def restart(game_box,points,highscore,f,DISPLAYSURF,BASICFONT):
                                # draw on the surface object
                                DISPLAYSURF.fill(SILVER)
                        
                                #----------Game Initialization section begins----------
                                game_box = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #initially making the 4*4 array's value 0 or "nothing" for all positions
                                first_position_list = [0,1,2,3]
                                first_row_to_begin = random.choice(first_position_list)
                                first_column_to_begin = random.choice(first_position_list)
                                while True:
                                        second_row_to_begin = random.choice(first_position_list)
                                        second_column_to_begin = random.choice(first_position_list)
                                        if second_row_to_begin!=first_row_to_begin and second_column_to_begin!=first_column_to_begin:
                                                game_box[second_row_to_begin][second_column_to_begin]=2
                                                break
                                game_box[first_row_to_begin][first_column_to_begin] = 2 #placing the first 2 to begin the game in position selected randomly
                                points=0        
                                
                                f=open('score.txt','r')
                                for line in f:
                                        highscore=int(line)             
                                main(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)


def run(game_box,points,highscore,f,DISPLAYSURF,BASICFONT):
    row_indexes_with_zero = []
    column_indexes_with_zero = []
    for i in range(0,4):
        for j in range(0,4):
            if game_box[i][j] == 0:
                row_indexes_with_zero.append(i)
                column_indexes_with_zero.append(j)
            if game_box[i][j] == 2048:
                drawboard(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                drawscore(points,highscore,DISPLAYSURF,BASICFONT)
                pygame.mixer.music.load('Metroid_Door.wav')
                pygame.mixer.music.play(1)
                if ccbox("Congratulations you have achieved the 2048 tile!!Your score is "+str(points)+".Do you want to restart the game?", title="Result",choices=('Yes','No')):
                                if highscore<=points:
                                                fw=open('score.txt','r+')
                                                fw.write(str(points))
                                                fw.close()
                                restart(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                else:
                                if ccbox("Do you want to quit?", title="Verify",choices=('Yes','No')):
                                        f.close()
                                        
                                        if highscore<=points:
                                                fw=open('score.txt','r+')
                                                fw.write(str(points))
                                                fw.close()                                      
                                        pygame.quit()
                                        sys.exit()
                                else:
                                        if highscore<=points:
                                                fw=open('score.txt','r+')
                                                print (highscore)
                                                fw.write(str(points))
                                                fw.close()
                                        pygame.quit()
                                        menu(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                break
    if len(row_indexes_with_zero) > 1:
        while True:
                random_index = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))
                row_to_place_entry = row_indexes_with_zero[random_index]
                column_index=column_indexes_with_zero.index(random.choice(column_indexes_with_zero))
                column_to_place_entry = column_indexes_with_zero[column_index]
                if game_box[row_to_place_entry][column_to_place_entry]==0:
                        break
        game_box[row_to_place_entry][column_to_place_entry] = 2
        drawboard(game_box,DISPLAYSURF,BASICFONT)
        drawscore(points,highscore,DISPLAYSURF,BASICFONT)
    elif len(row_indexes_with_zero) == 1:
        row_to_place_entry = row_indexes_with_zero[0]
        column_to_place_entry = column_indexes_with_zero[0]
        game_box[row_to_place_entry][column_to_place_entry] = 2
        drawboard(game_box,DISPLAYSURF,BASICFONT)
        drawscore(points,highscore,DISPLAYSURF,BASICFONT)
    else:
        if not check(game_box):
                        pygame.mixer.music.load('Metroid_Door.wav')
                        pygame.mixer.music.play(1)
                        if ccbox("You have lost the game!!Your score is "+str(points)+".Do you want to restart the game?", title="Result",choices=('Yes','No')):
                                if highscore<=points:
                                                fw=open('score.txt','r+')
                                                fw.write(str(points))
                                                fw.close()
                                restart(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                        else:
                                if ccbox("Do you want to quit?", title="Verify",choices=('Yes','No')):
                                        f.close()
                                        if highscore<=points:
                                                fw=open('score.txt','r+')
                                                fw.write(str(points))
                                                fw.close()                                      
                                        pygame.quit()
                                        sys.exit()
                                else:
                                        if highscore<=points:
                                                fw=open('score.txt','r+')
                                                print (highscore)
                                                fw.write(str(points))
                                                fw.close()
                                        pygame.quit()
                                        menu(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                
        else:
            drawboard(game_box,DISPLAYSURF,BASICFONT)
            drawscore(points,highscore,DISPLAYSURF,BASICFONT)

def main(game_box,points,highscore,f,DISPLAYSURF,BASICFONT):
    drawboard(game_box,DISPLAYSURF,BASICFONT)
    drawscore(points,highscore,DISPLAYSURF,BASICFONT)
    while True:
        for event in pygame.event.get():
             if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                 if not ccbox("Your score is "+str(points)+".Do you want to continue the game?", title="Result",choices=('Yes','No')):
                                if highscore<=points:
                                                fw=open('score.txt','r+')
                                                fw.write(str(points))
                                                fw.close() 
                                pygame.quit()
                                menu(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
             if event.type == pygame.KEYDOWN:
                pygame.mixer.music.load('Pop Clip In.wav')
                pygame.mixer.music.play(1)
                if event.key == pygame.K_LEFT:
                    moved=left_movement(game_box)
                    points,added=left_addition(game_box,points)
                    print(moved,added)
                    if moved or added:
                            run(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                
                if event.key == pygame.K_RIGHT:
                    moved=right_movement(game_box)
                    points,added=right_addition(game_box,points)
                    print(moved,added)
                    if moved or added:
                            run(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                            
                if event.key == pygame.K_UP:
                    moved=up_movement(game_box)
                    points,added=up_addition(game_box,points)
                    if moved or added:
                            run(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                            
                if event.key == pygame.K_DOWN:
                    moved=down_movement(game_box)
                    points,added=down_addition(game_box,points)
                    if moved or added:
                            run(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
                
        pygame.display.update()

def menu(game_box,points,highscore,f,DISPLAYSURF,BASICFONT):
    pygame.init()
    pygame.mixer.music.load('CARTOONY.wav')
    pygame.mixer.music.play(-1)
    reply=buttonbox('','2048 - Get me if u can??',('Play','Instructions','Quit'),'download.png')
    if reply=='Play':
            pygame.mixer.music.stop()
            DISPLAYSURF = pygame.display.set_mode((700, 500), 0, 32)
            pygame.display.set_caption('2048 - Get me if u can??')
            DISPLAYSURF.fill(SILVER)
            BASICFONT = pygame.font.SysFont('Calibri', 30,True,False)
            restart(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
    elif reply=='Instructions':
            textbox('Instructions are as follows:','Instructions for 2048 game',"The points will be rewarded in a format 'tile number after joining * 2' eg>>>> 2 2 8 16 >>>>left movement>>>4 8 16 0 >>>>>points = 4*2\n"+
                    "Press left arrow key for moving tiles towards left.\n"+
                    "Press right arrow key for moving tiles towards right.\n"+
                    "Press up arrow key for moving tiles towards up.\n"+
                    "Press down arrow key for moving tiles towards down.\n")
            menu(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
    elif reply=='Quit':
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
    else:
            pygame.mixer.music.stop()
            sys.exit()
            
if __name__=='__main__':
    menu(game_box,points,highscore,f,DISPLAYSURF,BASICFONT)
    
    
