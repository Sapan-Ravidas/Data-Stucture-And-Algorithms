import sys

class Cord:
    def __init__(self, left, right):
        self.left = 0
        self.right = 0
    
    def size(self):
        return self.right - self.left + 1
    
    def __repr__(self):
        return f"({self.left}, {self.right})"
        

def solve(string, n):
    checkPalindrome = [[False for _ in range(n)] for i in range(n)]
    size = [[Cord(0, 0) for _ in range(n)] for i in range(n)]
    left, right = 0, 0
    
    for gap in range(n):
        i = 0
        for j in range(gap, n):
            if gap == 0:
                checkPalindrome[i][j] = True
                size[i][j].left, size[i][j].right = i, j
                continue
            elif gap == 1:
                checkPalindrome[i][j] = string[i] == string[j]
            else:
                checkPalindrome[i][j] = string[i] == string[j] and checkPalindrome[i + 1][j - 1]
            
            # if it is a palindrome
            if checkPalindrome[i][j]:
                # left box
                size[i][j].left, size[i][j].right = i, j
                
                if size[i][j].size() < size[i][j - 1].size():
                    size[i][j].left, size[i][j].right = size[i][j - 1].left, size[i][j - 1].right
                
                # down box
                if size[i][j].size() < size[i + 1][j].size():
                    size[i][j].left, size[i][j] = size[i + 1][j].left, size[i + 1][j].right
            else:
                if size[i][j - 1].size() > size[i + 1][j].size():
                    size[i][j].left, size[i][j].right = size[i][j - 1].left, size[i][j - 1].right
                else:
                    size[i][j].left, size[i][j].right = size[i + 1][j].left, size[i + 1][j].right
            
            i += 1
    
    return string[size[0][n-1].left : size[0][n-1].right + 1]

if __name__ == '__main__':
    string = "abccbc"
    result = solve(string, len(string))
    print(result)
    