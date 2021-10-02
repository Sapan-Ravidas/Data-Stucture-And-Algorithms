# find right most diiferent bit
# a = 10 -> 1010
# b = 14 -> 1110
# ans -> 3

def solve(a, b):
    mask = 1
    count = 1
    while (a & mask) == (b & mask):
        count += 1
        mask = mask << 1
    return count

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result)
    