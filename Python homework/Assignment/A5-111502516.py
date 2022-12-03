"""
Assignment 5
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
"""
file = open('score.txt','r')
input_list = []
_input = file.read()
input_list = _input.split()
file.close()

cmdlist = []
with open('cmd.txt','r') as file:
    for line in file:
        cmdlist.append(line.split())
files = open('output.txt', 'w')
def split_info( input_list ) :
    wait_list = []
    global return_list
    return_list = []
    for i in range(1,len(input_list)+1):
        if (i %5) ==0:
            wait_list.append(input_list[i-1])
            return_list.append(wait_list)
            wait_list = []
        else:
            wait_list.append(input_list[i-1])
    return return_list

def grading_system( student_list ) :
    if int(student_list[1])>= 12 and int(student_list[2])>= 12 and int(student_list[3])>= 8 and int(student_list[4])>= 12:
        return_str = 'Hello '+ student_list[0] + ', welcome to NCU CSIE!'
    else:
        return_str = "Sorry, " + student_list[0] + " can't enter NCU CSIE."
    return return_str

def find_grade( student_list, name, subject ) :
  # Your sList should be a list of lists, containing the student's name and score, such as:
  # [ [ 'John','10','4','5','12' ] , [ 'Mary','10','4','5','12' ] , [ 'Tom','10','4','5','12' ] ]
  # this Function Should Return with a string, representing the student's score, such as:
  # "10" or "4" or "12"
  # if the name or subject is not found, return "Error"
    namelist = []
    return_str = ''
    for i in range(1,len(student_list)+1):
        if (i %5) ==1:
            namelist.append(input_list[i-1])
    try:
        if subject == 'chinese':
            return_str = str(return_list[namelist.index(name)][1])
        elif subject == 'english':
            return_str = str(return_list[namelist.index(name)][2])
        elif subject == 'math':
            return_str = str(return_list[namelist.index(name)][3])
        elif subject == 'science':
            return_str = str(return_list[namelist.index(name)][4])
        else:
            return 'Error'
    except:
        return 'Error'
    #return_str = ''
  # Write your code here
    return return_str # should be the student's score in string type or "Error"
split_info(input_list)
for student_list in split_info(input_list):
    files.write(grading_system(student_list)+'\n')
for i in range(len(cmdlist)):
    files.write(find_grade(input_list, cmdlist[i][0],cmdlist[i][1])+'\n')
files.close()