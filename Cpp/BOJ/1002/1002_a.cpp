#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int x1, y1, r1, x2, y2, r2, T, d, dis1, dis2;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        // d = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
        d = pow(x1-x2, 2) + pow(y1-y2, 2);
        dis1 = pow(r1+r2,2);
        dis2 = pow(r1-r2,2);

        if(d == 0)
        {
            if (dis2 == 0)
                cout << "-1" << '\n';
            else 
                cout << "0" << '\n';
        }
        else if (d == dis1 || d == dis2)
            cout << "1" << '\n';
        else if (d < dis1 && d > dis2) 
            cout << "2" << '\n';
        else cout << "0" << '\n';

    }

    return 0;
}
