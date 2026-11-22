# Problem Statement:
# Find the largest number in a given array.

numbers = [10, 25, 8, 45, 32]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Array:", numbers)
print("Largest element:", largest)


# Code Explanation:
# 1. Create an array of numbers.
# 2. Assume the first element is the largest.
# 3. Compare each element with the largest value.
# 4. If a bigger element is found, update largest.
# 5. Print the largest element.

# Output:
# Array: [10, 25, 8, 45, 32]
# Largest element: 45

# Time Complexity: O(n)
# Space Complexity: O(1)
