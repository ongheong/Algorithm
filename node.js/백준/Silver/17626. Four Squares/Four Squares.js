const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const n = parseInt(input);

const dp = new Array(n+1).fill(0);
let k = 1;

while (k*k <= n) {
  dp[k*k] = 1
  k++;
}

for (let i = 1; i < n+1; i++) {
  if (dp[i] !== 0) continue // 처음부터 제곱수에 해당하면 넘어가기
  j = 1
  while (j*j <= i) { // 제곱수가 아닌 수일 경우
    if (dp[i] === 0) {
      dp[i] = dp[j*j] + dp[i - j*j]
    } else {
      dp[i] = Math.min(dp[i], dp[j*j] + dp[i - j*j])
    }
    j++;
  }
}

console.log(dp[n]);