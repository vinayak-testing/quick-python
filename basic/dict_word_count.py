sample_string = "To be or not to be"
occurrence = {}
for word in sample_string.split():
    occurrence[word] = occurrence.get(word, 0) + 1

for word in occurrence:
    print("The word", word, "occurs", occurrence[word], "times in the sentence")

