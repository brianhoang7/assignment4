# Author: Brian Hoang
# Date: 10/23/2019
# Description: Asks user for falling time of object and outputs the distance object fell in meters.

#define fall distance function
def fall_distance(g,t):
    #return distance formula
    return g*t**2/2
    #prints result with given values
print(float(fall_distance(9.8,3.2)))