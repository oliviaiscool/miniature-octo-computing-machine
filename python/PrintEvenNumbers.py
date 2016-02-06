def find_even_numbers(number):
	counter = 0
	element_number = 0
	number_list = [x for x in range(number + 1)]

	while (counter <= number):
		if number_list[element_number] % 2 == 0: 
			print number_list[element_number]

		element_number += 1
		counter += 1
	

find_even_numbers(33)