/*
Assignment 11 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
*/
#include <iostream>
# include<map>
# include<vector>
using namespace std;
int times;
string temp_store;
int sum = 0;
map<string,map<string,int> >test;
vector<string>items;
vector<string>kinds;
vector<string>sizes;
map<string,map<string,int> > get_input(map<string,map<string,int> >doll_map){
    //Please write your code here
cin>>times;
for(int i = 0;i<times*2;i++){
    cin>>temp_store;
    items.push_back(temp_store);
}
for(int i = 1;i<times*2;i+=2){
    if(doll_map.count(items[i]) == 1){
        if(doll_map[items[i]].count(items[i-1])==1){
            doll_map[items[i]][items[i-1]] +=1;
        }
        else{
            sizes.push_back(items[i-1]);
            doll_map[items[i]][items[i-1]] = 1;
        }
    }
    else{
        kinds.push_back(items[i]);
        sizes.push_back(items[i-1]);
        doll_map[items[i]][items[i-1]]=1;
    }
}
return doll_map;
    //
}

void calculate_doll(map<string,map<string,int> >& doll_map){
    //Please write your code here
for(int i = 0;i<kinds.size();i++){
    int counter = 0;
    for(int j = 0;j<sizes.size();j++){
        //cout<<"種類："<<kinds[i]<<endl<<"大小："<<sizes[j]<<endl<<"數量："<<test[kinds[i]][sizes[j]]<<endl;
        if(test[kinds[i]][sizes[j]]>counter){
            counter = test[kinds[i]][sizes[j]];
        }
    }
    sum += counter;
    //cout<<kinds[i]<<endl<<counter<<endl;
}
cout<<sum<<endl;
    //
}
int main(){
map<string,map<string,int> >doll_map;
test = get_input(doll_map);
calculate_doll(test);

return 0;
}