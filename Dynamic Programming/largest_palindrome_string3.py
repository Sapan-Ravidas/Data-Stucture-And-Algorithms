# Python program

import sys

def printString(st, low, high) :
	sys.stdout.write(st[low : high + 1])
	sys.stdout.flush()
	return ''

def largest_palindrome(st) :
	n = len(st) 

	dp = [[0 for x in range(n)] for y
						in range(n)]

	maxLength = 1
	i = 0
	while (i < n) :
		dp[i][i] = True
		i = i + 1

	start = 0
	i = 0
	while i < n - 1 :
		if (st[i] == st[i + 1]) :
			dp[i][i + 1] = True
			start = i
			maxLength = 2
		i = i + 1

	k = 3
	while k <= n :

		i = 0
		while i < (n - k + 1) :

			j = i + k - 1
	
			if (dp[i + 1][j - 1] and
					st[i] == st[j]) :
				dp[i][j] = True
	
				if (k > maxLength) :
					start = i
					maxLength = k
			i = i + 1
		k = k + 1
	print (printString(st, start,start + maxLength - 1))
 
 
st = input()
largest_palindrome(st)

