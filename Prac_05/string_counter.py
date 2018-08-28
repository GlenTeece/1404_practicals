word_to_count = {}
text = input("Please enter the desired string: ")
word_list = text.strip().split(" ")
largest_word = 0
for word in word_list:
    largest_word = max(largest_word, len(word))
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
print("Text: {}".format(text))
for key,item in sorted(word_to_count.items()):
    print("{:{}} : {}".format(key,largest_word,item))