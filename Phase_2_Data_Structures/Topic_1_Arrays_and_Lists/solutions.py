"""
Topic 1: Arrays & Lists - SOLUTIONS
Only look at this AFTER trying the exercises yourself!
"""

print("=" * 70)
print("EXERCISE 1: Basic Operations & Indexing - SOLUTIONS")
print("=" * 70)

arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Array: {arr}\n")

# a) Get the 3rd element (index 2)
print("a) Get the 3rd element (index 2)")
print(f"   Solution: arr[2]")
print(f"   Result: {arr[2]}")

# b) Get the last element
print("\nb) Get the last element")
print(f"   Solution: arr[-1]")
print(f"   Result: {arr[-1]}")

# c) Get elements from index 2 to 5 (exclusive)
print("\nc) Get elements from index 2 to 5 (exclusive)")
print(f"   Solution: arr[2:5]")
print(f"   Result: {arr[2:5]}")

# d) Reverse the array using slicing
print("\nd) Reverse the array using slicing")
print(f"   Solution: arr[::-1]")
print(f"   Result: {arr[::-1]}")

# e) Count how many 1s are in the array
print("\ne) Count how many 1s are in the array")
print(f"   Solution: arr.count(1)")
print(f"   Result: {arr.count(1)}")

# f) Find the index of the first 5
print("\nf) Find the index of the first 5")
print(f"   Solution: arr.index(5)")
print(f"   Result: {arr.index(5)}")

print("\n" + "=" * 70)
print("EXERCISE 2: Modification & Time Complexity - SOLUTIONS")
print("=" * 70)

print("Starting with: arr = [10, 20, 30]\n")

print("Operation 1: arr.append(40)")
arr = [10, 20, 30]
arr.append(40)
print(f"  Result: {arr}")
print(f"  Time Complexity: O(1) amortized")
print(f"  Why: Appending to end usually doesn't require shifting")

print("\nOperation 2: arr.insert(0, 5)")
arr = [10, 20, 30, 40]
arr.insert(0, 5)
print(f"  Result: {arr}")
print(f"  Time Complexity: O(n)")
print(f"  Why: Must shift all 4 elements to the right")

print("\nOperation 3: arr.pop()")
arr = [5, 10, 20, 30, 40]
removed = arr.pop()
print(f"  Result: {arr}")
print(f"  Removed: {removed}")
print(f"  Time Complexity: O(1)")
print(f"  Why: Removing from end requires no shifting")

print("\nOperation 4: arr.remove(20)")
arr = [5, 10, 20, 30, 40]
arr.remove(20)
print(f"  Result: {arr}")
print(f"  Time Complexity: O(n)")
print(f"  Why: Must find (O(n)) + shift elements (O(n))")

print("\n" + "=" * 70)
print("EXERCISE 3: Slicing - SOLUTIONS")
print("=" * 70)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array: {arr}\n")

result1 = arr[2:7]
print(f"result1 = arr[2:7]")
print(f"  Answer: {result1}")
print(f"  Explanation: Start at index 2, stop before 7 (indices 2,3,4,5,6)")

result2 = arr[::3]
print(f"\nresult2 = arr[::3]")
print(f"  Answer: {result2}")
print(f"  Explanation: Every 3rd INDEX: 0, 3, 6, 9")

result3 = arr[-3:]
print(f"\nresult3 = arr[-3:]")
print(f"  Answer: {result3}")
print(f"  Explanation: Last 3 elements (indices 7, 8, 9)")

result4 = arr[::-1]
print(f"\nresult4 = arr[::-1]")
print(f"  Answer: {result4}")
print(f"  Explanation: Reverse array (step -1)")

result5 = arr[1:8:2]
print(f"\nresult5 = arr[1:8:2]")
print(f"  Answer: {result5}")
print(f"  Explanation: Start 1, stop before 8, step 2 → indices 1,3,5,7")

result6 = arr[2:10:3]
print(f"\nresult6 = arr[2:10:3]")
print(f"  Answer: {result6}")
print(f"  Explanation: Start 2, stop before 10, step 3 → indices 2,5,8")

print("\n" + "=" * 70)
print("EXERCISE 4: 2D Arrays - SOLUTIONS")
print("=" * 70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nSolutions:")

# a) Get element at row 1, column 2
print("\na) Get element at row 1, column 2")
print(f"   Solution: matrix[1][2]")
print(f"   Result: {matrix[1][2]}")

# b) Get entire second row (index 1)
print("\nb) Get entire second row (index 1)")
print(f"   Solution: matrix[1]")
print(f"   Result: {matrix[1]}")

# c) Get main diagonal [1, 5, 9]
print("\nc) Get main diagonal [1, 5, 9]")
print(f"   Solution 1: [matrix[i][i] for i in range(3)]")
diagonal = [matrix[i][i] for i in range(3)]
print(f"   Result: {diagonal}")
print(f"   Solution 2: [matrix[i][j] for i in range(3) for j in range(3) if i==j]")

# d) Print all elements in reverse order
print("\nd) Print all elements in reverse order (bottom-right to top-left)")
print(f"   Solution:")
print(f"   for i in range(len(matrix)-1, -1, -1):")
print(f"       for j in range(len(matrix[i])-1, -1, -1):")
print(f"           print(matrix[i][j])")
print(f"   Output: ", end="")
for i in range(len(matrix)-1, -1, -1):
    for j in range(len(matrix[i])-1, -1, -1):
        print(matrix[i][j], end=" ")
print()

# e) Double all values
print("\ne) Create new matrix with values doubled")
print(f"   Solution: [[val*2 for val in row] for row in matrix]")
doubled = [[val*2 for val in row] for row in matrix]
print(f"   Result:")
for row in doubled:
    print(f"      {row}")

print("\n" + "=" * 70)
print("EXERCISE 5: List Comprehensions - SOLUTIONS")
print("=" * 70)

# a) Numbers 1 to 10
result_a = [x for x in range(1, 11)]
print(f"a) Numbers 1 to 10:")
print(f"   [x for x in range(1, 11)]")
print(f"   Result: {result_a}")

# b) Squares of 0 to 9
result_b = [x**2 for x in range(10)]
print(f"\nb) Squares of numbers 0 to 9:")
print(f"   [x**2 for x in range(10)]")
print(f"   Result: {result_b}")

# c) Even numbers 0 to 20
result_c = [x for x in range(21) if x % 2 == 0]
print(f"\nc) Even numbers 0 to 20:")
print(f"   [x for x in range(21) if x % 2 == 0]")
print(f"   Result: {result_c}")

# d) Odd numbers 1 to 20
result_d = [x for x in range(1, 21) if x % 2 == 1]
print(f"\nd) Odd numbers 1 to 20:")
print(f"   [x for x in range(1, 21) if x % 2 == 1]")
print(f"   Result: {result_d}")

print("\n" + "=" * 70)
print("All solutions completed!")
print("=" * 70)