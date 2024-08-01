import time
from playsound import playsound


CLEAR = "\033[2J"       #clears the terminal
CLEAR_AND_RETURN = "\033[H"     #clears the terminal and returns the curser to the top


def alarm(set_time):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed != set_time:
        time.sleep(1)
        time_elapsed += 1

        time_left = set_time - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    print(CLEAR)
    print("now playing the sound")
    #playsound("alarm_sound.mp3")