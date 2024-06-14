def count_word_occurrences(sentence):
    # Split the sentence into words and convert them to lowercase
    words = sentence.lower().split()
    
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

# Take input from the user
sentence = input("Enter a sentence: ")

# Count occurrences of each word in the given sentence
word_occurrences = count_word_occurrences(sentence)

# Print the results
for word, count in word_occurrences.items():
    print(f"'{word}' occurs {count} time(s) in the sentence.")
