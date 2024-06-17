class Solution:
    def dp(self, idx: int, n: int) -> int:
        if idx == 4 or n == 0:
            return 1
        ans = 0
        for i in range(idx, 5):
            ans += self.dp(i, n-1)
        return ans

    def countVowelStrings(self, n: int) -> int:
        return self.dp(0, n)