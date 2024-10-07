import string

word = input("Enter a word ")


print("length of word: " + str(len(word)))
print("Uppercase: " + word.upper())
print("Lowercase: " + word.lower())

letter = input("Enter a letter: ")

print(letter + " appears " + str(word.count(letter)) + " in: " + word)

substring = input("Enter a substring: ")
print(substring + " appears " + str(word.count(substring)) + " in: " + word)

reversedString = word[::-1]
print("Reversed: " + reversedString)

startingIndex = input("Enter a starting index: ")
endingIndex = input("Enter an ending index: ")
# slicedWord = slice(startingIndex,endingIndex)
print(word[int(startingIndex):int(endingIndex)])

replaceChar = input("Enter a character to replace: ")
whatReplacement = input("Enter the replacement character: ")
newWord = word.replace(replaceChar, whatReplacement)
print(newWord)

secondWord = input("Enter a second word: ")
print("Concatenated: " + word + secondWord)

def isPalindrome(string):
 if(word == word[::-1]):
    return "The word is a palindrome"
 else:
    return "The word is not a palindrome."

print(isPalindrome(word))



if(word.isidentifier() == True):
    identifier = "Yes"
else: identifier = "No"


print("Is a valid python identifier: " + identifier)

