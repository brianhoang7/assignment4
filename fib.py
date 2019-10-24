# Author: Brian Hoang
# Date: 10/23/2019
# Description: function that returns nth number in fibonacci sequence

def fib(n):
    #return 1st number in seq, which is 1
    if n == 1:
        return 1
    #return 2nd number in seq, which is 1
    elif n == 2:
        return 1
    #return nth number of sequence
    else:
        return fib(n-1)+fib(n-2)
print(int(fib(9)))