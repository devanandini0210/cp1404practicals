text = input("Text: ")
text = text.split()
count = []
width = 15
for i in range(len(text)):
    count.append(0)
text.sort()
words_to_occurrences = dict(zip(text, count))

for word in text:
    if word in words_to_occurrences:
        words_to_occurrences[word] += 1

for keys, value in words_to_occurrences.items():
    print(f"{keys:{width}} : {value}")
