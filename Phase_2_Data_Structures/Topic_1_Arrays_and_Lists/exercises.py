"""
Topic 1: Arrays & Lists - Exercises
Try solving these WITHOUT looking at solutions first!
"""

print("=" * 70)
print("EXERCISE 1: Basic Operations & Indexing")
print("=" * 70)

# Given this array
arr = [3, 1, 4, 1, 5, 9, 2, 6]

print(f"Array: {arr}")
print("\nAnswer these questions:")
print("a) Get the 3rd element (index 2)")
print("b) Get the last element")
print("c) Get elements from index 2 to 5 (exclusive)")
print("d) Reverse the array using slicing")
print("e) Count how many 1s are in the array")
print("f) Find the index of the first 5")

print("\n" + "=" * 70)
print("EXERCISE 2: Modification & Time Complexity")
print("=" * 70)

arr = [10, 20, 30]
print(f"Starting array: {arr}")
print("\nFor each operation, predict:")
print("  - What the array becomes after the operation")
print("  - The time complexity (O(1), O(n), O(n log n), etc.)")

print("\nOperation 1: arr.append(40)")
print("  Result: ?")
print("  Time Complexity: ?")

print("\nOperation 2: arr.insert(0, 5)")
print("  Result: ?")
print("  Time Complexity: ?")

print("\nOperation 3: arr.pop()")
print("  Result: ?")
print("  Time Complexity: ?")

print("\nOperation 4: arr.remove(20)")
print("  Result: ?")
print("  Time Complexity: ?")

print("\n" + "=" * 70)
print("EXERCISE 3: Slicing (Tricky!)")
print("=" * 70)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array: {arr}")
print("\nWhat does each line produce?")

print("\nresult1 = arr[2:7]")
print("  Answer: ?")

print("\nresult2 = arr[::3]")
print("  Answer: ?")
print("  Explanation: ?")

print("\nresult3 = arr[-3:]")
print("  Answer: ?")

print("\nresult4 = arr[::-1]")
print("  Answer: ?")

print("\nresult5 = arr[1:8:2]")
print("  Answer: ?")
print("  Explanation: ?")

print("\nresult6 = arr[2:10:3]")
print("  Answer: ?")
print("  Explanation: ?")

print("\n" + "=" * 70)
print("EXERCISE 4: 2D Arrays")
print("=" * 70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nQuestions:")
print("a) Get the element at row 1, column 2")
print("   Answer: ?")

print("\nb) Get the entire second row (index 1)")
print("   Answer: ?")

print("\nc) Get the main diagonal [1, 5, 9]")
print("   Answer: ? (write the code)")

print("\nd) Print all elements in reverse order")
print("   Answer: ? (write the code to do this)")

print("\ne) Create a new matrix with values doubled")
print("   Answer: ? (use list comprehension)")

print("\n" + "=" * 70)
print("EXERCISE 5: List Comprehensions (Bonus)")
print("=" * 70)

print("Write list comprehensions for:")
print("a) All numbers from 1 to 10")
print("   [? for ? in ?]")

print("\nb) Squares of numbers 0 to 9")
print("   [? for ? in ?]")

print("\nc) All even numbers from 0 to 20")
print("   [? for ? in ? if ?]")

print("\nd) All odd numbers from 1 to 20")
print("   [? for ? in ? if ?]")

print("\n" + "=" * 70)
print("Try to solve these WITHOUT looking at solutions!")
print("=" * 70)