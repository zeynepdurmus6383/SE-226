#include <iosfwd>
#include <iostream>
#include <string>

using namespace std;
void swapValues(int* p1, int* p2) {
    cout << "Swapping two numbers: " << endl << "Before swap: " << endl << "p1 = " << *p1 << endl << "p2 = " << *p2 << endl;
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
    cout << "After swap: " << endl << "p1 = " << *p1 << endl << "p2 = " << *p2 << endl;
}

void printArray(int* arr, int size) {
    cout << "Array elements:" << endl;
    int *p = arr;
    for (int i = 0; i < size; i++) {
        cout << *p << " ";
        p++;
    }
    cout << endl;
}

int findMax(int* arr, int size) {
    int* p = arr;
    int max = *arr;
    for (int i = 0; i < size; i++) {
        if (*p >= max) {
            max = *p;
        }
        p++;
    }
    cout << "Maximum element: " << max << endl;
    return max;
}
void reverseArray(int* arr, int size) {
    int *p = arr;
    int *end = p + (size-1);
    for (int i = 0; i < size/2 ; i++) {
        swapValues(p, end-i);
        p++;
    }
    cout << "Array after reverseArray: " << endl;
    printArray(arr, size);
}

 int* createArray(int size) {
    int *arr = new int[size];
    cout << "Enter values: " << endl;
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }
    return arr;
}
void deleteArray(int* arr) {
    cout << "Deleting array..." << endl;
    delete[] arr;
    cout << "Memory released successfully." << endl;
}

int main() {
    int size;
    cout << "Enter array size: " << endl;
    cin >> size;
    int* p = createArray(size);
    printArray(p, size);
    findMax(p, size);
    int p1 = 5;
    int p2 = 8;
    swapValues(&p1, &p2);
    reverseArray(p, size);
    deleteArray(p);
}