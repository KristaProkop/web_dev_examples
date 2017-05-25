import random
from datetime import datetime

startTime = datetime.now()

def insertion_sort(mylist):
    print "\nOriginal List:\n", mylist
    for index in range(1,len(mylist)):
        currentvalue = mylist[index]
        
        while index > 0 and mylist[index-1]>currentvalue:
            mylist[index]=mylist[index-1]
            index = index-1

        mylist[index]=currentvalue
    print "\n Sorted list:"
    return mylist

random_list = [int(10000*random.random()) for i in xrange(100)]
print insertion_sort(random_list)
print "\n Process execution time: ", (datetime.now() - startTime)
