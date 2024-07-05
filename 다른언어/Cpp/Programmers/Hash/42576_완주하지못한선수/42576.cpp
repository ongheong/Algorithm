//프로그래머스 고득점 Kit 해시 Level.1 완주하지 못한 선수

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> map; //key-value 쌍 관리

    for (auto runner : participant) {
        if (map.end() == map.find(runner)) //'runner'를 키로 가지는 요소가 맵에 없으면
            map.insert(make_pair(runner, 1));
        else
            map[runner]++;//이미 있다면 이름이 같은 선수이므로 count++
    }

    for (auto runner : completion) {
        map[runner]--;//완주 목록에 있다면 하나씩 제거
    }

    for (auto runner : participant) {
        if (map[runner] > 0)
            answer = runner;
    }

    return answer;
}

int main(void) {
    vector<string> partition = {"leo", "kiki", "eden"};
    vector<string> completion = {"eden", "kiki"};
    cout << solution(partition, completion);
    return 0;
}