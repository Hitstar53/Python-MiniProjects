'''
Health Reminder System
'''
import datetime
import time
import pygame

def get_date():
    m = ""
    n = str(datetime.datetime.now())
    m = "[" + n + "] "
    return m

def playfile(type):
    pygame.mixer.init()
    pygame.mixer.music.load(f"D:\\Python-MiniProjects\\Mini Projects\\health-Reminder\\{type}.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    query = ' '
    while True:
        query = input("have you done your task?\n")
        if query.lower() == 'done':
            pygame.mixer.music.stop()
            break
        else:
            continue

'''
def remtype(type):
    if type == 'water':
        playfile(type)
    elif type == 'eye':
        playfile(type)
    elif type == 'physical':
        playfile(type)
'''

def logging(type):
    if type == 'water':
        with open('D:\\Python-MiniProjects\\Mini Projects\\health-Reminder\\drink_log.txt','a') as w:
            w.write(get_date())
            w.write("You drank 0.5 L of water!")
            w.write("\n")
    elif type == 'eye':
        with open('D:\\Python-MiniProjects\\Mini Projects\\health-Reminder\\eye_log.txt','a') as e:
            e.write(get_date())
            e.write("You did some eye exercise!")
            e.write("\n")
    elif type == 'physical':
        with open('D:\\Python-MiniProjects\\Mini Projects\\health-Reminder\\phys_log.txt','a') as p:
            p.write(get_date())
            p.write("You did some physical activity!")
            p.write("\n")

def remtime():
    hrlist = ['09','10','11','12','13','14','15','16','17']
    minlist3 = ['55','40','25','10']
    minlist2 = ['35','05']
    minlist1 = ['00']
    wc,ec,pc = 0,0,0
    print("THE HEALTH REMINDER SYSTEM IS NOW RUNNING!(9 AM TO 5 PM")
    while True:
        temp = datetime.datetime.now()
        temp1 = temp.strftime("%H:%M:%S")
        if temp1[0:2] not in hrlist:
            print("You are not in your work-hours currently!")
            break
        elif temp1[0:2] in hrlist and temp1[3:5] in minlist1 and temp1[6:8] == '00':
            type = 'water'
            playfile(type)
            logging(type)
            wc += 0.5
            continue
        elif temp1[0:2] in hrlist and temp1[3:5] in minlist2 and temp1[6:8] == '00' :
            type = 'eye'
            playfile(type)
            logging(type)
            ec += 1
            continue
        elif temp1[0:2] in hrlist and temp1[3:5] in minlist3 and temp1[6:8] == '00':
            if temp1[3:5] == '55' and pc in [0,4,8]:
                type = 'physical'
                playfile(type)
                logging(type)
                pc += 1
                continue
            elif temp1[3:5] == '40' and pc in [1,5,9]:
                type = 'physical'
                playfile(type)
                logging(type)
                pc += 1
                continue
            elif temp1[3:5] == '25' and pc in [2,6]:
                type = 'physical'
                playfile(type)
                logging(type)
                pc += 1
                continue
            elif temp1[3:5] == '10' and pc in [3,7]:
                type = 'physical'
                playfile(type)
                logging(type)
                pc += 1
                continue
        else:
            continue

if __name__ == '__main__':
    remtime()