#consonant values
def consonant_values(string):
    #define the vowels
    vowels = "aeiou"
    #define the consonants
    consonant_values = {char: i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
    max_consonant_value = 0
    current_consonant_value = 0

#for method to check whether the letters in the string are vowels or consonants
    for char in string:
        if char not in vowels:
            current_consonant_value += consonant_values[char]
        else:
            if current_consonant_value > max_consonant_value:
                max_consonant_value = current_consonant_value
            current_consonant_value = 0

    #Check the consonant substring in order to compare which of the substrings has the larger value
    #The substrings are the consonants between the vowels
    if current_consonant_value > max_consonant_value:
        max_consonant_value = current_consonant_value
#output the substring with the larger value 
    return max_consonant_value


print(consonant_values("zodiacs")) 


print(consonant_values("heisenberg"))
print(consonant_values("strength"))