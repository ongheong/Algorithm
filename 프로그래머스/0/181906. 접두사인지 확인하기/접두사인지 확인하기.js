function solution(my_string, is_prefix) {
    var answer = 0;
    if (is_prefix === my_string.substring(0, is_prefix.length)) answer = 1;
    return answer;
}