# Olivia Ross
# June 2015
# Implementation of an insertion sort, bubble sort, and selection sort in Python 2.7.

import random

### THING TO SORT ###

thelist = random.sample(range(5000), 3)


###### ---- INSERTION SORT ---- ######

def sort_this(mylist):

    index = 0
    
    while not index >= len(mylist) - 1:
        if not mylist[index] <= mylist[index + 1]:
            mylist[index], mylist[index + 1] = mylist[index + 1], mylist[index]
        index += 1
    
    return mylist

#def another_way_to_sort_this(mylist):
#    for index in range( 1, len(mylist) - 1):
#        element = mylist[index]
#        j = index
#        while j > 0 and mylist[[j - 1] > element:
#            mylist[j] = mylist[j - 1]
#            j = j - 1
#        mylist[j] = element


print(thelist)
print(sort_this(thelist))

## Not done. TODO:
##    - make it so that after the comparing the first two elements, we go back and compare the rest too.
