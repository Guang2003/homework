"""
Practice 7
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
"""
route_history = [[0,0]]
route_stack = [[0,0]]
right_road = [[1,1]]
history_road = [[1,1]]
def get_maze():
    f = open('input.txt', 'r')
    maze = []
    for lines in f.readlines():
        maze.append(lines.split())
    f.close()
    return maze
maze=get_maze()
times = 0
def do_maze(location):
    #print(location)
    newlocation = [location[0]+1,location[1]]
    if maze[newlocation[0]][newlocation[1]] != '0':
        if newlocation == [5,5]:
            #print('aaaaaaaaaaaaaaaaaa')
            global times
            times += 1
        do_maze(newlocation)
    newlocation = [location[0],location[1]+1]
    if maze[newlocation[0]][newlocation[1]] != '0':
        if newlocation == [5,5]:
            #print('aaaaaaaaaaaaaaaaaa')
            times += 1
        do_maze(newlocation)
    #return newlocation
locate = [1,1]
do_maze(locate)
if times > 0:
    print(1)
else:
    print(0)