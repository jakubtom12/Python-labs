import re

dictionary = {
    "szkoda": "super",
    "reka": "noga",
    "samochod": "rower",
}

def replace_words(text, replacements):
    pattern = r'\b(' + '|'.join(re.escape(word) for word in replacements.keys()) + r')\b'
    def replace(match):
        return replacements[match.group(0)]
    return re.sub(pattern, replace, text)

with open("Lab1\zad4txt.txt", 'r') as text_file:
    text = text_file.read()

text_file.close()

new_text = replace_words(text, dictionary)

print(new_text)