import time 
import datetime
import pygame


def alarm(alarmtime,*args, musName):
    print(f"alarm is set for {alarmtime}")
    file_path = "bensound-hope.mp3"
    is_running = True

    while is_running:
     currenttime = datetime.datetime.now()
     currenttime = currenttime.strftime("%H:%M:%S")
     print(f"current time : {currenttime} ", end ="\r")
     
     if currenttime==alarmtime:
        print("\n")
        print(f'wake up , time for {args} ')
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
       
        while pygame.mixer.music.get_busy():
           time.sleep(1)

        is_running= False


     time.sleep(1)

if __name__ == "__main__":
     
     alarmtime = input("set alarm time : ")

     alarm(alarmtime,("clean bed") )
         

    
    