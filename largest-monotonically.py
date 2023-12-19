# Import the bisect_left function from the bisect module
from bisect import bisect_left

# Define the function for finding the Largest Monotonically Increasing Subsequence (LMIS)
def LMIS(arr):
    # Initialize the list for storing the LMIS
    lis = [0]*len(arr)
    # Initialize the length of the LMIS
    length = 0

    # Iterate over the input array
    for i in range(len(arr)):
        # Find the position where arr[i] can be inserted in lis
        pos = bisect_left(lis, arr[i], 0, length)
        # Update the element at the found position
        lis[pos] = arr[i]
        # If arr[i] is larger than all elements in lis, increase the length of the LMIS
        if pos == length:
            length += 1

    # Return the length of the LMIS
    return length

# Read the number of elements
n = int(input())
# Read the elements
arr = list(map(int, input().split()))
# Print the length of the LMIS
print(LMIS(arr))
