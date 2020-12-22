import math


'''finding the total number of multiplicatios required to perform matrix chain multiplication'''
'''dp is used to return above mentioned'''

'''for split position table Split is used'''

''' top downn approach for matrix chain multiplication'''
def top_down(dimentions):
    n = len(dimentions) - 1
    dp = [[float('inf') for j in range(n)] for i in range(n)]
    Split = [[0 for i in range(n+1)] for j in range(n+1)]
    result =  lookup(dp, dimentions, 0, n-1, Split)
    print("dp table\n")
    for i in range(n):
        print(dp[i])

    print("\n\n Split table\n")
    for i in range(n+1):
        print(Split[i])


def lookup(dp, dimentions, i, j, Split):
    if dp[i][j] < float('inf'):
        return dp[i][j]

    if i == j:
        dp[i][j] = 0
    else:
        for k in range(i, j):
            x = lookup(dp, dimentions, i, k, Split) + lookup(dp, dimentions, k+1, j, Split) +\
                dimentions[i] * dimentions[k+1] * dimentions[j+1]
            if x < dp[i][j]:
                dp[i][j] = x
                Split[i][j] = k + 1

    return dp[i][j]




'''bottom-up approach for matrix chain multiplication'''
def bottom_up(dimentions):
    n = len(dimentions) - 1
    dp = [[math.inf for j in range(n + 1)] for i in range(n + 1)]

    Split = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][i] = 0

    for l in range(2, n+1):
        '''l is the length of chain'''
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j):
                x = dp[i][k] + dp[k+1][j] + dimentions[i-1] * dimentions[k] * dimentions[j]
                if x < dp[i][j]:
                    dp[i][j] = x
                    Split[i][j] = k

    print("dp table\n")
    for i in range(n+1):
        print(dp[i])

    print("\n\n Split table")
    for i in range(n+1):
        print(Split[i])


    '''now we have Split position as well as minimum multiplication required to
    find multiplication of matrices'''


    return dp[1][n]





if __name__=="__main__":
    '''dimention array'''
    dimentions = [1, 2, 1, 4, 1]
    print(top_down(dimentions))
