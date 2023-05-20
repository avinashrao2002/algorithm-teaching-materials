#step 1: 
a = [1,3,4,5,6,7,18,19,20]
#step 2:
# a= [7, 18,19,20]
#step 3:
# a = [19, 20]
#low = 0
#high = len(arr) - 1 = 8

# does 19 exist in the array a
# O(n) - n elements in the array, we have to look at n elements
def basic_search():
    for i in range(len(a)):
        if a[i] == 19:
            return True
    return False
# look at middle - 6

# step 2 - low = 5, high = 8

# step 3 - low = 7, high = 8

# n elements in the array, how many steps to solve. O(log(n))
# say I have 64 elements:
#step 1 - 64
#step 2: 32, step 3 - 16, step 4 - 8, step 5 -4, step 6 - 2, step 7 - 1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
    

def binary_search_iter(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


