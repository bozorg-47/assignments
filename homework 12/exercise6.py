def is_vowel(single):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if single in vowel:
        return True
    else:
        return False
print('is "a" a vowel?', is_vowel("a"))
print('is "b" a vowel?', is_vowel("b"))
print('is "E" a vowel?', is_vowel("E"))
print('is "Z" a vowel?', is_vowel("Z"))