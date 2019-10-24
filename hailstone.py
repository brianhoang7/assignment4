# Author: Brian Hoang
# Date: 10/23/2019
# Description: function that returns # of steps to reach 1 in hailstone sequence when starting at n

def hailstone(n):
    #count variable is increased everytime loop is ran
    count=0
    #runs loop until n=1
    while n!=1:
        #if number is even, divide by 2
        if(n%2) == 0:
            n=n/2
            count+=1
        #if number is odd, multiply by 3 and add 1
        else:
            n=n*3+1
            count+=1
    #return number it takes to get to 1
    return count
print(int(hailstone(3)))


