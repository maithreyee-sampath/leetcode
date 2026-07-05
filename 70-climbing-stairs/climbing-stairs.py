class Solution:
    def climbStairs(self, n: int) -> int:
        num_of_ways = [1,1]

        for i in range(2, n+1):
            num_of_ways.append(num_of_ways[i-1] + num_of_ways[i-2])

        return num_of_ways[n]
