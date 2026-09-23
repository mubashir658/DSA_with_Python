"""
Topic 2: Strings (Advanced) - Complete Implementation Examples
Master all string operations and patterns with time complexity analysis
"""

print("=" * 70)
print("STRINGS (ADVANCED) - COMPLETE IMPLEMENTATION")
print("=" * 70)

# ============================================================================
# PART A: CREATION & INDEXING (O(1))
# ============================================================================

print("\n" + "=" * 70)
print("PART A: CREATION & INDEXING")
print("=" * 70)

# CREATE STRINGS
s = "hello"
s = 'hello'              # Single or double quotes (same)
s = """multi
line
string"""               # Multi-line
s = str(123)            # Convert to string "123"

s = "python"
print(f"String: {s}")
print(f"Length: {len(s)}")  # O(1)

# INDEXING (O(1))
print("\n--- Indexing Examples ---")
print(f"s[0] = {s[0]}")         # 'p' (first)
print(f"s[5] = {s[5]}")         # 'n' (last)
print(f"s[2] = {s[2]}")         # 't' (middle)
print(f"s[-1] = {s[-1]}")       # 'n' (last using negative)
print(f"s[-2] = {s[-2]}")       # 'o' (second from last)
print(f"s[-6] = {s[-6]}")       # 'p' (first using negative)

# IMMUTABILITY DEMONSTRATION
print("\n--- String Immutability ---")
print(f"Original string: {s}")
# s[0] = 'x'  # ❌ This would cause ERROR: TypeError

# Correct way: Create new string
s_modified = 'x' + s[1:]
print(f"After modifying first char: {s_modified}")

# ============================================================================
# PART B: SLICING (O(k) - Creates new string)
# ============================================================================

print("\n" + "=" * 70)
print("PART B: SLICING")
print("=" * 70)

s = "programming"
print(f"String: {s}")

print("\n--- Basic Slicing ---")
print(f"s[0:3]    = {s[0:3]}")      # 'pro' (indices 0,1,2)
print(f"s[3:9]    = {s[3:9]}")      # 'gramm' (indices 3-8)
print(f"s[:5]     = {s[:5]}")       # 'progr' (from start)
print(f"s[6:]     = {s[6:]}")       # 'amming' (to end)
print(f"s[:]      = {s[:]}")        # 'programming' (full copy)

print("\n--- Slicing with STEP ---")
print(f"s[::2]    = {s[::2]}")      # 'pormig' (every 2nd INDEX)
print(f"s[1::2]   = {s[1::2]}")     # 'ogrann' (start 1, every 2nd)
print(f"s[::3]    = {s[::3]}")      # 'pramn' (every 3rd INDEX)

print("\n--- REVERSE ---")
print(f"s[::-1]   = {s[::-1]}")     # 'gnimmargorP' REVERSE!
print(f"s[5:0:-1] = {s[5:0:-1]}")   # 'margorp' (reverse 5 to 1)

# ============================================================================
# PART C: STRING METHODS - CASE CONVERSION
# ============================================================================

print("\n" + "=" * 70)
print("PART C: STRING METHODS - CASE CONVERSION")
print("=" * 70)

s = "Hello World"
print(f"Original: {s}")

print(f"\ns.upper()      = {s.upper()}")           # "HELLO WORLD"
print(f"s.lower()      = {s.lower()}")           # "hello world"
print(f"s.title()      = {s.title()}")           # "Hello World"
print(f"s.capitalize() = {s.capitalize()}")      # "Hello world"
print(f"s.swapcase()   = {s.swapcase()}")        # "hELLO wORLD"

# ============================================================================
# PART D: STRING METHODS - SEARCHING (O(n) or O(n*m))
# ============================================================================

print("\n" + "=" * 70)
print("PART D: SEARCHING METHODS")
print("=" * 70)

s = "hello world"
print(f"String: {s}")

print(f"\ns.find('o')          = {s.find('o')}")        # 4 (first)
print(f"s.rfind('o')         = {s.rfind('o')}")        # 7 (last)
print(f"s.index('o')         = {s.index('o')}")        # 4 (like find)
print(f"s.count('l')         = {s.count('l')}")        # 3
print(f"s.count('o')         = {s.count('o')}")        # 2
print(f"s.startswith('hello')= {s.startswith('hello')}")  # True
print(f"s.endswith('world')  = {s.endswith('world')}")    # True
print(f"'o' in s             = {'o' in s}")            # True
print(f"'x' in s             = {'x' in s}")            # False

# ============================================================================
# PART E: STRING METHODS - SPLITTING & JOINING
# ============================================================================

print("\n" + "=" * 70)
print("PART E: SPLITTING & JOINING")
print("=" * 70)

s = "hello world python"
print(f"String: {s}\n")

print("--- SPLIT ---")
print(f"s.split()     = {s.split()}")          # Split by whitespace
print(f"s.split(' ')  = {s.split(' ')}")       # Split by space
print(f"s.split('o')  = {s.split('o')}")       # Split by 'o'

print("\n--- JOIN ---")
words = ['apple', 'banana', 'cherry']
print(f"Words: {words}")
print(f"' '.join(words)  = {' '.join(words)}")      # "apple banana cherry"
print(f"','.join(words)  = {','.join(words)}")      # "apple,banana,cherry"
print(f"'-'.join('abc')  = {'-'.join('abc')}")      # "a-b-c"

# ============================================================================
# PART F: STRING METHODS - REPLACING
# ============================================================================

print("\n" + "=" * 70)
print("PART F: REPLACING")
print("=" * 70)

s = "hello world"
print(f"Original: {s}")

print(f"\ns.replace('o', '0')     = {s.replace('o', '0')}")       # All
print(f"s.replace('o', '0', 1)  = {s.replace('o', '0', 1)}")     # First only
print(f"s.replace('hello', 'hi') = {s.replace('hello', 'hi')}")  # 'hi world'

# ============================================================================
# PART G: STRING METHODS - STRIPPING & PADDING
# ============================================================================

print("\n" + "=" * 70)
print("PART G: STRIPPING & PADDING")
print("=" * 70)

s = "  hello  "
print(f"Original (with spaces): '{s}'")
print(f"s.strip()   = '{s.strip()}'")          # "hello"
print(f"s.lstrip()  = '{s.lstrip()}'")         # "hello  "
print(f"s.rstrip()  = '{s.rstrip()}'")         # "  hello"

print("\n--- Padding ---")
s = "5"
print(f"s.zfill(3)           = '{s.zfill(3)}'")          # "005"
print(f"s.ljust(5, '-')       = '{s.ljust(5, '-')}'")     # "5----"
print(f"s.rjust(5, '-')       = '{s.rjust(5, '-')}'")     # "----5"
print(f"s.center(7, '-')      = '{s.center(7, '-')}'")    # "--5----"

# ============================================================================
# PART H: CHARACTER CHECKING
# ============================================================================

print("\n" + "=" * 70)
print("PART H: CHARACTER CHECKING")
print("=" * 70)

print(f"'123'.isdigit()     = {'123'.isdigit()}")          # True
print(f"'abc'.isalpha()     = {'abc'.isalpha()}")          # True
print(f"'abc123'.isalnum()  = {'abc123'.isalnum()}")       # True
print(f"'   '.isspace()     = {'   '.isspace()}")          # True
print(f"'Hello'.isupper()   = {'Hello'.isupper()}")        # False
print(f"'HELLO'.isupper()   = {'HELLO'.isupper()}")        # True
print(f"'hello'.islower()   = {'hello'.islower()}")        # True

# ============================================================================
# PART I: CHARACTER OPERATIONS (ASCII)
# ============================================================================

print("\n" + "=" * 70)
print("PART I: CHARACTER OPERATIONS (ASCII)")
print("=" * 70)

print(f"ord('A')  = {ord('A')}")      # 65
print(f"ord('a')  = {ord('a')}")      # 97
print(f"ord('0')  = {ord('0')}")      # 48
print(f"chr(65)   = {chr(65)}")       # 'A'
print(f"chr(97)   = {chr(97)}")       # 'a'
print(f"chr(48)   = {chr(48)}")       # '0'

# ============================================================================
# PART J: STRING FORMATTING
# ============================================================================

print("\n" + "=" * 70)
print("PART J: STRING FORMATTING")
print("=" * 70)

name = "Alice"
age = 25
score = 95.5

print("\n--- F-strings (Modern) ---")
print(f"{name} is {age}")                          # "Alice is 25"
print(f"{name.upper()} scored {score:.1f}")        # "ALICE scored 95.5"
print(f"Score: {score:.2f}%")                      # "Score: 95.50%"

print("\n--- Format method ---")
print("{} is {}".format(name, age))                # "Alice is 25"
print("{1} {0}".format(name, age))                 # "25 Alice"

# ============================================================================
# PART K: INTERVIEW PATTERNS
# ============================================================================

print("\n" + "=" * 70)
print("PART K: INTERVIEW PATTERNS")
print("=" * 70)

# PATTERN 1: CHARACTER FREQUENCY
print("\n--- Pattern 1: Character Frequency (O(n)) ---")
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

result = char_frequency("aabbcc")
print(f"char_frequency('aabbcc') = {result}")

# PATTERN 2: PALINDROME CHECK (Two Pointers, O(n))
print("\n--- Pattern 2: Palindrome Detection (O(n)) ---")
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(f"is_palindrome('racecar')    = {is_palindrome('racecar')}")
print(f"is_palindrome('hello')      = {is_palindrome('hello')}")
print(f"is_palindrome('A man a plan a canal Panama') = {is_palindrome('A man a plan a canal Panama')}")

# PATTERN 3: REVERSE WORDS (O(n))
print("\n--- Pattern 3: Reverse Words (O(n)) ---")
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(f"reverse_words('hello world python') = '{reverse_words('hello world python')}'")

# PATTERN 4: ANAGRAM CHECK (O(n log n))
print("\n--- Pattern 4: Anagram Check (O(n log n)) ---")
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

print(f"are_anagrams('listen', 'silent') = {are_anagrams('listen', 'silent')}")
print(f"are_anagrams('hello', 'world')   = {are_anagrams('hello', 'world')}")

# ============================================================================
# PART L: STRING VS LIST CONVERSION
# ============================================================================

print("\n" + "=" * 70)
print("PART L: STRING VS LIST CONVERSION")
print("=" * 70)

s = "hello"
print(f"Original string: {s}")

# Convert to list
s_list = list(s)
print(f"As list: {s_list}")

# Modify
s_list[0] = 'x'
s_list[2] = 'z'
print(f"After modifications: {s_list}")

# Convert back
s_modified = ''.join(s_list)
print(f"Back to string: {s_modified}")

# ============================================================================
# PART M: COMPLEXITY WARNING
# ============================================================================

print("\n" + "=" * 70)
print("PART M: STRING CONCATENATION COMPLEXITY WARNING")
print("=" * 70)

print("\n❌ BAD (O(n²)) - Never do this:")
print("""
result = ""
for char in "hello":
    result += char  # Creates new string each time!
""")

print("✅ GOOD (O(n)) - Do this instead:")
print("""
result = ''.join(list("hello"))
""")

# Show the actual difference
import time

s = "a" * 1000

# Bad way (commented to not slow down output)
# start = time.time()
# result = ""
# for char in s:
#     result += char
# print(f"Concatenation method: {time.time() - start:.4f}s")

# Good way
start = time.time()
result = ''.join(list(s))
print(f"Join method: {time.time() - start:.6f}s (much faster)")

print("\n" + "=" * 70)
print("End of Strings Implementation")
print("=" * 70)