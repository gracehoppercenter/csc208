# Thanks to https://docs.python.org/3/howto/curses.html and
# https://hyperskill.org/blog/post/introduction-to-the-curses-library-in-python-text-based-interfaces
# for curses guidance. Thanks to Jake Stewart for the group selection code
import random
import curses 
from curses import wrapper

def main(stdscr):
    people = [
        "Dane","Parker", "Shangwen", "Ved", "Jackson", "Liam", "Cody", "Johan",
        "Luis", "Trostin", "Turner", "Anfal", "Ivan", "Anar", "Akshay", "Marin",
        "James", "Caleb", "Fikir", "Jamethiel", "Isaac", "Adonis"
    ]

    topics = {
        "0.1: What is Discrete Mathematics?": 3,
        "0.2: Mathematical Statements": 9, 
        "0.3: Sets": 5,
        "0.4: Functions": 5
    }
    random.shuffle(people)

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    YELLOW_BLACK = curses.color_pair(1)
    RED_BLACK = curses.color_pair(2)

    # Clear screen
    stdscr.clear()
    row, col = 4, 2

    for key in topics.keys():
        stdscr.addstr(
            row,
            col,
            f"Covering {key}:",
            curses.A_BOLD | RED_BLACK
        )
        stdscr.addstr(
            row + 1,
            col + 5,
            ", ".join(people[:topics[key]]),
            curses.A_BOLD | YELLOW_BLACK
        )
        people = people[topics[key]:]   
        row += 3

    stdscr.addstr(21, 5, "Press any key to exit... ")
    stdscr.getkey()

wrapper(main)
