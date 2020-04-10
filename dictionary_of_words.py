"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict({
    "okapi": "hooved mammal, lives in the DRC in Africa, relative of the giraffe",
    "Baird's tapir": "hooved mammal, lives in central and south america, related to horses and rhinos"
})

# print(word_definitions)

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["yellow-backed duiker"] = "hooved mammal, lives in eastern Africa, type of anelope"

word_definitions["bongo"] = "hooved mammal lives in Kenya, Uganda, and the DRC, type of antelope"

# print(word_definitions)

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

# print(word_definitions["okapi"])
# print(word_definitions["bongo"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for key in word_definitions:
    print(f"The definition of {key} is {word_definitions[key]}")