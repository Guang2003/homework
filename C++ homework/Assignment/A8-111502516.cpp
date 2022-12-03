/*
Assignment 8 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
*/
#include<iostream>
using namespace std;
int main(){
int a,b,t,x,y;
cin>>a>>b;
x = a;
y = b;
while(b != 0)
{
    t = b;
    b = a%b;
    a = t;
}
cout<<(x*y)/a<<endl;

}