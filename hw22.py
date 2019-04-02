#Team Wilde Loops -- Patrick Ren, Abir Taheer, Derrick Chen
#IntroCS pd1
#HW22 -- Loopy
#2019-03-12

#sum_digits(n) takes a positive integer n and returns the sum of its digits.
def sum_digits(n):
    sumd = 0 #keeps track of the sum
    while n > 0: #while n still has a positive integer in the ones place
        sumd = sumd + (n % 10) #adds the current ones digit of n to sumd
        n = n // 10 #removes the ones digit of n
    return sumd

print(sum_digits(1))
print("should be 1")
print(sum_digits(27))
print("should be 9")
print(sum_digits(5043))
print("should be 12")

#squares(n) takes a positive integer n and prints each integer from 1 to n, inclusive, along with its square. The number and its square should appear on the same line. 
def squares(n):
    while n > 0: #while n is (an integer) greater than 0 (so that it includes 1)
        m = n ** 2 
        print(n,m) #prints out the value of n followed by the value of m
        n = n - 1 #n becomes one less than it's previous value
        
squares(1)
print("should be 1 1")
squares(5)
print("should be 5 25 / 4 16 / 3 9 / 2 4 / 1 1")
squares(10)
print("should be 10 100 / 9 81 / 8 64 / 7 49 / 6 36 / 5 25 / 4 16 / 3 9 / 2 4 / 1 1")


#sum_perf_sqs(n) takes a positive integer n and returns the sum of the perfect squares between 1 and n, inclusive.
def sum_perf_sqs(n):
    sumsqrs = 0 #keeps track of the sum of the perfect squares
    x = 1 #used to compare the square of x to n
    while x**2 <= n: #while the perfect square is between 1 and n
        sumsqrs = (x**2) + sumsqrs #the perfect square is added to the sum
        x = x + 1 #x increases in value by 1
    return sumsqrs

print(sum_perf_sqs(3))
print("should be 1")
print(sum_perf_sqs(4))
print("should be 5")
print(sum_perf_sqs(16))
print("should be 30")