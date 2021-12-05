i = 0
j = 0
k = 0
import pygame
import time
import datetime
initial = time.time()
listwater = [['13','05'],['11','00'],['12','00'],['13','00'],['14','00'],['15','00'],['16','00'],['17','00']]
listeye = [['13','06'],['10','00'],['10','30'],['11','00'],['11','30'],['12','00'],['12','30'],['13','00'],['13','30'],['14','00'],['14','30'],['15','00'],['15','30'],['16','00'],['16','30'],['17','00']]
listphysical = [['13','07'],['10','30'],['11','15'],['12','00'],['12','45'],['13','30'],['14','15'],['15','00'],['15','45'],['16','30']]
'''
To drink a total of 3.5-liter water after some
 time interval between 9-5 pm.
To do eye exercise after every 30 minutes.
To perform physical activity after every 45 minutes
'''
def playfile(type):
    pygame.mixer.init()
    pygame.mixer.music.load(f"{type}.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    while True:
        query = input("have you done your task")
        if query.lower() == 'done':
            pygame.mixer.music.stop()
            break
        else:
            pygame.mixer.music.play()
            continue

def remtype(type):
    if type == "water":
        playfile(type)
    elif type == "eye":
        playfile(type)
    elif type == "physical":
        playfile(type)

def remtime():
    i,j,k= 0,0,0
    while True:
        temp = datetime.datetime.now()
        temp = temp.strftime("%H:%M:%S")
        if temp[0:2] == listwater[i][0] and temp[3:5] == listwater[i][1]:
            remtype("water")
            i +=1
            pass
        elif temp[0:2] == listeye[j][0] and temp[3:5] == listeye[j][1]:
            remtype("eye")
            j +=1
            pass
        elif temp[0:2] == listphysical[k][0] and temp[3:5] == listphysical[k][1]:
            remtype("physical")
            k +=1
            pass
        time.sleep(30)


remtime()