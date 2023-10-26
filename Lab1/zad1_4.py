dictionary = {
    "szkoda": "super",
    "reka": "noga",
    "samochod": "rower",
}

def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text

with open("Lab1\zad4txt.txt", 'r') as text_file:
    text = text_file.read()

text_file.close()

new_text = replace_words(text, dictionary)

print(new_text)