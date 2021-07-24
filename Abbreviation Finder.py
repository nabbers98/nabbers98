import docx
import re

print('© RR Enterprise 2020 Product \nDeveloped by Arnab Talukder')

wanteddoc = input(
    'Please type in the file that you want. \nFor example D:\\Project\\Contract.docx \n Type in the file here:')

doc = docx.Document(wanteddoc)

allText = []
for docpara in doc.paragraphs:
    allText.append(docpara.text)

stringle = ''

for i in allText:
    stringle += ' ' + i

proper = " ".join(re.findall('\w+', stringle))
proper = str(proper)
word_list = proper.split()

abv_list = []
other_list = []


for i in word_list:
    if i == i.upper():
        abv_list.append(i)
    else:
        other_list.append(i)

final_list = set(abv_list)
final_list_string = str(final_list)
nova_list = final_list_string.split()

finale = ''

for i in range(0, len(nova_list)):
    finale += '\n' + str(nova_list[i])
pass

shesh = " ".join(re.findall('\w+' , finale))
shesh = " ".join(re.split('\d', shesh))

shesher_pore = shesh.split()
drachma = []

for i in shesher_pore:
    if len(i) > 1:
        drachma.append(i)
bon = ''

for i in range(0, len(drachma)):
    bon += '\n' + str(drachma[i])
pass

bon = bon.split()
drachma = sorted(bon)

f = open('All Abbreviations.txt', 'w+')

f.write('© RR Enterprise 2020 Product \nDeveloped by Arnab Talukder \n')
khatam = '© RR Enterprise 2020 Product'

for i in drachma:
    khatam = '\n' + i
    f.write(khatam)

f.close()
