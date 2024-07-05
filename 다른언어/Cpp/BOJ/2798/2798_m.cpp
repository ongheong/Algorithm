#include <iostream>
using namespace std;

int make_sum(int *arr, int c, int n, int m){
    int sum, max, fix;
    sum = 0;
    max = 0;
    fix = arr[c];

    for(int i=c+1; i<n; i++)
    {
        for (int j=i+1; j<n; j++)
        {
            sum = fix + arr[i] + arr[j];
            if(sum > max && sum <= m) max = sum;
        }
    }
    return max;
}

int main()
{
    int count, n, m;
    int t, max;
    cin >> n >> m;

    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    t = make_sum(arr, 0, n, m);
    count = 1;
    max = 0;

    while (count != n)
    {
        if (t > max && t <= m) max = t;
        else
            t = make_sum(arr, count, n, m);
        count++;
    }
    cout << max;
    return 0;
}


