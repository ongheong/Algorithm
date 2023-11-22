#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_map<string, int> map;

    for (auto num : phone_book) {
        map[num]++;
    }

    for (int i=0; i < phone_book.size(); i++) { // 이중루프
        string str="";
        for (int j=0; j<phone_book[i].size(); j++) {
            str += phone_book[i][j]; //phone_book 원소의 앞 글자부터 추가하며 맵에 있는지 탐색
            if (map[str] && str != phone_book[i]) { // 접두어 str가 phone_book에 존재하면서 현재 검사하는 문자열이 아니면
                return false; // 바로 함수 종료
            }
        }
    }

    return answer;
}

int main(void) {
    vector<string> phone_book = {"12","123","1235","567","88"};
    cout << solution(phone_book);
    return 0;
}