



def reverse_string(word):

    split = word.split('.')
    reverse = reversed(split)
    new_word = '.'.join(reverse)
    return new_word

print(reverse_string("hello.i.me"))
