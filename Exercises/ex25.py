def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = word.pop(0)
    print(word)

def pritn_last_word(words):
    """Prints the last word after pooping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    pritn_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    pritn_last_word(words)

# 1- True
# 2- True
# 3- False
# 4- True
# 5- True
# 6- True
# 7- False
# 8- True
# 9- True
# 10- False
# 11- True
# 12- False
# 13- False
# 14- False
# 15- False
# 16- False
# 17- False
# 18- True
# 19- False
# 20- True