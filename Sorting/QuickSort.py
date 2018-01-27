#Implement Quick Sort

#Function to partition the subarray

def partition(array, p, r):

	#Initialise variable q that will assume final pivot position.
	q = p

	#Iterate from p to r - 1. The rightmost element is our pivot, i.e. array[r]

	for j in range(p, r):

		# If element at jth position is <= pivot, increment q and swap j,q

		if array[j] <= array[r]:

			swap(array, q, j)
			q += 1


	# One final swap to put pivot in the correct place
	swap(array, q, r)

	return q

# Function to swap values

def swap(array, first, second):

	array[first], array[second] = array[second], array[first]

	return array

# Function to implement Recursive calls to Quick Sort

def quick_sort(array, p, r):

	if p < r:

		q = partition(array, p, r)
		quick_sort(array, p, q - 1)
		quick_sort(array, q + 1, r)

	return array

arr = [-1, -10, 0, 10, 2]
print quick_sort(arr, 0, len(arr) - 1)

