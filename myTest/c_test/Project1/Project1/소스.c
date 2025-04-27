#include <stdio.h>

void NumberChanger(int* num);

int main()
{
	int data[5] = { 10,6,7,9,3 };

	int temp;

	for(int i = 0; i < 4; ++i) {
		for(int j = i + 1; j < 5; ++j) {
			if(data[i] > data[j]) {
				temp = data[i];
				data[i] = data[j];
				data[j] = temp;
			}
		}
	}

	for(int i = 0; i < 5; ++i)
		printf("%d ", data[i]);

	return 0;
}

void NumberChanger(int* num)
{
	*num = 10;
}