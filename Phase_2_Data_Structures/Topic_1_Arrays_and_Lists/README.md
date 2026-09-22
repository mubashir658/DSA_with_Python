# Topic 1: Arrays & Lists

## 📚 Concept
Arrays/Lists are contiguous memory blocks storing elements. Python lists 
are dynamic arrays that automatically resize.

## 🎯 What You'll Learn
✅ Indexing and slicing (including negative indices)  
✅ 2D arrays (lists of lists)  
✅ Modification operations and their complexity  
✅ List comprehensions  
✅ Common patterns (rotation, searching, sorting)  

## ⏱️ Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Access `arr[i]` | O(1) | - |
| Search | O(n) | - |
| Append | O(1) amortized | - |
| Insert | O(n) | - |
| Pop last | O(1) | - |
| Pop index i | O(n) | - |
| Sort | O(n log n) | O(log n-n) |

## 📝 Files in This Topic

- `notes.md` — Concept explanation and intuition
- `implementation.py` — Code examples and patterns
- `exercises.py` — Problems to solve
- `solutions.py` — My solutions with explanations

## 🎯 Exercises
- Exercise 1: Type conversion & operators ✅
- Exercise 2: Modulo & integer division ✅
- Exercise 3: Boolean logic ✅
- Exercise 4: 2D arrays ✅

**Score:** 4/4 ✅

## 🔑 Key Patterns
1. **Slicing:** `arr[start:stop:step]`
2. **Negative indexing:** `arr[-1]` = last element
3. **2D access:** `matrix[i][j]`
4. **List comprehension:** `[x*2 for x in arr]`

## 💡 Interview Tips
- Master slicing — appears in 30% of array problems
- Two-pointer technique for array problems
- Be careful with insert/remove complexity
- Use in-place modifications when possible (saves space)

## 📚 Related LeetCode Problems
- Two Sum
- Best Time to Buy and Sell Stock
- Container With Most Water
- Remove Duplicates from Sorted Array