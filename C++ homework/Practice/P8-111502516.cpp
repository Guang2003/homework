/*
Practice 8 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
*/
#include<iostream>
using namespace std;
int main(){
int a,b,t;
cin>>a>>b;
while(b != 0)
{
    t = b;
    b = a%b;
    a = t;
}
cout<<a<<endl;
}