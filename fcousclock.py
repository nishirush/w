import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")

# 设置专注时长（以秒为单位）
focus_time = 25 * 60

countdown(focus_time)
