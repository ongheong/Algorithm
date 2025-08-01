const fs = require("fs");
// 한 줄에 입력 다 받음
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input.shift()); // 배열의 맨 앞 요소 꺼내기 

let arr = [];

for (let i = 0; i < N; i++) {
  arr.push(input[i].split(" ").map((item) => Number(item)));
}

arr.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0]
  } else {
    return a[1] - b[1] 
  }
});

for (let i = 0; i < N; i++) {
  let ans = arr[i].join(" ");
  console.log(ans);
}
