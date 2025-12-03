# Complete the function that accepts a string parameter, 
# and reverses each word in the string. 
# All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(s):
    # 1. Split the string by a single space (' ').
    # This is crucial for preserving multiple spaces.
    words = s.split(' ')

    # 2. Initialize a list to hold the reversed words.
    reversed_words = []

    # 3. Iterate through the words list and reverse each word manually.
    for word in words:
        # String slicing [::-1] is the most efficient way to reverse a string
        reversed_word = word[::-1]
        
        # Append the reversed word (or empty string if it was a space separator)
        reversed_words.append(reversed_word)

    # 4. Join the list back using the single space (' ').
    # The empty strings are now filled with the single space separator,
    # correctly restoring the original spacing
    return ' '.join(reversed_words)

reverseLettersWords = reverse_words("This is an example!")
print(reverseLettersWords)