#include <iostream>
#include <string>

#define MAX 10000

using namespace std;

int stack[MAX];
int idx = -1;

int Push(int x, int idx)
{
    stack[idx] = x;
    idx++;
    return idx;
}

int Pop(int idx)
{
    if (idx == -1){
        cout << -1 << endl;
    } else {
        cout << stack[idx] << endl;
        stack[idx] = NULL;
    }
    idx--;
    return idx;
}

void CheckSize(int idx)
{
    cout << idx + 1 << endl;
}

void CheckEmpty(int idx)
{
    if (idx == -1){
        cout << 1 << endl;
    } else {cout << 0 << endl;}
}

void PrintTop(int idx)
{
    if (idx == -1){
        cout << -1 << endl;
        return;
    }
    cout << stack[idx] << endl;
}

int main(void)
{
    int num, x;
    string cmd, sub;

    cin >> num;

    while(num > 0)
    {
        getline(cin, cmd); //������ ������ ���ڿ� �Է� �ޱ�

        if(cmd.find(" ") != string::npos){ //���鹮�� ������
            sub = cmd.substr(cmd.find(" ") + 1, cmd.length());
            x = stoi(sub); // ���ڿ����� ������ ��ȯ
            cmd = cmd.substr(0, cmd.find(" "));
        }
            
        switch (expression)
        {
        case /* constant-expression */:
            /* code */
            break;
        
        default:
            break;
        }
        num--;
    }
}