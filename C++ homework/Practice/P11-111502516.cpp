/*
Practice 11 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
*/
#include <iostream>
# include<map>
# include<vector>
using namespace std;
int times;
int temp_store;
int counter = 0;
map<int,int>test;
vector<int>oops;
map<int,int> get_input(map<int,int> doll_map){
    //Please write your code here
cin>>times;
for(int i = 0;i<times;i++){
    cin>>temp_store;
    if(doll_map.count(temp_store)==1){
        doll_map[temp_store] +=1;
        }
    else{
        doll_map[temp_store] = 1;
        oops.push_back(temp_store);
}
}
return doll_map;
    //
}

void calculate_doll(map<int,int>& doll_map){
    //Please write your code here
for(int i = 0;i<oops.size();i++){
    if(doll_map[oops[i]]>=counter){
    counter = doll_map[oops[i]];
}
}
cout<<counter<<endl;
    //
}
int main(){
map<int,int>doll_map;
test = get_input(doll_map);
calculate_doll(test);

return 0;
}