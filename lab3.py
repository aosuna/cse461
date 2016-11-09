#Adrian Osuna
#CSE 461 Lab 3 

import string
import random
import time

SIZE = 10

def string_generator():
	files = []
	charSize = 5
	chars = string.ascii_uppercase
	for x in xrange(SIZE):
		files.append(''.join(random.choice(chars) for y in xrange(charSize)))
	return files

def search_unsorted(listArry, check):
	start = time.time()
	if check in listArry:
		print ("Your input is in the array!")
	else:
		print ("Your input is not in the array.")
	stop = time.time()
	return (stop - start)

def search_sorted(listArry, check):
	start = time.time()
	low = 0
	high = len(listArry)
	while low <= high:
		mid = low + (high - low) // 2
		if(check < listArry[mid]):
			high = mid - 1
		elif(check > listArry[mid]):
			if low == mid:
				break
			low = mid + 1
		elif(check == listArry[mid]):
			print ("Your input is in the array at index: "), mid
			break
		else:
			print("Your input was not in the array.")
	stop = time.time()
	return (stop - start)

if __name__ == '__main__':
	inputChk = raw_input("Enter a string of 5 characters long: ")
	if(len(inputChk) != 5):
		print ("Input was invalid, please enter 5 characters")
	else:
		stringInput = string_generator()
		inputChk = inputChk.upper()

		unsortSearch = search_unsorted(stringInput, inputChk)
		print ("Time to search a unsorted list: "),unsortSearch * 1000

		stringInput = sorted(stringInput)

		sortedSearch = search_sorted(stringInput, inputChk)
		print ("Time to search a sorted list: "),sortedSearch * 1000




