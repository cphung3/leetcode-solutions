

def reverse_string(word, idx):
    if idx == len(word):
        return ""
    char = word[idx]
    return reverse_string(word, idx+1) + char


print(reverse_string("hello", 0))
