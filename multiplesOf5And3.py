'''
--------------------------------------------------------

PROBLEM ONE
------------
If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
these multiples is 23. Find the sum of all the multiples
of 3 or 5 below 1000.

https://projecteuler.net/problem=1

--------------------------------------------------------

'''

number_list = []

for x in range(1000):
    number_list.append(x)
    

index = 0
element = number_list[index]

max = 1000
deleted = 0

while index < max - deleted:

    element = number_list[index]
    
    if element % 5 != 0:
        number_list.remove(element)
        deleted = deleted + 1
    else if element % 3 != 0:
        number_list.remove(element)
        deleted = deleted + 1
    else:   
        index = index + 1

                     
print(sum(number_list))





