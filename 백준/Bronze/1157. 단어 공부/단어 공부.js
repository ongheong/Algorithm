const fs = require("fs")
const input = fs.readFileSync("/dev/stdin").toString().trim().toUpperCase();
let dict = {};

for(let c of input){
    if(!(c in dict)){
        dict[c] = 1;
        continue;
    }
    dict[c] += 1;
}

let max = Math.max(...Object.values(dict));
let answer = []

for(key in dict){
    if(dict[key] == max){
        answer.push(key);
    }
}

if(answer.length > 1) {
    console.log('?');
}
else {
    console.log(answer[0]);
}
