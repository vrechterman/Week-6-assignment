# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    from collections import Counter
    if not numbers:
        return None
    counts = Counter(numbers)
    return max(counts, key=counts.get)


# Test Cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # expected:3
print(most_frequent([1, 1, 2, 2]))          # expected:1 or 2 because of tie
print(most_frequent([]))                    # expected:is none
print(most_frequent([5]))                   # expected:5

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) 
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(k) where k = will equal the number of unique elements
- Why this approach? this approach because the counter is more efficient and easier to read and or clean for counting frequencies.
- Could it be optimized? all of the elements have to inspected, so nothing significantly beyond O(n).
"""

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# Test Cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # expected:[4, 5, 6, 7]
print(remove_duplicates([]))                  # expected:[]
print(remove_duplicates([1, 1, 1]))           # expected:[1]
print(remove_duplicates([10, 9, 8]))          # expected:[10, 9, 8]

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n), this is because of the storing seen elements.
- Why this approach? I used this approach because this set is able to give O(1) an average lookup, while being able to preserve order efficiently.
- Could it be optimized? It could also use dict.fromkeys(nums) however it would have roughly the same complecity
"""

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


# Test Cases
print(find_pairs([1, 2, 3, 4], 5))     # expected:[(1, 4), (2, 3)]
print(find_pairs([2, 4, 6, 8], 10))    # expected:[(4, 6), (2, 8)]
print(find_pairs([1, 2, 3], 10))       # expected:[]
print(find_pairs([], 5))               # expected:[]

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) same as above, because of the storing seen elements.
- Why this approach? I chose to use a hash set to be able to avoid nested loops.
- Could it be optimized? In my opinion this is optimal enough for this problem.
"""

# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    arr = []
    for i in range(n):
        if len(arr) == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2
            new_arr = arr.copy()
            arr = new_arr
        arr.append(i)
    return arr


# Test Cases
add_n_items(6)  

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes happen when the list is reaching capacity such as (1, 2, 4, 8, …).
- Worst-case for a single append: O(n) when resizing occurs.
- Amortized time per append: O(1), because resizes are infrequent.
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Doubling reduces the cost overall because fewer resizes will make the total cost spread more evenly spreads evenly.
"""

# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result


# Test Cases
print(running_total([1, 2, 3, 4]))   # expected:[1, 3, 6, 10]
print(running_total([0, 0, 0]))      # expected:[0, 0, 0]
print(running_total([]))             # expected:[]
print(running_total([5]))            # expected:[5]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? This approach is more efficient due to the fact that it uses single-pass accumulation.
- Could it be optimized? This is already optimal for this problem.
"""

