const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const alphabetList = "abcdefghijklmnopqrstuvwxyz".split("");

const inputArr = input.split("");

for (let i = 0; i < alphabetList.length; i++) {
  if (inputArr.includes(alphabetList[i])) {
    alphabetList[i] = inputArr.indexOf(alphabetList[i]);
  } else {
    alphabetList[i] = -1;
  }
}

console.log(alphabetList.join(" "));