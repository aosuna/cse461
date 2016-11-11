#Adrian Osuna
#CSE 461 - Dr. Gomez
#Lab 3
# -*- coding: utf-8 -*-
import string
import random
import time
import numpy

SIZE = 10000
sizeHash = SIZE * 2

def string_generator():
	files = []
	charSize = 5
	chars = string.ascii_uppercase
	for x in xrange(SIZE):
		files.append(''.join(random.choice(chars) for y in xrange(charSize)))
	return files

def search_unsorted(listArry, check):
	start = time.time()
	for x in xrange(len(listArry)):
		if listArry[x] == check:
			#print ("Your input is in the array!"), x
			break
	stop = time.time()
	return (stop - start)

def hashIt(listArry):
	hash_table = [[] for x in xrange(sizeHash)]
	for x in xrange(len(listArry)):
		hashVal = hash(listArry[x]) % sizeHash
		hash_table[hashVal].append(listArry[x])
	return hash_table

def search_hash(hashtable, check):
	search = hash(check) % sizeHash
	start = time.time()
	for x in hashtable[search]:
		if x == check:
			#print("Your input is in the array!")
			break
	stop = time.time()
	return(stop - start)

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
				#print("Your input was not in the array.")
				break
			low = mid + 1
		elif(check == listArry[mid]):
			#print ("Your input is in the array at index: "), mid
			break
	stop = time.time()
	return (stop - start)

if __name__ == '__main__':
	unsort = []
	binsearch = []
	hashlook = []
	for x in xrange(100):
		stringInput = string_generator()
		inputChk = stringInput[random.randint(0,SIZE-1)]
		inputChk = inputChk.upper()
		#print inputChk
		unsortSearch = search_unsorted(stringInput, inputChk)
		unsort.append(unsortSearch * 1000)
		sortInput = sorted(stringInput)
		sortedSearch = search_sorted(sortInput, inputChk)
		binsearch.append(sortedSearch * 1000)
		hashSearch = search_hash(hashIt(stringInput), inputChk)
		hashlook.append(hashSearch * 1000)

	print("Average for 100 list; unsorted list : "), numpy.mean(unsort)
	print("Average for 100 list; binary search : "), numpy.mean(binsearch)
	print("Average for 100 list; hash look up  : "), numpy.mean(hashlook)

