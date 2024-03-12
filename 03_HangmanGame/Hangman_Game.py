# Hangman Game: There will be a random word chosen from the list. User has to guess the word letter by letter to win the game.
# Concepts Utilized: for & while loops, if-else statements, lists, strings, range(), random module

# create a list of words related to python programming language
word_list = ["python", "hangman", "game", "programming", "computer", "science", "algorithm", "variable", "function", "loop", 
             "condition", "string", "integer", "list", "dictionary", "tuple", "set", "class", "object", "method", 
             "inheritance", "polymorphism", "encapsulation", "abstraction", "module", "package", "library", "import", 
             "export", "file", "input", "output", "exception", "try", "except", "finally", "raise", "assert", "debug", 
             "error", "syntax", "semantic", "interpreter", "compiler", "runtime", "memory", "variable", "assignment", 
             "expression", "iteration", "recursion", "stack", "queue", "tree", "graph", "binary", "search", "sorting", 
             "merge", "quick", "bubble", "insertion", "selection", "linear", "binary", "hash", "map", "set", "union", 
             "intersection", "difference", "complement", "concatenation", "substring", "slice", "reverse"]


# import random module to randomly choose the word and create relevant variables
import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# displaying the blank spaces for the characters in the word
display = []

for _ in range(word_length):
    display += "_"

# game should not end unless all the letters are correctly placed
end_of_game = False

# let the user guessing
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # check if the letter the used guessed by the user is one of the letters in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]

        # print the guessed letter in right place, and display the remaining blanks
        if letter == guess:
            display[position] = letter
    
    print(display)

    # check if any blank place remains
    if "_" not in display:
        end_of_game = True
        print("You Win!")







        