# **** Love Calculator ****

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
#
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# 2. Then check for the number of times the letters in the word LOVE occurs.
#
# 3. Then combine these numbers to make a 2 digit number and print it out.
#
# e.g.
#
# name1 = "Angela Yu" name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53


def calculate_love_score(name1,name2):
    word1 = "TRUE"
    word2 = "LOVE"
    count1 = 0
    count2 = 0
    for letter in word1.casefold():
        for char in name1.casefold():
            if char == letter:
                count1+=1
        for char in name2.casefold():
            if char == letter:
                count1+=1

    for letter in word2.casefold():
        for char in name1.casefold():
            if char == letter:
                count2 += 1
        for char in name2.casefold():
            if char == letter:
                count2+=1

    print(f"{count1}{count2}")

calculate_love_score("Kanye West", "Kim Kardashian")