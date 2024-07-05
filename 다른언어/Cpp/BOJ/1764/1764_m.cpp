#include <iostream>
using namespace std;
#include <set>

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    string name;
    set<string> db, dbj;
    set<string>::iterator it;

    cin >> n >> m;

    for(int i=0; i<n+m; i++)
    {
        cin >> name;
        if (db.find(name) != db.end())
        {
            dbj.insert(name);
        }
        db.insert(name);
    }

    cout << dbj.size() << "\n";
    for(it=dbj.begin(); it != dbj.end(); ++it)
    {
        cout << *it << "\n";
    }

    return 0;
}