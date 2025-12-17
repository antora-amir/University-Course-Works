sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = {}

for word in words:
    word = word.lower()         
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
