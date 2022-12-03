file = open('score.txt','r')
input_list = []
_input = file.read()
input_list = _input.split()
file.close()
files = open('output.txt', 'w')
def split_info( input_list ) :
    wait_list = []
    return_list = []
    for i in range(1,len(input_list)+1):
        if (i %5) ==0:
            wait_list.append(input_list[i-1])
            return_list.append(wait_list)
            wait_list = []
        else:
            wait_list.append(input_list[i-1])
  # Your inputList should be a list of strings, containing the student's name and score, such as:
  # [ 'John','10','4','5','12', 'Mary','10','4','5','12', 'Tom','10','4','5','12' ]
  # this Function Should Return a list of lists, containing the student's name and score, such as:
  # [ [ 'John','10','4','5','12' ] , [ 'Mary','10','4','5','12' ] , [ 'Tom','10','4','5','12' ] ]

  # Write your code here
    return return_list # should be: [ [ 'John','10','4','5','12' ] , [ 'Mary','10','4','5','12' ] , [ 'Tom','10','4','5','12' ] ]

def grading_system( student_list ) :
  # studentList should be a list of strings, containing the student's name and score, such as:
  # [ 'John','10','4','5','12']
  # this Function Should Return with a string, representing weather the student can enter NCU CSIE, such as:
  # "Hello "+ name + ", welcome to NCU CSIE!" 
  # or
  # "Sorry, " + name + " can't enter NCU CSIE." 
  if int(student_list[1])>= 12 and int(student_list[2])>= 12 and int(student_list[3])>= 8 and int(student_list[4])>= 12:
    return_str = 'Hello '+ student_list[0] + ', welcome to NCU CSIE!'
  else:
    return_str = "Sorry," + student_list[0] + " can't enter NCU CSIE."
  # Write your code here
  return return_str # should be: "Hello "+ name + ", welcome to NCU CSIE!"  or "Sorry, " + name + " can't enter NCU CSIE." 

# Main Function
# Write Your Code Here

split_info(input_list)
for student_list in split_info(input_list):
  files.write(grading_system(student_list)+'\n')
files.close()