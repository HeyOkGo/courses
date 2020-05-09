text = ''
with open('C:\\Users\\PAVILION\\Downloads\\dataset_3363_2.txt') as s:
    for line in s:
        line = line.strip()
        text += line
s.close()
print(text)
with open('C:\\Users\\PAVILION\\Downloads\\text.txt', 'w') as ouf:
    ouf.write(text)