import sys

def palindrome_partitioning(string, n):
    # find if the substring is palindrome or not
    checkPalindrome = [[False  for _ in range(n)] for i in range(n)]
    
    for gap in range(n):
        i = 0
        for j in range(gap, n):
            if gap == 0:
                checkPalindrome[i][j] = True
            elif gap == 1:
                checkPalindrome[i][j] = string[i] == string[j]
            else:
                checkPalindrome[i][j] = (string[i] == string[j] and checkPalindrome[i + 1][j - 1])
                    
            i += 1
    
    # find min cut
    findCut = [0 for _ in range(n)]
    for i in range(1, n):
        if checkPalindrome[0][i]:
            findCut[i] = 0
            continue
        
        min_value = sys.maxsize
        for j in range(i , 0, -1):
            if checkPalindrome[j][i]:
                if findCut[j - 1] < min_value:
                    min_value = findCut[j - 1]
                    
        findCut[i] = min_value + 1
    print(findCut)
    
    return findCut[n-1]            
    

if __name__ == '__main__':
    string = "abccbc"
    result = palindrome_partitioning(string, len(string))
    print(result)
    