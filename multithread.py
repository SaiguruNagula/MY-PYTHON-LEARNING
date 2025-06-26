# multithreading : Used to preform multiple task at the same time (mutlitasking)
#                  good for I/o bound task like getting input or fetching data from API
#    SYNTAX      : threading.thread(target= my_function)      


import threading
import time
import datetime
import AlarmClock___ as al
import pygame

def bed_clean(timeforcleaning):
     timecl = timeforcleaning
     al.alarm(timecl,"bed cleaning")

     print("time up clean ur bed ")

def trash_throw(timefor):
     timecl2= timefor
     al.alarm(timecl2, "trash throwing")
     print("throw ur trash")
    

set_time1 = input('enter the time to clean the bed  : ')
set_time2 = input('enter the time to throw the trash: ')

chore1 = threading.Thread(target= bed_clean, args =( set_time1,))
chore1.start()

chore2 = threading.Thread(target= trash_throw,args =( set_time2,))
chore2.start()