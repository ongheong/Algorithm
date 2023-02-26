#include <iostream>
using namespace std;

#define MAX 500000

//시간초과
bool find_m(int *arr_n, int m, int n)
{
	for (int i = 0; i < n; i++)
	{
		if (arr_n[i] == m)
		{
			return 1;
		}
	}
	return 0;
}

int main()
{
	bool find;
    int n, m;
    int arr_n[MAX];
	int arr_m[MAX];

	find = 0;

	cin >> n;
	for(int i=0; i<n; i++)
	{
		cin >> arr_n[i];
	}

	cin >> m;
	for(int i=0; i<m; i++)
	{
		cin >> arr_m[i];
	}

	for(int j=0; j<m; j++)
	{
		cout << find_m(arr_n, arr_m[j], n) << ' ';
	}

	return 0;
}

