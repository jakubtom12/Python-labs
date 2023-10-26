words_list = ['blabla']

with open("Lab1\zad3txt.txt", 'r') as text_file:
    new_text = text_file.read()

for word in words_list:
    new_text = new_text.replace(word, "")

text_file.close()

print(new_text)