# Learn Python together
"""Given a string s consisting of words and spaces, 
return the length of the last word in the string."""

# Solution
def length_last_word(s):
    s_split = s.strip().split(" ")
    if s_split:
        return len(s_split[-1])
    return 0

# check
print(length_last_word("Easy Python")) # -> 6
print(length_last_word("   fly me   to   the moon  ")) # -> 4
print(length_last_word("    ")) # -> 0