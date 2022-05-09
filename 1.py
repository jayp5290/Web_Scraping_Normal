phrase = input("Type in: ")
phrase_splitted = phrase.split(' ')

word_list = []
for i in phrase_splitted:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))

