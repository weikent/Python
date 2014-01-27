#!/usr/bin/env python



import sys



def median(fileName): 
    '''Return the median of the list of numbers.''' 
    # Sort the list of numbers and take the middle element. 
    numbers = []
    for line in open(fileName).readlines():
        numbers.append(float(line))


    n = len(numbers) 
    copy = numbers[:]
    # So that "numbers" keeps its original order 
    copy.sort() 
    if n & 1: 
        # There is an odd number of elements 
        print "%.15f" % (copy[n / 2])
        return "%.15f" % (copy[n / 2])
    else: 
        print "%.15f" % ((copy[n / 2 - 1] + copy[n / 2]) / 2)
        return "%.15f" % ((copy[n / 2 - 1] + copy[n / 2]) / 2)



if __name__ == '__main__':
    fileName = sys.argv[1]
    median(fileName)
