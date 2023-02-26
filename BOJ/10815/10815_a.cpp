#include <iostream>
#include <set>
using namespace std;

int main(void)
{
    //~시간을 줄여주는 마법의 문장~
    //c의 버퍼(stdio)와의 동기화 비활성화
    ios_base::sync_with_stdio(false);
    //cin과 cout의 묶음을 풀어줌. 입출력 번갈아가며 반복시 반드시 추가해줄것.
    //이때 endl은 개행문자 + 버퍼 비우는 역할이라 딜레이 발생함. '\n'으로 개행할것.
    cin.tie(NULL);
    
    int n, m, num;
    set<int> set_n;

	cin >> n;
	for(int i=0; i<n; i++)
	{
        cin >> num;
		set_n.insert(num);
	}

	cin >> m;
    for (int i = 0; i<m; i++)
    {
        cin >> num;
        if(set_n.find(num) != set_n.end())
            cout << "1 ";
        else cout << "0 ";
    }
    return 0;
}