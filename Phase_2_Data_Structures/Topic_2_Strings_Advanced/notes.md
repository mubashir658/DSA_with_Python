# Topic 2: Strings (Advanced) - Comprehensive Notes

## 📚 What is a String?

**String** = Sequence of characters stored in memory

### Key Property: IMMUTABILITY

Once created, strings **cannot be modified**. Any operation returns a new string.

```python
s = "hello"
s[0] = 'x'       # ❌ ERROR: TypeError
s = 'x' + s[1:]  # ✅ Correct: Create new string
```

### Why This Matters

- Algorithm design must account for immutability
- Creating new strings in loops is expensive (O(n) each time)
- Understanding this prevents O(n²) complexity bugs

---

## 🎯 Core Concepts

### 1. INDEXING (O(1) Access)

Strings support the same indexing as lists:

```python
s = "python"
     012345

s[0]    # 'p'
s[5]    # 'n'
s[-1]   # 'n' (last)
s[-2]   # 'o' (second from last)
```

### 2. SLICING (O(k) - Creates New String)

```python
s = "python"

s[1:4]      # "yth" (indices 1,2,3)
s[::2]      # "pto" (every 2nd index)
s[::-1]     # "nohtyp" (reverse)
```

⚠️ **Critical:** Slicing CREATES A NEW STRING (O(k) space and time)

### 3. STRING IMMUTABILITY

```python
s = "hello"
s[0] = 'x'           # ❌ ERROR

# Correct approach: Create new string
s = 'h' + s[1:]      # "hello"
s = 'x' + s[1:]      # "xello"

# Convert to list for multiple modifications
s = "hello"
s_list = list(s)
s_list[0] = 'x'
s_list[2] = 'z'
s = ''.join(s_list)  # "xezlo"
```

---

## 📊 String Methods (O(n) unless noted)

### Case Conversion (O(n) - Creates new string)

```python
s = "Hello World"

s.upper()        # "HELLO WORLD"
s.lower()        # "hello world"
s.title()        # "Hello World"
s.capitalize()   # "Hello world"
s.swapcase()     # "hELLO wORLD"
```

### Searching (O(n*m) where m = pattern length)

```python
s = "hello world"

s.find('o')          # 4 (first index, or -1 if not found)
s.rfind('o')         # 7 (last index)
s.index('o')         # 4 (like find, but raises error if not found)
s.count('l')         # 3 (how many occurrences)
s.startswith('hello')  # True
s.endswith('world')  # True
'o' in s             # True (O(n))
```

### Splitting & Joining (O(n))

```python
s = "hello world python"

s.split()            # ['hello', 'world', 'python'] (split by whitespace)
s.split(' ')         # ['hello', 'world', 'python'] (split by space)
s.split('o')         # ['hell', ' w', 'rld pyth', 'n'] (split by 'o')

",".join(['a', 'b']) # "a,b" (join with separator)
" ".join("abc")      # "a b c" (join characters)
```

### Replacing (O(n))

```python
s = "hello world"

s.replace('o', '0')       # "hell0 w0rld" (replace all)
s.replace('o', '0', 1)    # "hell0 world" (replace first only)
```

### Stripping Whitespace (O(n))

```python
s = "  hello  "

s.strip()    # "hello" (remove both ends)
s.lstrip()   # "hello  " (remove left)
s.rstrip()   # "  hello" (remove right)
```

### Checking Content

```python
"123".isdigit()       # True
"abc".isalpha()       # True
"abc123".isalnum()    # True
"   ".isspace()       # True
"Hello".isupper()     # False
"hello".islower()     # True
```

### Padding

```python
"5".zfill(3)          # "005"
"5".ljust(5, '-')     # "5----"
"5".rjust(5, '-')     # "----5"
"5".center(7, '-')    # "--5----"
```

---

## 🔤 Character Operations

### ASCII Values

```python
ord('A')              # 65 (char → ASCII)
chr(65)               # 'A' (ASCII → char)

# Useful ranges:
ord('a')              # 97
ord('z')              # 122
ord('A')              # 65
ord('Z')              # 90
ord('0')              # 48
ord('9')              # 57
```

---

## ⏱️ Time Complexity Analysis

| Operation | Time | Why |
|-----------|------|-----|
| **Access** `s[i]` | **O(1)** | Direct memory access |
| **Slice** `s[a:b]` | **O(k)** | k = slice size (creates new string) |
| **Search** `s.find(x)` | **O(n*m)** | n = string length, m = pattern length |
| **Contains** `x in s` | **O(n*m)** | Same as find |
| **Replace** `s.replace(x, y)` | **O(n)** | Creates new string |
| **Split** `s.split()` | **O(n)** | Creates list of strings |
| **Join** `','.join(lst)` | **O(n)** | n = total characters |
| **Upper/Lower** | **O(n)** | Creates new string |
| **Concatenation** `s + t` | **O(n+m)** | Creates new string |

### 🔥 CRITICAL: String Concatenation in Loops

**❌ BAD - O(n²)**
```python
result = ""
for char in string:      # n iterations
    result += char       # Each += creates new string (O(n))
# Total: O(n²) complexity!
```

**✅ GOOD - O(n)**
```python
result = ''.join(list(string))  # Single operation, O(n)
```

---

## 🔑 Interview Patterns

### Pattern 1: Character Frequency

```python
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("aabbcc"))
# {'a': 2, 'b': 2, 'c': 2}
```

**Time:** O(n)  
**Space:** O(k) where k = unique characters

### Pattern 2: Palindrome Detection

**Approach 1: Two Pointers**
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Approach 2: Reversal**
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

**Time:** O(n)  
**Space:** O(1) for two-pointer, O(n) for reversal

### Pattern 3: Reverse Words

```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("hello world python"))
# "python world hello"
```

**Time:** O(n)  
**Space:** O(n)

### Pattern 4: Anagrams

```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
    # OR
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())
```

**Time:** O(n log n) due to sorting  
**Space:** O(n)

---

## 💡 String vs List Conversion

```python
# WHEN TO CONVERT
s = "hello"
s_list = list(s)     # ['h', 'e', 'l', 'l', 'o']

# MODIFY IN LIST (mutable)
s_list[0] = 'x'      # ['x', 'e', 'l', 'l', 'o']

# CONVERT BACK
s = ''.join(s_list)  # "xello"
```

---

## 📚 F-strings (Modern Python)

```python
name = "Alice"
age = 25
score = 95.5

f"{name} is {age}"                # "Alice is 25"
f"{name.upper()} scored {score:.1f}"  # "ALICE scored 95.5"
```

---

## ⚠️ Common Mistakes

1. **Thinking strings are mutable:** Can't modify in-place
2. **String concatenation in loops:** Creates O(n²) complexity
3. **Case-sensitive searching:** 'A' ≠ 'a'
4. **Index out of bounds:** Similar to lists
5. **Slice includes start, excludes stop:** `s[1:3]` = indices 1 and 2

---

## 🎯 Summary

✅ **Use strings when:**
- Working with text data
- Need immutability (hashable, can use as dict keys)
- Performing character-level operations

❌ **Avoid when:**
- Need frequent modifications (convert to list)
- Doing many concatenations (use join())
- Need O(1) insertion/deletion (use different DS)

---

## 🚀 What's Next?

In exercises, you'll practice:
- String indexing and slicing
- String methods (upper, lower, find, split, replace)
- Character frequency counting
- Palindrome detection
- String reversal and manipulation