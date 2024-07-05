function solution(num_list) {
    var answer = [];
    if (num_list.at(-1) > num_list.at(-2)) answer = [...num_list, num_list.at(-1) - num_list.at(-2)];
    else answer = [...num_list, num_list.at(-1)*2];
    return answer;
}