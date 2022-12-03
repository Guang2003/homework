"""
Assignment 1
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
"""
grade1 = float(input('Please enter your Chinese score: '))
grade2 = float(input('Please enter your English score: '))
grade3 = float(input('Please enter your Math score: '))
grade4 = float(input('Please enter your Science score: '))
average1=(grade1+grade2+grade3+grade4)/4
print ('Your average score is:',average1)
if grade1>58.74 and grade2>68.30 and grade3>38.93 and grade4>88.56:
    print('Welcome to NCU CSIE!')
else:
    print("Sorry, you can't enter NCU CSIE.")