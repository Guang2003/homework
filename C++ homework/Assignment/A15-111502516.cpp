/*
Assignment 15 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
*/
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
using namespace std;
string deal;
void sort_card(string *p_card)
{
    map <string, int> compare = {{"C2",0},{"C3",1},{"C4",2},{"C5",3},{"C6",4},{"C7",5},{"C8",6},{"C9",7},{"CT",8},{"CJ",9},{"CQ",10},{"CK",11},{"CA",12},
                                {"D2",13},{"D3",14},{"D4",15},{"D5",16},{"D6",17},{"D7",18},{"D8",19},{"D9",20},{"DT",21},{"DJ",22},{"DQ",23},{"DK",24},{"DA",25},
                                {"S2",26},{"S3",27},{"S4",28},{"S5",29},{"S6",30},{"S7",31},{"S8",32},{"S9",33},{"ST",34},{"SJ",35},{"SQ",36},{"SK",37},{"SA",38},
                                {"H2",39},{"H3",40},{"H4",41},{"H5",42},{"H6",43},{"H7",44},{"H8",45},{"H9",46},{"HT",47},{"HJ",48},{"HQ",49},{"HK",50},{"HA",51},};
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 13; j++)
        {
            for(int k = 0; k < 12; k++)
            {
                string card1 = p_card[i][k];//此行報錯conversion from '__gnu_cxx::__alloc_traits<std::allocator<char>, char>::value_type' {aka 'char'} to non-scalar type 'std::__cxx11::string' {aka 'std::__cxx11::basic_string<char>'} requested
                string card2 = p_card[i][k+1];
                if(compare[card1] > compare[card2])
                {
                    string temp = p_card[i][k];
                    p_card[i][k] = p_card[i][k+1];
                    p_card[i][k+1] = temp;
                }
            }
        }
    }
}

void show_card(string *p_card)
{
    int dealer;
    map <string, int> dealmap = {{"E",0},{"S",1},{"W",2},{"N",3}};
    dealer = dealmap[deal];
    int deal_ary[4][4] = {{0,1,2,3},{3,0,1,2},{2,3,0,1},{1,2,3,0}};
    string direct[4] = {{"S:"},{"W:"},{"N:"},{"E:"}};
    ofstream OutFile("output.txt", ios::out);
    if(!OutFile)
    {
        cout<<"Output is wrong."<<endl;
    }
    else
    {
        for(int i = 0; i < 4; i++)
        {
            OutFile<<direct[i];
            int judge = deal_ary[dealer][i];
            for(int j = 0; j < 13; j++)
            {
                OutFile<<" "<<p_card[judge][j];
            }
            OutFile<<endl;
        }
        OutFile.close();
    }
}

int main()
{
    string card[4][13];
    ifstream InFile("input.txt", ios::in);
    if(!InFile)
    {
        cout<<"Input is wrong."<<endl;
    }
    else
    {
        int order1 = 0;
        int order2 = 0;
        string tmp = "";
        InFile >> deal;
        for(int i = 0; i < 52; i++)
        {
            InFile >> tmp;
            card[order1][order2] = tmp;
            if(order1 == 3)
            {
                order1 = 0;
                order2 += 1;
                continue;
            }
            order1 += 1;
        }
        int cmd;
        InFile >> cmd;
        InFile.close();
    }
    sort_card(&card[0][0]);
    //show_card(&card[0][0]);
}
