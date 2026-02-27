#include <iostream>
#include <String>
using namespace std;
int main() {
    int y;
    cout << "Enter an amount of seconds to convert:" << endl;
    cin >> y;
    int seconds = y%60;
    int totalMinutes = y/60;
    int minutes = totalMinutes%60;
    int hours = totalMinutes/60;
    cout << y << " seconds is " << hours << " hours, " << minutes << " minutes, and " << seconds << " seconds." << endl;
    return 0;
}