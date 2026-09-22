"""
Topic 1: Arrays & Lists - Complete Implementation Examples
Master all array/list operations with time complexity analysis
"""

# ============================================================================
# PART A: CREATION & BASIC ACCESS (O(1))
# ============================================================================

print("=" * 70)
print("PART A: CREATION & BASIC ACCESS")
print("=" * 70)

# CREATE LISTS
arr = []                      # Empty list
arr = [1, 2, 3, 4, 5]        # With initial values
arr = list(range(5))          # [0, 1, 2, 3, 4]
arr = [0] * 5                 # [0, 0, 0, 0, 0] (replicate)
arr = [x for x in range(5)]   # [0, 1, 2, 3, 4] (comprehension)

print(f"List: {arr}")
print(f"Length: {len(arr)}")  # O(1)

# ACCESS BY INDEX (O(1) - Instant!)
arr = [10, 20, 30, 40, 50]
print(f"\nIndexing Examples:")
print(f"arr[0] = {arr[0]}")        # 10 (first)
print(f"arr[4] = {arr[4]}")        # 50 (last)
print(f"arr[2] = {arr[2]}")        # 30 (middle)
print(f"arr[-1] = {arr[-1]}")      # 50 (last using negative)
print(f"arr[-2] = {arr[-2]}")      # 40 (second from last)
print(f"arr[-5] = {arr[-5]}")      # 10 (first using negative)

# ============================================================================
# PART B: SLICING (O(k) where k = slice size)
# ============================================================================

print("\n" + "=" * 70)
print("PART B: SLICING")
print("=" * 70)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original array: {arr}")

print("\n--- Basic Slicing ---")
print(f"arr[1:4]     = {arr[1:4]}")        # [1, 2, 3] (indices 1,2,3)
print(f"arr[2:7]     = {arr[2:7]}")        # [2, 3, 4, 5, 6]
print(f"arr[:3]      = {arr[:3]}")         # [0, 1, 2] (from start)
print(f"arr[6:]      = {arr[6:]}")         # [6, 7, 8, 9] (to end)
print(f"arr[:]       = {arr[:]}")          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (full copy)

print("\n--- Slicing with STEP (Critical!) ---")
print(f"arr[::2]     = {arr[::2]}")        # [0, 2, 4, 6, 8] (every 2nd INDEX)
print(f"arr[1:8:2]   = {arr[1:8:2]}")      # [1, 3, 5, 7] (start 1, stop 8, step 2)
print(f"arr[::3]     = {arr[::3]}")        # [0, 3, 6, 9] (every 3rd INDEX)
print(f"arr[2:10:3]  = {arr[2:10:3]}")     # [2, 5, 8] (start 2, stop 10, step 3)

print("\n--- REVERSE with Step ---")
print(f"arr[::-1]    = {arr[::-1]}")       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] REVERSE!
print(f"arr[8:2:-1]  = {arr[8:2:-1]}")     # [8, 7, 6, 5, 4] (reverse from 8 to 3)

print("\n--- Negative Indexing in Slicing ---")
print(f"arr[-3:]     = {arr[-3:]}")        # [7, 8, 9] (last 3 elements)
print(f"arr[:-2]     = {arr[:-2]}")        # [0, 1, 2, 3, 4, 5, 6, 7, 8] (exclude last 2)

# ============================================================================
# PART C: MODIFICATION OPERATIONS
# ============================================================================

print("\n" + "=" * 70)
print("PART C: MODIFICATION OPERATIONS")
print("=" * 70)

arr = [10, 20, 30, 40, 50]
print(f"Original: {arr}")

# APPEND (O(1) amortized)
print("\n--- APPEND (Add to end, O(1)) ---")
arr.append(60)
print(f"After append(60): {arr}")

# INSERT (O(n) - shifts elements!)
print("\n--- INSERT (Add at position, O(n)) ---")
arr_copy = arr.copy()
arr_copy.insert(1, 15)  # Insert 15 at index 1
print(f"After insert(1, 15): {arr_copy}")
print("⚠️ O(n) because all elements after index 1 shift right!")

# REMOVE (O(n) - find + shift)
print("\n--- REMOVE (Delete by value, O(n)) ---")
arr_copy = arr.copy()
arr_copy.remove(30)  # Remove element with value 30
print(f"After remove(30): {arr_copy}")

# POP (O(1) if last, O(n) if middle)
print("\n--- POP (Remove by index) ---")
arr_copy = arr.copy()
last = arr_copy.pop()  # Remove last element (O(1))
print(f"After pop(): {arr_copy}, removed: {last}")

arr_copy = arr.copy()
middle = arr_copy.pop(1)  # Remove index 1 (O(n))
print(f"After pop(1): {arr_copy}, removed: {middle}")

# EXTEND (O(k) where k = number of elements)
print("\n--- EXTEND (Add multiple elements, O(k)) ---")
arr_copy = [10, 20]
arr_copy.extend([30, 40, 50])
print(f"After extend([30, 40, 50]): {arr_copy}")

# MODIFY ELEMENT (O(1))
print("\n--- MODIFY (Change element, O(1)) ---")
arr_copy = [10, 20, 30]
arr_copy[1] = 200
print(f"After arr[1] = 200: {arr_copy}")

# SORT (O(n log n))
print("\n--- SORT (O(n log n)) ---")
arr_copy = [5, 2, 8, 1, 9]
arr_copy.sort()
print(f"After sort(): {arr_copy}")

arr_copy.sort(reverse=True)
print(f"After sort(reverse=True): {arr_copy}")

# REVERSE (O(n))
print("\n--- REVERSE (O(n)) ---")
arr_copy = [1, 2, 3, 4, 5]
arr_copy.reverse()
print(f"After reverse(): {arr_copy}")

# CLEAR (O(n))
print("\n--- CLEAR (Remove all, O(n)) ---")
arr_copy = [1, 2, 3]
arr_copy.clear()
print(f"After clear(): {arr_copy}")

# ============================================================================
# PART D: SEARCH OPERATIONS (O(n))
# ============================================================================

print("\n" + "=" * 70)
print("PART D: SEARCH OPERATIONS (O(n))")
print("=" * 70)

arr = [10, 20, 30, 20, 40, 50, 20]
print(f"Array: {arr}")

print(f"\narr.count(20)        = {arr.count(20)}")        # 3 (how many 20s?)
print(f"20 in arr            = {20 in arr}")            # True (membership)
print(f"99 in arr            = {99 in arr}")            # False
print(f"arr.index(20)        = {arr.index(20)}")        # 1 (first occurrence)

# ============================================================================
# PART E: 2D ARRAYS (Lists of Lists)
# ============================================================================

print("\n" + "=" * 70)
print("PART E: 2D ARRAYS")
print("=" * 70)

# CREATE 2D ARRAY
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# ACCESS
print(f"\nmatrix[0][0] = {matrix[0][0]}")    # 1 (top-left)
print(f"matrix[1][2] = {matrix[1][2]}")     # 6 (middle-right)
print(f"matrix[2][2] = {matrix[2][2]}")     # 9 (bottom-right)
print(f"matrix[-1][-1] = {matrix[-1][-1]}")  # 9 (bottom-right using negative)

# ITERATE 2D ARRAY
print("\nIterate all elements:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# CREATE WITH COMPREHENSION
print("\n--- 2D Comprehension ---")
matrix2 = [[i + j for j in range(3)] for i in range(3)]
print("Matrix created with comprehension [[i+j for j in range(3)] for i in range(3)]:")
for row in matrix2:
    print(row)

# TRANSPOSE
print("\n--- TRANSPOSE ---")
matrix_t = [[matrix[i][j] for i in range(3)] for j in range(3)]
print("Transposed matrix:")
for row in matrix_t:
    print(row)

# ============================================================================
# PART F: LIST COMPREHENSIONS (Pythonic!)
# ============================================================================

print("\n" + "=" * 70)
print("PART F: LIST COMPREHENSIONS")
print("=" * 70)

# BASIC COMPREHENSION
result = [x for x in range(5)]
print(f"[x for x in range(5)] = {result}")

# WITH TRANSFORMATION
result = [x*2 for x in range(5)]
print(f"[x*2 for x in range(5)] = {result}")

# WITH CONDITION
result = [x for x in range(10) if x % 2 == 0]
print(f"[x for x in range(10) if x % 2 == 0] = {result}")

# NESTED COMPREHENSION
result = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nNested comprehension (multiplication table):")
for row in result:
    print(row)

# ============================================================================
# PART G: COMMON ARRAY PATTERNS
# ============================================================================

print("\n" + "=" * 70)
print("PART G: COMMON ARRAY PATTERNS")
print("=" * 70)

# PATTERN 1: TWO POINTERS
print("\n--- TWO POINTERS (Sorted array) ---")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11

left, right = 0, len(arr) - 1
found = False
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print(f"Found pair: {arr[left]} + {arr[right]} = {target}")
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if not found:
    print(f"No pair found for target {target}")

# PATTERN 2: PREFIX SUM
print("\n--- PREFIX SUM ---")
arr = [1, 2, 3, 4, 5]
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)
print(f"Array: {arr}")
print(f"Prefix sum: {prefix}")
print("Use case: Quick range sum queries")

# PATTERN 3: SLIDING WINDOW
print("\n--- SLIDING WINDOW ---")
arr = [1, 2, 3, 4, 5, 6, 7, 8]
window_size = 3
for i in range(len(arr) - window_size + 1):
    window = arr[i:i + window_size]
    print(f"Window {i}: {window}, Sum: {sum(window)}")

# ============================================================================
# SUMMARY TABLE
# ============================================================================

print("\n" + "=" * 70)
print("TIME COMPLEXITY SUMMARY")
print("=" * 70)

complexity_table = """
Operation           | Time         | Space | Notes
--------------------|--------------|-------|------------------------------------------
Access arr[i]       | O(1)         | -     | Direct memory access
Search              | O(n)         | -     | Linear search required
Append (end)        | O(1) amort.  | -     | Usually O(1), sometimes O(n) resize
Insert (position)   | O(n)         | -     | Must shift elements
Pop (last)          | O(1)         | -     | No shifting needed
Pop (index)         | O(n)         | -     | Must shift after index
Remove (value)      | O(n)         | -     | Find + shift
Sort                | O(n log n)   | O(logn-n) | Timsort in Python
Reverse             | O(n)         | -     | Reverse all elements
Slice               | O(k)         | O(k)  | k = slice size (creates new list)
Contains (in)       | O(n)         | -     | Check each element
"""

print(complexity_table)

print("=" * 70)
print("End of Arrays & Lists Implementation")
print("=" * 70)