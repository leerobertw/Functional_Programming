def read_latin():
    with open("lorem ipsum.txt") as file:
        return file.read()


vowels = ('a', 'e', 'i', 'o', 'u')


def translate_word(word):
    if word[0] in vowels:
        if word.isalpha():
            return word + "yay"
        else:
            return word[0:-1] + "yay" + word[-1]
    for i in range(len(word)):
        if word[i] in vowels:
            if word.isalpha():
                return word[i:] + word[:i] + "ay"
            else:
                return word[i:-1] + word[:i] + "ay" + word[-1]
    if word.isalpha():
        return word + "ay"
    else:
        return word[0:-1] + "ay" + word[-1]


def main():
    data = read_latin()
    data = data.split(" ")
    data = list(map(str.lower, data))
    translated = map(translate_word, data)
    pig_latin_latin = " ".join(translated)
    print(pig_latin_latin)


main()
