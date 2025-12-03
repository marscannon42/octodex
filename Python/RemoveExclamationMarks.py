# Write function RemoveExclamationMarks 
# which removes all exclamation marks from a given string

#solution 1:
def remove_exclamation_marks(s):
    no_exclam = s.replace("!", "")
    return no_exclam

#solution 2:
def remove_exclamation_marks(s):
    return s.replace("!", "")

word = "Hello World!"
replace_exclam = remove_exclamation_marks(word)
print(replace_exclam)