# Find factorial of given number

num = 5
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1)

print("Factorial of",num,"is",factorial(num))
