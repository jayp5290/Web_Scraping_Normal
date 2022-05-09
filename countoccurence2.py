def count_occurence(words, word_to_count):
    count = 0
    for word in words:
        if word == word_to_count:
            count = count + 1
    return count


words = ['hello', 'goodbye', 'howdy']
print(f'"hello" appears {count_occurence(words, "hello")} time(s)')
print(f'"howdy" appears {count_occurence(words, "howdy")} time(s)')

