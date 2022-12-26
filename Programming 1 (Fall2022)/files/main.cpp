#include <iostream>
#include <fstream>

using namespace std;

int main() {


  int numbers[6];
  int temp = 0;

  for (int i = 0 ; i < 6 ; i++) {
    cout << "Enter number " << i+1 << " : ";
    cin >> numbers[i];
  }
  
  // [ 6 , 5 , 7 , 18 , 25 , 4 ]
  // [ 4 , 5 , 6 , 7 , 18 , 25]
  for (int i = 0 ; i < 6 ; i++) {
    
    temp = i;
    for (int j = i ; j < 6 ; j++) {
      if(numbers[j] < numbers[temp]) {
        temp = j;
      } else {
        continue;
      }
    }

    if (temp != i) {
      int t = numbers[i];
      numbers[i] = numbers[temp];
      numbers[temp] = t;
    }
  }

  for (int i = 0 ; i < 6 ; i++) {
    cout << numbers[i];
  }
}