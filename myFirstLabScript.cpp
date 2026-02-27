#include <iostream>
#include <String>
using namespace std;
int main() {
    string name;
    cout << "What is your name?" << endl;
    cin >> name;
    int number;
    cout << "Hello " << name << endl;
    cout << "What is your Student ID?" << endl;
    cin >> number;
    cout << "Your ID is " << number << endl;
    return 0;
}