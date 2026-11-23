# Problem Statement:
# Find the second largest distinct element in an array.

numbers = [10, 25, 8, 45, 32]
largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Array:", numbers)
    print("Second largest element:", second_largest)


# Code Explanation:
# 1. Create an array of numbers.
# 2. Initialize largest and second_largest.
# 3. Traverse each element in the array.
# 4. If an element is greater than largest,
#    update second_largest and largest.
# 5. Otherwise, if it is greater than
#    second_largest and different from largest,
#    update second_largest.
# 6. Print the second largest distinct element.

# Output:
# Array: [10, 25, 8, 45, 32]
# Second largest element: 32

# Time Complexity: O(n)
# Space Complexity: O(1)
