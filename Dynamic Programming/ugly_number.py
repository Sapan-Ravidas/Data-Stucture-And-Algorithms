import itexit, io, sys

buffer = io.StringIO()
sys.stdout = buffer

@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())


def ugly_number(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    i2 = i3 = i5 = 1
    for i in range(1, n+1):
        dp[i] = min(i2 * 2, i3 * 3, i5 * 5)


if __name__=="__main__":
    pass
