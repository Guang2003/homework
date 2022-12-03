grade = round(float(input()))
if grade <60:
    print('F')
elif grade < 63:
    print('C-')
elif grade < 67:
    print('C')
elif grade < 70:
    print('C+')
elif grade < 73:
    print('B-')
elif grade < 77:
    print('B')
elif grade < 80:
    print('B+')
elif grade < 85:
    print('A-')
elif grade < 90:
    print('A')
else:
    print('A+')