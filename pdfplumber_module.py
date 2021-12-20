import pdfplumber
import re

txt = ""

with pdfplumber.open("./21_391_11.pdf") as pdf:
    for i in range(len(pdf.pages)):
        page = pdf.pages[i];
        l = page.crop((0, 0, 0.5 * float(page.width), float(page.height))).extract_text();
        r = page.crop((0.5 * float(page.width), 0.0, float(page.width), float(page.height))).extract_text();
        txt += str(l)
        txt += str(r)

present_congressman = []
flag = False
split_txt = txt.split('\n')
for sentence in split_txt:
    if flag == True:
        if sentence.find('◯') != -1:
            break
        splited_sentence = sentence.split('     ')
        short_name = ''
        for idx in range(len(splited_sentence)):
            if len(splited_sentence[idx]) > 10 and len(splited_sentence[idx].split('   ')) > 1:
                splited_sentence.append(splited_sentence[idx].split('   ')[1])
                splited_sentence[idx] = splited_sentence[idx].split('   ')[0]
        for name in splited_sentence:
            name = name.strip()
            if len(name) > 10:
                continue
            elif len(name) > 2:
                present_congressman.append(name)
            elif short_name == '':
                short_name += name
            else:
                short_name += name
                present_congressman.append(short_name)
                short_name = ''
    if sentence.find('출석 의원') != -1:
        flag = True

names = ""
for name in present_congressman:
    names += name.replace(" ", '') + '\n'

print(str(len(present_congressman)) + "명")

with open("./present_congressman.txt", "w", -1, 'utf-8') as file:
    file.write(names)
