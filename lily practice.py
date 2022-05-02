import time
while True:
    sec = int(input("enter sec: "))
    minute = int(input("Enter min: "))
    hour = int(input("Enter hour: "))

    when_to_stop = sec + (minute * 60) + ((hour * 60)* 60)

    if sec < 0 or minute < 0 or hour < 0:
        print("Invalid input")
    else:
        while when_to_stop > 0:
            minute, sec = divmod(when_to_stop, 60)
            hour, minute = divmod(minute, 60)

            time_left = str(hour).zfill(2) + "." + str(minute).zfill(2) + "." + str(sec).zfill(2)
            print(time_left)

            time.sleep(1)
            when_to_stop -= 1
            if when_to_stop == 0:
                print("00:00:00")
                break
        break
