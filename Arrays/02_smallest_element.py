# Problem Statement:
# Find the smallest number in a given array.

numbers = [10, 25, 8, 45, 32]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Array:", numbers)
print("Smallest element:", smallest)


# Code Explanation:
# 1. Create an array of numbers.
# 2. Assume the first element is the smallest.
# 3. Compare each element with the smallest value.
# 4. If a smaller element is found, update smallest.
# 5. Print the smallest element.

# Output:
# Array: [10, 25, 8, 45, 32]
# Smallest element: 8

# Time Complexity: O(n)
# Space Complexity: O(1)
