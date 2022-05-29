import time
def countdown(t):
    while t:
        hours,mins = divmod(t,60)
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
        print(timer,end = "\r")
        time.sleep(1)
        t -=1
    
    print("timer complteed!")

t = input ('enter the time in seconds: ')

countdown(int(t))
