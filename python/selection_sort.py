# First, a way to sort by creating a new list

import random
from datetime import datetime

startTime = datetime.now()

def selection_sort(original_list):
    print "Unsorted List: \n", original_list
    sorted_list = []
    for item in range(len(original_list)):
        sorted_list.append(min(original_list))
        original_list.remove(min(original_list))
    print "Sorted List: "
    return sorted_list

random_list = [int(10000*random.random()) for i in xrange(100)]
print(selection_sort(random_list))


print "\n Process execution time: ", (datetime.now() - startTime)

#next, a way to sort without creating a new list
#COMING SOON

#def new_selection_sort(original_list):
    # print "Unsorted List: \n", original_list
    #      for item in range(len(original_list)):