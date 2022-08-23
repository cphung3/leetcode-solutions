def longest_word(words):
    word_dict = {}
    for word in words:
        word_dict[len(word)] = set()
        word_dict[len(word)].add(word)

    max_key = max(word_dict.keys())
    longest_words = [w for w in word_dict[max_key]]
    longest_words.sort()
    for longest in longest_words:
        for length in range(len(longest)):
            if longest[0:length] not in word_dict[length + 1]:
                break
        return longest
    return ""


wor = ["w","wo","wor","worl", "world"]
print(longest_words(wor))


