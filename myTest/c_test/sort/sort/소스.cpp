#include <iostream>
#include <ctime>

#define SIZE 4

using namespace std;

void MergeSort(int* Arr, int start, int end);
void Merge(int* Arr, int start, int mid, int end);

void main()
{
	int* arr = new int[SIZE];

	for (int i = 0; i < SIZE; ++i) {
		arr[i] = rand() % SIZE;
		cout << arr[i] << ' ';
	}
	cout << endl;

	time_t start = time(0);

	//@@@
	MergeSort(arr, 0, SIZE);
	//@@@
	double now = double(time(0) - start) / CLOCKS_PER_SEC;


	for (int i = 0; i < SIZE; ++i) {
		cout << arr[i] << ' ';
	}
	cout << endl;
	cout << "소요시간: " << now << endl;
}

void MergeSort(int* Arr, int start, int end)
{
	cout << "start - " << start << '\t' << "end - " << end << endl;
	if (start >= end)
		return;

	int mid = start + (end - start) / 2;

	MergeSort(Arr, start, mid);
	MergeSort(Arr, mid+1, end);
	Merge(Arr, start, mid, end);
}

int tempArr[SIZE];
void Merge(int* Arr, int start, int mid, int end)
{
	//cout << "start - " << start << '\t' << "end - " << end << endl;

	int i = 0;
	int s = start;
	int m = mid + 1;

	while (s < mid && m < end) {
		if (Arr[i] <= Arr[m]) {
			tempArr[i++] = Arr[s++];
		}
		else {
			tempArr[i++] = Arr[m++];
		}
	}

	if (s < m) {
		for (int l = s; l < m; ++l, ++i) {

		}
	}
	else{
		for (int l = m; l < end; ++l, ++i) {

		}
	}

	//cout << "----------------------" << endl;
	for (int l = start, i = 0; l < end; ++l, ++i) {
		//cout << l << "Arr: " << Arr[l] << endl;
		//cout << i << "tempArr: " << tempArr[i] << endl;
		Arr[l] = tempArr[i];
	}
	//cout << "----------------------" << endl;

	delete[] tempArr;
}