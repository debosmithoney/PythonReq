str = input()
words = [word.lower() for word in str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word, end=" ")