import time

sleep_time = int(input("How long do you want to wait before running?: "))

while sleep_time > 0:

    print(sleep_time, end="\r")
    time.sleep(1)
    sleep_time -= 1
print("Time to go for a run!!!")
