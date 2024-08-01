from main import *
import curses
import queue
import time


def find_start(maze, start):
    for i ,row in enumerate(maze):
        for j , column in enumerate(row):
            if column == start:
                return i, j
    return None

def find_neighbor(maze, row, column):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, column))

    if row + 1 != len(maze):
        neighbors.append((row + 1, column))

    if column > 0:
        neighbors.append((row, column - 1))
    
    if column + 1 < len(maze[0]):
        neighbors.append((row, column + 1))
    return neighbors

def print_maze(maze, stdscr, path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    for i ,row in enumerate(maze):
        for j ,column in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", red)
            else:
                stdscr.addstr(i, j * 2, column, blue)

def find_shortest_path(maze, stdscr):
    start = "O"
    end = "X"
    start_coordinates = find_start(maze, start)

    q = queue.Queue()
    q.put((start_coordinates, [start_coordinates]))

    visited = set()

    while not q.empty():
        current_position, path = q.get()
        row, column = current_position

        time.sleep(0.25)
        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()

        if maze[row][column] == end:
            return path
        
        neighbors = find_neighbor(maze, row, column)

        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            if maze[row][column] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)







