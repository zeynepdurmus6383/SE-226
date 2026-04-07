#include <iostream>
#include <String>
#include <cmath>
using namespace std;
int main() {
    float x1;
    float y1;
    float x2;
    float y2;
    cout << "Please enter the coordinates x of Line 1";
    cin>> x1;
    cout << "Please enter the coordinates y of Line 1";
    cin>> y1;
    cout << "Please enter the coordinates x of Line 2";
    cin>> x2;
    cout << "Please enter the coordinates y of Line 2";
    cin>> y2;
    float subx = x2 - x1;
    float suby = y2 - y1;
    subx *= subx;
    suby *= suby;
    float total = subx + suby;
    float result = sqrt(total);
    cout << "Distance: " << result << endl;
    return 0;
}

