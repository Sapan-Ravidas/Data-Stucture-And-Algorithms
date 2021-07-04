import sys

def solve(rod, n):
    dp = [0 for _ in range(n+1)]
    dp[1] = rod[0]
    
    for i in range(2, n +1):
        dp[i] = -sys.maxsize
        for j in range(i + 1):
            dp[i] = max(dp[i], rod[j - 1] + dp[i - j])
    print(dp)
    return dp[n]


# alternate method
def solve2(rod, n):
    dp = [0 for i in range(n + 1)]
    dp[1] = rod[0]
    
    for i in range(2, n+1):
        dp[i] = rod[i - 1]
        for j in range(i // 2 + 1):
            dp[i] = max(dp[i], dp[j] + dp[i - j]) 
    print(dp)
    return dp[n]   



if __name__ == '__main__':
    rod = [1, 5, 8, 9, 10, 17, 17, 20]
    result = solve(rod, len(rod))
    print(result)
    