# Reverse a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = [word[::-1] for word in words]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)

