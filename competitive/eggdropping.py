# Title: Egg dropping problem
# source: https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0
# tags: dynamic programming



# code
import sys
# creating a 2d table
dp = [[i for i in range(51)] for j in range(11)]

for i in range(11):
    for j in range(51):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif i == 1 or j ==1:
            dp[i][j] == j
        else:
            dp[i][j] = sys.maxsize
            for x in range(j):
                worst_case = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], worst_case)

for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    print(dp[n][k])
