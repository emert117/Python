# Function for nth Fibonacci number
def Fibonacci(n):

	# Check if input is 0 then it will
	# raise an error
	if n < 0:
		raise("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1 or 2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
print(Fibonacci(9))