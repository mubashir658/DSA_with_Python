# Topic 1: Arrays & Lists - Comprehensive Notes

## 📚 What is an Array?

**Array** = Contiguous block of memory storing elements of the same type

### Visual Representation
Index: 0 1 2 3 4
[10] [20] [30] [40] [50]
Mem: 0x1000 0x1004 0x1008 0x1012 0x1016 (4 bytes apart for integers)



- Each element at a specific **index** (position)
- Elements stored **consecutively** in RAM
- Accessing element at index i is **instant** (just calculate position)

## 🐍 Python Lists vs Arrays

### Python Lists (What We Use)
```python
lst = [1, 2, 3, 4, 5]
lst = ["hello", 42, 3.14]  # Can mix types!
```

**Characteristics:**
- ✅ Dynamic (grow/shrink automatically)
- ✅ Flexible (any data type)
- ✅ Built-in (always available)
- ✅ Used in 99% of DSA problems

### Fixed Arrays (Other Languages)
```java
int[] arr = new int[5];  // Only integers, fixed size
```

**Characteristics:**
- ✅ Fixed size (must specify upfront)
- ✅ Type-specific (all same type)
- ✅ Slightly more efficient
- ❌ Less flexible

---

## 🎯 Core Concepts

### 1. INDEXING (O(1) Access)

**Zero-based indexing:**
```python
arr = [10, 20, 30, 40, 50]
       0   1   2   3   4

arr[0]   # 10 (first)
arr[4]   # 50 (last)
arr[2]   # 30 (middle)
```

**Negative indexing:**
```python
arr[-1]   # 50 (last)
arr[-2]   # 40 (second from last)
arr[-5]   # 10 (first)
```

**Why negative indexing?** Useful for accessing from end without calculating length.

### 2. SLICING (O(k) Access)

**Syntax:** `arr[start:stop:step]`
- **start:** Where to begin (default 0)
- **stop:** Where to stop BEFORE (default end)
- **step:** Jump size (default 1)

**Examples:**
```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr[1:4]       # [1, 2, 3] - indices 1,2,3
arr[2:8]       # [2, 3, 4, 5, 6, 7] - indices 2 to 7
arr[::2]       # [0, 2, 4, 6, 8] - every 2nd index
arr[1:8:2]     # [1, 3, 5, 7] - start 1, stop 8, step 2
arr[::-1]      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - REVERSE!
arr[5:]        # [5, 6, 7, 8, 9] - from 5 to end
arr[:5]        # [0, 1, 2, 3, 4] - from start to 5
```

⚠️ **Critical:** Step applies to **indices**, not values!

```python
arr[::3] means:
- Indices: 0, 3, 6, 9
- Values: arr[0], arr[3], arr[6], arr[9] = 0, 3, 6, 9
```

### 3. 2D ARRAYS (Lists of Lists)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access
matrix[0][0]      # 1 (row 0, col 0)
matrix[1][2]      # 6 (row 1, col 2)
matrix[2][1]      # 8 (row 2, col 1)
matrix[-1][-1]    # 9 (bottom-right)

# Iterate
for row in matrix:
    for val in row:
        print(val)

# Transpose
transposed = [[matrix[i][j] for i in range(3)] for j in range(3)]
```

---

## ⏱️ Time Complexity Analysis

| Operation | Time | Why |
|-----------|------|-----|
| **Access** `arr[i]` | **O(1)** | Direct memory access, no searching |
| **Search** (linear) | **O(n)** | Must check each element |
| **Append** (end) | **O(1) amortized** | Usually O(1), occasionally O(n) when resizing |
| **Insert** (middle) | **O(n)** | Must shift all elements after insertion point |
| **Remove** (value) | **O(n)** | Must find it first + shift elements |
| **Pop** (end) | **O(1)** | No shifting needed |
| **Pop** (index i) | **O(n)** | Must shift elements after index i |
| **Sort** | **O(n log n)** | Using efficient algorithms (Timsort in Python) |
| **Reverse** | **O(n)** | Must reverse all elements |
| **Slice** | **O(k)** | k = number of elements in slice |

### Why Insert/Remove are O(n):

Original: [10, 20, 30, 40, 50]
Insert 15 at index 1:

Memory before:
[10] [20] [30] [40] [50]
0 1 2 3 4

Step 1: Shift all elements right from index 1
[10] [__] [20] [30] [40] [50]

Step 2: Place 15 at index 1
[10] [15] [20] [30] [40] [50]

We shifted 4 elements for a list of size 5 → O(n)


---

## 📊 Space Complexity

| Operation | Space |
|-----------|-------|
| Access | O(1) |
| Append | O(1) |
| Insert | O(n) |
| Sort | O(log n) to O(n) |
| Slice | O(k) - creates new list |
| Copy | O(n) |

---

## 🔑 List Comprehensions (Pythonic!)

**Standard approach:**
```python
squares = []
for x in range(5):
    squares.append(x**2)
# squares = [0, 1, 4, 9, 16]
```

**List comprehension (cleaner):**
```python
squares = [x**2 for x in range(5)]
# Same result, more concise
```

**With conditions:**
```python
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

**Nested comprehension:**
```python
matrix = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

---

## 💡 Key Insights

1. **Direct Access:** Arrays excel at O(1) random access
2. **Insertion Cost:** Adding elements in the middle is expensive (O(n))
3. **Dynamic Resizing:** Python automatically grows arrays when needed
4. **Memory Layout:** Understanding contiguous memory helps optimize
5. **Slicing Creates Copy:** `arr[1:3]` returns NEW list, doesn't modify original

---

## ⚠️ Common Mistakes

1. **Index out of bounds:** `arr[10]` when length is 5 → IndexError
2. **Negative indexing confusion:** `arr[-0]` is same as `arr[0]`
3. **Slicing step:** Forgetting step applies to indices: `arr[::2]` ≠ "every 2nd value"
4. **Insert complexity:** Thinking insert at index 0 is O(1) when it's O(n)
5. **Slice creates copy:** `arr2 = arr[:]` is NOT a reference, it's a copy

---

## 🎯 Interview Patterns

1. **Two Pointers:** Use left and right pointers for sorted arrays
2. **Sliding Window:** Maintain a window of elements
3. **Prefix Sum:** Pre-calculate cumulative sums
4. **Binary Search:** On sorted arrays for O(log n) search
5. **Matrix Problems:** Usually need nested loops or 2D indexing

```markdown
Example: Two Pointers
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
```

---

## 📚 Summary

✅ **Use arrays when:**
- Need fast random access (O(1))
- Working with ordered data
- Need to modify elements frequently

❌ **Avoid arrays when:**
- Frequent insertions in middle (O(n))
- Unknown size upfront (but Python handles this!)
- Need O(1) insertion (use Linked Lists instead)

---

## 🚀 What's Next?

In exercises, you'll practice:
- Mastering slicing with different step values
- 2D array manipulation
- Understanding modification complexities
- Using list comprehensions effectively