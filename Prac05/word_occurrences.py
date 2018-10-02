
all_words = {}
user_text = input("Text: ")
words = user_text.split()
for word in words:
    frequency = all_words.get(word, 0)
    all_words[word] = frequency + 1

words = list(all_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, all_words[word]))