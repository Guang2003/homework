/*
Assignment 10 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1001*
*/
# include<iostream>
# include<vector>
using namespace std;

// ========== Global Variables ==========
int i = 100;
string input;
char tested[100];
int count0,count1,count2;
int counter = 0;
string str;
vector <string> test0;
vector <string> test1;
vector <string> test2;
vector <string> test3;
int judge;
int summation;
 // Global token list

// ========== Print Function ==========

void print_types_info( int i_num, int n_num, int s_num ) {
  cout << "Identifier: " << i_num << ", " << "Number: " << n_num << ", " << "Special Symbol: " << s_num << endl;
}

void print_invalid_command() {
  cout << "Invalid command." << endl;
}

void print_token( string token ) {
  cout << "[" << token << "]" << endl;
} 

void print_token_sum( int sum ) {
  cout << "Total number of tokens: " << sum << endl;
} 

// ========== Other Functions ==========

bool is_identifier( char c ) {
  // given a character, return true if it is a part of a identifier

  bool result = false;
  /*Your Code Here*/
  if (isalpha(c) || (c =='_'))
  {
    result = true;
  }
  return result;

} 

bool is_number( char c ) {
  // given a character, return true if it is a number

  bool result = false;
  /*Your Code Here*/
  if (isdigit(c))
  {
    result = true;
  }
  return result;

} 

bool is_special_symbol( char c ) {
  // given a character, return true if it is a special symbol or not

  bool result = false;
  /*Your Code Here*/
  if (c == '+'  || c == '-' || c == '*' || c == '/' ||
      c == '>'  || c == '<' || c == '=' || c == '%' ||
      c == '&'  || c == '|' || c == '^' || c == '"' ||
      c == '\'' || c == '.' || c == ',' || c == '(' ||
      c == ')'  || c == '[' || c == ']' || c == '{' ||
      c == '}'  || c == '!' || c == ':' || c == ';'  )
  {
    result = true;
  }
  return result;
}

void get_user_input() {
  // Get user input until END_OF_FILE appears, and store the tokens into g_token_list.

  /*Your Code Here*/
while(i>10)
{
  cin>>input;
  if(input == "END_OF_FILE")
  {
    break;
  }
  test0.push_back(input);
}
}

void excute_command( int cmd ) {
  switch (cmd){
    case 1:
    print_token_sum(summation);
    break;
    case 2:
    for(int k=0;k<test1.size();k++)
    {
      print_token(test1[k]);
    }
    break;
    case 3:
    print_types_info(count0,count1,count2);
    break;
    default:
    print_invalid_command();
    break;
} 
}

// ========== Main Function ==========

int main() {

get_user_input();
for(int j = 0; j<test0.size(); j++){
  str = test0[j];
  for(int k = 0; k<str.size(); k++){
    char l = str[k];
    if(is_identifier(l)){
      int m = k;
      for(int h = 0;h<40;h++){
        tested[h] = '\0';
      }
      tested[counter] = l;
      while(i>10){
        if(is_identifier(str[m+1])|| is_number(str[m+1])){
          counter += 1;
          tested[counter] = str[m+1];
          m += 1;
        }
        else{
          counter = 0;
          break;
        }
      }
      test1.push_back(tested);
      k = m;
      count0 +=1;
      continue;
    }
    else if(is_number(l)){
      int m = k;
      for(int h = 0;h<40;h++){
        tested[h] = '\0';
      }
      tested[counter] = l;
      while(i>10){
        if(is_number(str[m+1])){
          counter += 1;
          tested[counter] = str[m+1];
          m += 1;
        }
        else{
          counter = 0;
          break;
        }
      }
      test1.push_back(tested);
      k = m;
      count1 +=1;
      continue;
    }
    else if(is_special_symbol(l)){
      int m = k;
      for(int h = 0;h<40;h++){
        tested[h] = '\0';
      }
      tested[counter] = l;
      while(i>10){
        if((l == '+' && str[m+1] == '=')||(l == '-' && str[m+1] == '-')||(l == '+' && str[m+1] == '+')
        ||(l == '<' && str[m+1] == '=')||(l == '>' && str[m+1] == '=')||(l == '=' && str[m+1] == '=')
        ||(l == '!' && str[m+1] == '=')||(l == '&' && str[m+1] == '&')||(l == '|' && str[m+1] == '|')){
          counter += 1;
          tested[counter] = str[m+1];
          m += 1;
        }
        else{
          counter = 0;
          break;
        }
      }
      test1.push_back(tested);
      k = m;
      count2 +=1;
      continue;
    }
    else{
      for(int h = 0;h<40;h++){
        tested[h] = '\0';
      }
      tested[counter] = l;
      test1.push_back(tested);
    }
  }
}
summation = test1.size();
while(i>10)
{
  cin>>judge;
  if (judge == 0)
  {
    break;
  }
  switch (judge)
  {
  case 1:case 2: case 3:
    excute_command(judge);
    break;
  
  default:
    print_invalid_command();
    break;
  }
  }
}