# time complexity -> O(n^3)
import sys

def palindrom_partitioning(string, n):
    checkPalindrome = [[False for _ in range(n)] for i in range(n)]
    
    # check of paindrom for each substring
    for gap in range(n):
        i = 0
        for j in range(gap, n):
            if gap == 0:
                checkPalindrome[i][j] = True
            elif gap == 1:
                checkPalindrome[i][j] = string[i] == string[j]
            else:
                if string[i] == string[j] and checkPalindrome[i + 1][j - 1]:
                    checkPalindrome[i][j] = True
            i += 1

    # check minimum cut 
    findCut = [[0 for _ in range(n)] for i in range(n)]
    
    for gap in range(1, n):
        # at gap 0 single character is palindrome with mincut 0
        i = 0
        for j in range(gap, n):
            if gap == 1:
                if string[i] == string[j]:
                    pass
                else:
                    findCut[i][j] = 1
            else:
                if not checkPalindrome[i][j]:
                    min_value = sys.maxsize
                    for k in range(i, j):
                        left = findCut[i][k]
                        right = findCut[k + 1][j]
                        print(left, right)
                        if left + right + 1 < min_value:
                            min_value = left + right + 1
                    findCut[i][j] = min_value
            i += 1
    
    for i in range(n):
        print(findCut[i])
    return findCut[0][n - 1]


if __name__ == '__main__':
    string = "abccbc"
    result = palindrom_partitioning(string, len(string))
    print(result)