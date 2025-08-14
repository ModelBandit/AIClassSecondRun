#include <iostream>

using namespace std;

int main()
{
	char str[] = "this is dog";
	const char det = ' ';

	char *splitStr = strtok(str, &det);

	cout << &splitStr << ' ' << ' ' << endl;
	cout << &splitStr << endl;
	cout << &splitStr << endl;
	/*for (char* i = splitStr; i < splitStr + 3; ++i) {
		cout << &i << endl;
	}*/
	return 0;
}
