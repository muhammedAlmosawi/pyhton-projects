from type_test import *
import time
import random

def text_chooser():
    with open("text_choices.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(f"\nWPM {wpm}")
        
    for i, char in enumerate(current):
        if char == target[i]:
            color = curses.color_pair(1)
        else:
            color = curses.color_pair(3)
        
        stdscr.addstr(0, i, char, color)

def WPM_calculator(stdscr):
    target_text = text_chooser()
    current_text = []
    wpm = 0

    start_time = time.time()
    stdscr.nodelay(True)
    while True:

        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        if "".join(current_text) == target_text:
            break

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
