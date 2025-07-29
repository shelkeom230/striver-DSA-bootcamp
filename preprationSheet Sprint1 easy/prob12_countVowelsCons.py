# count vowels and consonants in a string
def countVowelsCons(string):
    string = string.replace(" ", "")
    vowels, cons = 0, 0
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowels += 1
        else:
            cons += 1
    print(f"vowels: {vowels} consonants: {cons}")


# optimised way with corner cases handling
def countVowelsCons2(string):
    vowels,cons=0,0
    vowels_set={'a','e','i','o','u'}
    
    for char in string.lower():
        if char.isalpha():
            if char in vowels_set:
                vowels+=1
            else:
                cons+=1
    print(f'vowels: {vowels} consonants: {cons}')


string = input()
countVowelsCons2(string)
