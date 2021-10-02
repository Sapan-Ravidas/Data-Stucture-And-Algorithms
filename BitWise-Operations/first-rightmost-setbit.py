# find 1st set bit in a number N 
# eg. 4 -> 100
# ans- 3

def solve(n):
    mask = 1
    count = 1
    while mask & n == 0:
        count += 1
        n = n >> 1
    return count


if __name__ == '__main__':
    n = int(input())
    result = solve(n)
    print(result)
    