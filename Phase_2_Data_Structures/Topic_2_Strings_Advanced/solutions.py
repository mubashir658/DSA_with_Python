"""
Topic 2: Strings (Advanced) - SOLUTIONS
Only look at this AFTER trying the exercises yourself!
"""

print("=" * 70)
print("EXERCISE 1: String Basics & Slicing - SOLUTIONS")
print("=" * 70)

s = "programming"
print(f"String: '{s}'\n")

# a) s[0]
print("a) s[0]")
print(f"   Answer: {s[0]}")
print(f"   Explanation: First character")

# b) s[-1]
print("\nb) s[-1]")
print(f"   Answer: {s[-1]}")
print(f"   Explanation: Last character")

# c) s[1:6]
print("\nc) s[1:6]")
print(f"   Answer: {s[1:6]}")
print(f"   Explanation: Characters from index 1 to 5 (stop is exclusive)")

# d) s[::2]
print("\nd) s[::2]")
print(f"   Answer: {s[::2]}")
print(f"   Explanation: Every 2nd character (indices 0, 2, 4, 6, 8, 10)")

# e) s[::-1]
print("\ne) s[::-1]")
print(f"   Answer: {s[::-1]}")
print(f"   Explanation: Reverse the string")

# f) len(s)
print("\nf) len(s)")
print(f"   Answer: {len(s)}")
print(f"   Explanation: Length of string")

print("\n" + "=" * 70)
print("EXERCISE 2: String Methods - SOLUTIONS")
print("=" * 70)

s = "Hello World"
print(f"String: '{s}'\n")

# a) s.lower()
print("a) s.lower()")
print(f"   Answer: '{s.lower()}'")

# b) s.upper()
print("\nb) s.upper()")
print(f"   Answer: '{s.upper()}'")

# c) s.find('o')
print("\nc) s.find('o')")
print(f"   Answer: {s.find('o')}")
print(f"   Explanation: First occurrence of 'o' is at index 4")

# d) s.count('l')
print("\nd) s.count('l')")
print(f"   Answer: {s.count('l')}")
print(f"   Explanation: 'l' appears 3 times (in 'Hello' and 'World')")

# e) s.replace('o', '0')
print("\ne) s.replace('o', '0')")
print(f"   Answer: '{s.replace('o', '0')}'")
print(f"   Explanation: Replace all lowercase 'o' with '0'")

# f) s.split()
print("\nf) s.split()")
print(f"   Answer: {s.split()}")
print(f"   Explanation: Split by whitespace into list of words")

print("\n" + "=" * 70)
print("EXERCISE 3: Character Counting - SOLUTION")
print("=" * 70)

def char_frequency(s):
    """Count frequency of each character in string."""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print("""
Solution:
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

How it works:
1. Create empty dictionary
2. Iterate through each character
3. Use .get(char, 0) to get current count (0 if not exists)
4. Increment count by 1
5. Return frequency dictionary

Time Complexity: O(n) - single pass through string
Space Complexity: O(k) - k = number of unique characters
""")

print("Test Results:")
print(f"char_frequency('aabbcc') = {char_frequency('aabbcc')}")
print(f"char_frequency('hello') = {char_frequency('hello')}")
print(f"char_frequency('aaa') = {char_frequency('aaa')}")
print(f"char_frequency('hello world') = {char_frequency('hello world')}")

print("\n" + "=" * 70)
print("EXERCISE 4: Palindrome Check - SOLUTION")
print("=" * 70)

def is_palindrome(s):
    """Check if string is palindrome (ignore spaces and case)."""
    # Normalize: remove spaces and convert to lowercase
    s = s.lower().replace(" ", "")
    
    # Two pointer approach
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print("""
Solution (Two-Pointer Approach):
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

How it works:
1. Remove spaces and convert to lowercase
2. Use two pointers from start and end
3. Compare characters moving inward
4. If any mismatch, return False
5. If all match, return True

Time Complexity: O(n)
Space Complexity: O(n) for normalized string

Alternative Solution (Simpler but less efficient):
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
""")

print("Test Results:")
print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
print(f"is_palindrome('hello') = {is_palindrome('hello')}")
print(f"is_palindrome('A man a plan a canal Panama') = {is_palindrome('A man a plan a canal Panama')}")
print(f"is_palindrome('Madam') = {is_palindrome('Madam')}")
print(f"is_palindrome('race car') = {is_palindrome('race car')}")

print("\n" + "=" * 70)
print("EXERCISE 5: Reverse Words - SOLUTION")
print("=" * 70)

def reverse_words(s):
    """Reverse the order of words in a string."""
    words = s.split()        # Split into words
    words = words[::-1]      # Reverse the list
    return ' '.join(words)   # Join back with spaces

print("""
Solution:
def reverse_words(s):
    words = s.split()         # Split into words
    words = words[::-1]       # Reverse the list
    return ' '.join(words)    # Join with spaces

One-liner:
def reverse_words(s):
    return ' '.join(s.split()[::-1])

How it works:
1. s.split() → Splits string into list of words
2. [::-1] → Reverses the list
3. ' '.join() → Joins words back with space separator

Time Complexity: O(n)
Space Complexity: O(n)

Example: "hello world python"
1. split() → ['hello', 'world', 'python']
2. [::-1] → ['python', 'world', 'hello']
3. join() → "python world hello"
""")

print("Test Results:")
print(f"reverse_words('hello world python') = '{reverse_words('hello world python')}'")
print(f"reverse_words('one two') = '{reverse_words('one two')}'")
print(f"reverse_words('a b c d') = '{reverse_words('a b c d')}'")
print(f"reverse_words('single') = '{reverse_words('single')}'")

print("\n" + "=" * 70)
print("All solutions completed!")
print("=" * 70)