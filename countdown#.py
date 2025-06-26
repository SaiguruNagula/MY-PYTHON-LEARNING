import time

my_time = int(input ("Enter the time in seconds: "))
print("Countdown starts now...")

for x in range ( my_time , 0 , -1 ):
    seconds = x%60
    minutes = (x/60)%60
    hours = (x/3600)%24

    print(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}", end="\r")
    time.sleep(1)
print("Time's up!") 