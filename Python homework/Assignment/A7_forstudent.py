#從文件中讀取迷宮矩陣
def get_maze():
    f = open('input.txt', 'r')
    maze = []
    for lines in f.readlines():
        maze.append(lines.split())
    f.close()
    return maze
#

