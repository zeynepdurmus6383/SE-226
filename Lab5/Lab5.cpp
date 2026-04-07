#include <iostream>
#include <ostream>
using namespace std;


int task3(int n,int r) {
    int result = 1;
    int add = 1;
    for (int i = 1; i <= n; i++) {
        add *= r;
        result += add;
    }
    return result;
}


int main() {
    cout<<task3(4,5)<<endl;
}
