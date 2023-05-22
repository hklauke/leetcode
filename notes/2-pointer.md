## Two Pointer Method
- Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.  
- Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
- a naive approach to 2 pointer is to use a double for loop
- The time complexity of this solution is **O(n)** because each element is visited at most twice.

```
# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum
# Using Two-pointers Technique

def isPairSum(arr, X):
	i = 0
	j = len(arr) -1 

	while(i < j):
	
		# If we find a pair
		if (arr[i] + arr[j] == X):
			return True

		# If sum of elements at current
		# pointers is less, we move towards
		# higher values by doing i += 1
		elif(arr[i] + arr[j] < X):
			i += 1

		# If sum of elements at current
		# pointers is more, we move towards
		# lower values by doing j -= 1
		else:
			j -= 1
	return 0

# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 17

print(isPairSum(arr, val))

```

