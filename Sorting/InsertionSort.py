# Implement Insertion Sort

# Function to insert element in correct position in sorted section

def insert(array, rightIndex, value):

	j = rightIndex

	while(j >= 0 and array[j] > value):

		array[j+1] = array[j]
		j -= 1

	array[j+1] = value

	return array

# Function that implements Insertion Sort
def insertion_sort(array):

	for i in range(1, len(array)):
		insert(array, i - 1, array[i])

	return array

arr = [0,-1,-2]

print insertion_sort(arr)