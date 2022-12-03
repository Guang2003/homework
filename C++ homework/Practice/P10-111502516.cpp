/*
Practice 10 C++
Name:賴光庭
Student Number:111502516
Course 2022-CE1003-A
*/
# include<iostream>
# include<vector>
using namespace std;

// ========== Global Variables ==========
int i = 100;
string input;
char tested;
int count0,count1,count2;
char wait0;
char wait1;
vector <char> g_token_list;
vector<string>h_token_list;
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

void skip_white_space() {
  // skip white space such as ' ', '\t', '\n', and make g_char the first character of the next token

  /*Your Code Here*/

}

bool is_identifier( char c ) {
  // given a character, return true if it is a part of a identifier

  bool result = false;
  /*Your Code Here*/
  if (isalpha(c)|| (c =='_'))
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
  if (ispunct(c) && (c != '_'))
  {
    result = true;
  }
  return result;

}

void get_user_input() {
  // Get user input until END_OF_FILE appears, and store the tokens into g_token_list.

  /*Your Code Here*/

} 

string get_token_type( string token ) {
  // Given a token, return the type of the token.(Identifier, Number, or Special Symbol?)

  string type;
  /*Your Code Here*/
  return type;

} 

void excute_command( int cmd ) {
  // Given a command:
  // if command == 1, print token sum
  // if command == 2, print all tokens
  // if command == 3, token sum in each cases
} 

// ========== Main Function ==========

int main() {
  // Get User Input form the input stream, and execute the command until command == 0.

  /*Your Code Here*/

while(i>10)
{
  cin>>input;
  if(input == "END_OF_FILE")
  {
    break;
  }
  h_token_list.push_back(input);
  tested = input[0];
  g_token_list.push_back(tested);
}
for(int j = 0;j<g_token_list.size();j++)
{ wait0 = g_token_list[j];
  if(is_identifier(wait0))
  {
    count0 +=1;
  }
  if(is_number(wait0))
  {
    count1 +=1;
  }
  if(is_special_symbol(wait0))
  {
    count2 +=1;
  }
}
summation = h_token_list.size();
//cout<<h_token_list[0];
while(i>10)
{
  cin>>judge;
  if (judge == 0)
  {
    break;
  }
  switch (judge)
  {
    case 1:
    print_token_sum(summation);
    break;
    case 2:
    for(int k=0;k<h_token_list.size();k++)
    {
      print_token(h_token_list[k]);
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
}