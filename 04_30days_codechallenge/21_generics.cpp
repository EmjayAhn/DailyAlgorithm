// https://www.hackerrank.com/challenges/30-generics/problem

/**
* generic 문제가 나왔을 때,
* python 은 generic 에 관한 문제가 생기지 않는다.
* 여기서 제공되는 문제 역시 c++, java, swift 등의 언어로 풀게끔 되어 있어,
* 일관성을 해치지만 .cpp, c++ 언어로 작성하였다.
**/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <typename type>
void printArray (vector<type> a) {
    for (type i:a) {
        cout << i << endl;
    }
}


int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}