# Author: Brian Hoang
# Date: 10/23/2019
# Description: function that returns distance formula with time and gravity agrument.

#define fall distance function
def fall_distance(g,t):
    #return distance formula
    return g*t**2/2
    #prints result with given values
print(float(fall_distance(9.8,3.2)))