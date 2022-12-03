/*
Practice 9 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
*/
#include<iostream>
using namespace std;
 
int which_date(int y, int m, int d)
{
	if (m == 1 || m == 2) {
		m += 12;
		y--;
	}
	int day = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7;
	return day;
}

void willy(int x)
{
    switch(x)
{
	case 0: cout << "Monday" << endl; break;
	case 1: cout << "Tuesday" << endl; break;
	case 2: cout << "Wednesday" << endl; break;
	case 3: cout << "Thursday" << endl; break;
	case 4: cout << "Friday" << endl; break;
	case 5: cout << "Saturday" << endl; break;
	case 6: cout << "Sunday" << endl; break;
}
}
int main()
{
	int year, month, day;
	cin >> year;
	cin >> month;
	cin >> day;
	willy(which_date(year, month, day));
}