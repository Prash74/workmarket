import docx2txt
import matplotlib.pyplot as plt
import re

fl = "Resume_doc.docx"
data = docx2txt.process(fl)
#print data
letters = "abcdefghijklmnopqrstuvwxyz"
letter_dict = {}
for i in letters:
    letter_dict[i] = 0
words = " ".join(re.findall("[a-zA-Z]+", data))
words_list = words.split(" ")
for i in words_list:
    for j in i:
        letter_dict[j.lower()] += 1

plt.bar(range(len(letter_dict)), letter_dict.values(), align='center')
plt.xticks(range(len(letter_dict)), letter_dict.keys())

plt.show()
