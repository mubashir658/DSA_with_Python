"""
Topic 2: Strings (Advanced) - Exercises
Try solving these WITHOUT looking at solutions first!
"""

print("=" * 70)
print("EXERCISE 1: String Basics & Slicing")
print("=" * 70)

s = "programming"
print(f"String: '{s}'\n")

print("What do these return?")
print("a) s[0]")
print("b) s[-1]")
print("c) s[1:6]")
print("d) s[::2]")
print("e) s[::-1]")
print("f) len(s)")

print("\n" + "=" * 70)
print("EXERCISE 2: String Methods")
print("=" * 70)

s = "Hello World"
print(f"String: '{s}'\n")

print("What do these return? (Predict the output)")
print("a) s.lower()")
print("b) s.upper()")
print("c) s.find('o')")
print("d) s.count('l')")
print("e) s.replace('o', '0')")
print("f) s.split()")

print("\n" + "=" * 70)
print("EXERCISE 3: Character Counting")
print("=" * 70)

print("""
Given a string, count frequency of each character.
Input: "aabbcc"
Output: {'a': 2, 'b': 2, 'c': 2}

Write a function char_frequency(s) that:
1. Takes a string as input
2. Returns a dictionary with character frequencies
3. Time complexity should be O(n)
4. Space complexity should be O(k) where k = unique characters

def char_frequency(s):
    # Your code here
    pass

# Test
print(char_frequency("aabbcc"))
print(char_frequency("hello"))
print(char_frequency("aaa"))
""")

print("\n" + "=" * 70)
print("EXERCISE 4: Palindrome Check (CLASSIC!)")
print("=" * 70)

print("""
A palindrome reads the same forwards and backwards.
"racecar" → YES
"hello" → NO
"A man a plan a canal Panama" → YES (ignore spaces and case)

Write a function is_palindrome(s) that:
1. Takes a string as input
2. Ignores spaces and case
3. Returns True if palindrome, False otherwise
4. Time complexity should be O(n)

def is_palindrome(s):
    # Your code here
    pass

# Test
print(is_palindrome("racecar"))      # True
print(is_palindrome("hello"))        # False
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Madam"))        # True
""")

print("\n" + "=" * 70)
print("EXERCISE 5: Reverse Words")
print("=" * 70)

print("""
Given: "hello world python"
Reverse the order of words
Output: "python world hello"

Write a function reverse_words(s) that:
1. Takes a string as input
2. Reverses the order of words (not characters!)
3. Returns the reversed string
4. Time complexity should be O(n)

def reverse_words(s):
    # Your code here
    pass

# Test
print(reverse_words("hello world python"))  # "python world hello"
print(reverse_words("one two"))              # "two one"
print(reverse_words("a b c d"))              # "d c b a"
""")

print("\n" + "=" * 70)
print("Try to solve these WITHOUT looking at solutions!")
print("=" * 70)