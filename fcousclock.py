import time
import winsound

def concentration_timer():
    concentration_minutes = int(input("请输入专注时间（以分钟为单位）："))
    seconds = concentration_minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

    # 播放声音提醒
    frequency = 2500  # 声音频率（以赫兹为单位）
    duration = 2000  # 声音持续时间（以毫秒为单位）
    winsound.Beep(frequency, duration)

    print('Time is up! Stay focused!')

# 开始专注时钟
concentration_timer()
