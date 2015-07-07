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
    
    if element % 5 != 0 and element % 3 != 0:
        number_list.remove(element)
        deleted = deleted + 1
    else:
        index = index + 1

                     
print(sum(number_list))

number_list = [] #created an empty array
multiple_list = [] #created an empty array
index = 0 #created a variable, index, and gave it an initial value of 0

for x in range(1000): #creating an array with 1000 slots
    number_list.append(x) #putting numbers below 1000

element = number_list[index] #created a variable, element, and gave it the value of the item in number_list that had "index" as it's index

while index < 1000: #while the index is less than 1000 (arrays start counting at 0, so the last element's index is going to be 999 - any bigger than this is out of the list's range)
    element = number_list[index] #make sure the element is updated so that we're looking at the next element in the list
    
    if element % 7 == 0: #if the element is divisible by 3
        multiple_list.append(element) #add it to the list of mutiples
        if element % 3 == 0: #if the element is divisble by 5 AND 3
            multiple_list.remove(element) #remove it, because we already counted it

    if element % 3 == 0: #if the element is divisble by 5
        multiple_list.append(element) #add it to the list of mutiples
    

    index += 1 #raise the index to the next numberz

print(sum(multiple_list)) #print out all the multiples of 3 and 5 below 1000




