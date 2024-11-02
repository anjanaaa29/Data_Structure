#-------------recursion------------#

# Time Complexity: O(n), Space Complexity: O(n) due to recursion stack
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
# print(fact(5))

#calculate the nth fibonacci number
# Time Complexity: O(2^n), Space Complexity: O(n) due to recursion stack
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
# print(fibo(4))


# Calculate the sum of the first n natural numbers
# Time Complexity: O(n), Space Complexity: O(n) due to recursion stack
def natural_sum(n):
    if n==0:
        return 0
    else:
        return n+natural_sum(n-1)
# print(natural_sum(10))


    