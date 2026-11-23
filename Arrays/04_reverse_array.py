# Problem Statement:
# Reverse the elements of a given array.

numbers = [10, 20, 30, 40, 50]
left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print("Original Array: [10, 20, 30, 40, 50]")
print("Reversed Array:", numbers)


# Code Explanation:
# 1. Create an array of numbers.
# 2. Initialize left at the first index.
# 3. Initialize right at the last index.
# 4. Use a while loop until left is less than right.
# 5. Swap the elements at the left and right positions.
# 6. Move left one step forward and right one step backward.
# 7. Repeat until the pointers meet or cross.
# 8. Print the reversed array.

# Output:
# Original Array: [10, 20, 30, 40, 50]
# Reversed Array: [50, 40, 30, 20, 10]

# Time Complexity: O(n)
# Space Complexity: O(1)
