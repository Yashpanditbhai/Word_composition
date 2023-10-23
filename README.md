# Word_composition
This Python program does two things: first, it looks for the longest compounded word, which is a word made by putting together smaller words from a list. Second, it finds the second longest compounded word. The program asks the user to choose between two input files, "Input_01.txt" or "Input_02.txt," which contain the list of words to work with.
# How can we run it
**Logical approach :** I have provided you a python code in main.py file just simply copy and then paste in your own IDE, same copy input files and paste in inputs.
# Approach 
Read a list of words from an input file and store them.
Sort the words in descending order of length to check longer words first.
Define a function check_compound to determine if a word can be made by combining shorter words. It does this by checking if a word is in the word list or if it can be split into two smaller words.
Find the longest compound word by iterating through the sorted list of words, removing each word from the list, and checking if it can be made from shorter words using check_compound.
Remove the longest compound word from the list and find the second longest compound word.
Print the results:
The longest compound word.
Word Composition Problem Solved 
