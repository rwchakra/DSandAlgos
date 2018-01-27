# Code to implement MergeSort


# Function that implements MergeSort recursively

def merge_sort(x):

	n = len(x)
	# Return array if it's empty or has single element
	if n == 0 or n == 1:
		return x

	mid = n/2

	# Recursively call merge_sort until list contains single element

	a = merge_sort(x[:mid])
	b = merge_sort(x[mid:])

	sorted_list = merge(a,b) # Merge the two lists

	return sorted_list

# Function to merge lists

def merge(a,b):

	c = []
	i = 0
	j = 0


	while i < len(a) and j < len(b):

		if a[i] < b[j]:
			c.append(a[i])
			i += 1

		else:
			c.append(b[j])
			j += 1

	
	c += a[i:]
	c += b[j:]


	return c


arr = [17, 20, 26, 31, 44, 54, 55, 77]

merge_sorted = merge_sort(arr)

print merge_sorted

