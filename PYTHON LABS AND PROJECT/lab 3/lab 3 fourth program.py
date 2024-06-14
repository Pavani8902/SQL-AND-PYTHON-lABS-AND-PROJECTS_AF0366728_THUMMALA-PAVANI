def count_and_display_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    vowel_list = []

    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)

    print("Vowels in the given text:", vowel_list)
    print("Total number of vowels:", vowel_count)

# Given text
String = "Welcome to python Training"

# Count and display vowels in the given text
count_and_display_vowels(String)
