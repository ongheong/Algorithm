#include <iostream>
using namespace std;

int main()
{
    int n, cnt, num;
    string str;

    cin >> n;
    cnt = 0;
    num = 666;
    
    while(1){
        str = to_string(num);
        for(int i = 0; i < (str.length()-2); i++)
        {
            if (str[i] == '6' && str[i+1] == '6' && str[i+2] == '6')
            {
                cnt++;
                break;
            }
        }
        if (cnt == n)
        {
            cout << num;
            return 0;
        }
        num++;
    }
}