import curses
from curses import wrapper


if __name__ == "__main__":
    from WPM_calculator import WPM_calculator

    def start_screen(stdscr):
        stdscr.clear()
        stdscr.addstr("here bro type something ", curses.color_pair(2))
        stdscr.addstr("\nHello!", curses.color_pair(2))
        stdscr.addstr("\npress any key to continue ", curses.color_pair(2))
        stdscr.refresh()
        stdscr.getkey()

    def main(stdscr):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        start_screen(stdscr)

        while True:
            WPM_calculator(stdscr)
            stdscr.nodelay(False)
            stdscr.addstr("\ncongrats you have correctly typed the text")
            stdscr.addstr("\nif you want to stop press (ESC)")
            key = stdscr.getkey()
            if ord(key) == 27:
                break

    wrapper(main)
