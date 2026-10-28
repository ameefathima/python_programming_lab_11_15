# 1. Character Replacement

text = input("Enter a string for character replacement: ")
old = input("Enter the character to be replaced: ")
new = input("Enter the new character: ")

text = text.replace(old, new)
print("After replacement:", text)


# 2. String Reversal

print("Reversed string:", text[::-1])


# 3. Palindrome

text = input("\nEnter a string for palindrome checking: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 4. Character Frequency

text = input("\nEnter a string for character frequency: ")
ch = input("Enter the character to count: ")

print("Character frequency:", text.count(ch))


# 5. Word Frequency

sentence = input("\nEnter a sentence for word frequency: ")
word = input("Enter the word to count: ")

words = sentence.split()

print("Word frequency:", words.count(word))