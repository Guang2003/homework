/*
Assignment 9 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
*/
#include<iostream>
using namespace std;
/*第一部分-1*/
int which_date(int y, int m, int d)
{
	if (m == 1 || m == 2) {
		m += 12;
		y--;
	}
	int day = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7;
	return day;
}
/*第一部分-2*/
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
/*閏年判斷(確定回傳type)*/
int leapornot(int ye, int mo, int ay)
{
	int leap[12] = {32,30,32,31,32,31,32,32,31,32,31,32};
	int average[12] = {32,29,32,31,32,31,32,32,31,32,31,32};
	if( ye%400==0 || ( ye%4==0 && ye%100!=0 ) )
	{
		return leap[mo-1];
	}
	else
	{return average[mo-1];}
}
/*打印月曆*/
void  display_calendar(int yea, int mon, int da)
{
    int count = 1;
    int a = 1;
    for (a=0;a<7;a++)
        cout <<"    "<<a;
    cout << endl << "=====================================" << endl;
	//cout<<yea<<mon<<da;
	int wtf = 1;
	int judge;
	if (mon == 1 || mon == 2) {
		mon += 12;
		yea--;
    judge = (wtf + 2 * mon + 3 * (mon + 1) / 5 + yea + yea / 4 - yea / 100 + yea / 400) % 7;
	mon -= 12;
	yea++;
	}
	else
	{
		judge = (wtf + 2 * mon + 3 * (mon + 1) / 5 + yea + yea / 4 - yea / 100 + yea / 400) % 7;
	}
	//cout<<judge<<endl;
	int count0 = judge;/*算換行用的*/
    if (judge !=6)
	{
		int count1 = 0;
		while(count1<=judge)
		{
			cout<<"     ";
			count1 +=1;
		}
	}
	
	while(count<10)
	{
		if(count0%7 ==6 && count != 1)
		{
			cout<<endl;
		}
		if(count==da)
		{
			cout<<"   *"<<count;
			count +=1;
		}
		else
		{
			cout<<"    "<<count;
			count +=1;
		}
		count0 +=1;
	}
	while(count<leapornot(yea,mon,da))
	{
		if(count0%7 ==6)
		{
			cout<<endl;
		}
		if(count==da)
		{
			cout<<"  *"<<count;
			count +=1;
		}
		else
		{
			cout<<"   "<<count;
			count +=1;
		}
		count0 +=1;
	}
    cout << endl << "=====================================" << endl;
}
int main()
{
	int year, month, day;
	cin >> year;
	cin >> month;
	cin >> day;
	willy(which_date(year, month, day));
    cout<<endl;
    display_calendar(year, month, day);
}