import re

words_list = ['blabla']

with open("Lab1\zad3txt.txt", 'r') as text_file:
    new_text = text_file.read()

word_pattern = r'\b(?:' + '|'.join(map(re.escape, words_list)) + r')\b'

new_text = re.sub(word_pattern, '', new_text)

print(new_text)