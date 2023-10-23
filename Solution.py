def check_compound(w, word_set):                  # w is a word
    if w in word_set:
        return True
    for i in range(1, len(w)):
        prefix = w[:i]
        suffix = w[i:]
        if prefix in word_set and check_compound(suffix, word_set):
            return True
    return False

def find_longest_compound_words(word_list):
    word_set = set(word_list)
    word_list.sort(key=lambda x: (-len(x), x))

    for w in word_list:
        word_set.remove(w)
        if check_compound(w, word_set):
            return w

# Reading word list from a input text file
with open("Input_01.txt", "r") as file:  # Change the input file according to test cases 
    word_list = [line.strip() for line in file]

# Here, Finding the longest compound word
longest_compound_word = find_longest_compound_words(word_list)

# Remove the longest compound word and find the second longest compound word
word_list.remove(longest_compound_word)
second_longest_compound_word = find_longest_compound_words(word_list)

# Print the results
print("1. Longest Compound Word:", longest_compound_word)
print("2. Second Longest Compound Word:", second_longest_compound_word)

