class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0: dp[i] = 0
            elif i == 1: dp[i] = 0
            else: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        print(dp)
        return dp[n]
                