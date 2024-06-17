function solution(phoneBook) {
    let answer = true;
    phoneBook.sort();
    let lg = phoneBook.length;
    for (let i = 0; i < lg - 1; i++){
        if (phoneBook[i] === phoneBook[i+1].substring(0, phoneBook[i].length)) {
            answer = false;
            return answer;
        }
    }
    return answer;
}