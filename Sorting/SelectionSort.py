# Implement Selection Sort

# Function to return index of minimum value in array

def minIndex(array, startIndex):

	minValue = array[startIndex]
	minIndex = startIndex

	for i in range(minIndex + 1, len(array)):
    	
		if(array[i] < minValue):
			minIndex = i
			minValue = array[i]

	return minIndex

# Function to swap values

def swap(array, firstIndex, SecondIndex):

	array[firstIndex], array[SecondIndex] = array[SecondIndex], array[firstIndex]

# Function to implement Selection Sort

def selection_sort(array):

	for i in range(0, len(array)):

		min_index = minIndex(array, i)
		swap(array, i, min_index)

	return array


array = [37, 12, 23, 11, 6]

array = selection_sort(array)

print array