# Define a function to calculate the sum of proper divisors
def sum_proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

# Accept input values from the user
num1, num2 = map(int, input().split(" "))

# Calculate the sum of proper divisors for both numbers
sum1 = sum_proper_divisors(num1)
sum2 = sum_proper_divisors(num2)

# Check if the numbers are amicable
if sum1 == num2 and sum2 == num1:
    print("Amicable")
else:
    print("Not Amicable")
