
def longest_common_subsequence(A, B):
    M, N = len(A), len(B)
    dp = [[0 for j in range(N + 1)] for i in range(M + 1)]
    
    for i in range(M + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                pass
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j -1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    for i in range(M):
        print(dp[i])

if __name__ == '__main__':
    A = 'ABCBDAB'
    B = 'BDCABA'
    
    longest_common_subsequence(A, B)
    