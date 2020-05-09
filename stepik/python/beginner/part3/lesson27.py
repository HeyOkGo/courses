sum_a = 0
sum_b = 0
sum_c = 0
count = 0
ouf = open('C:\\Users\\PAVILION\\Downloads\\text.txt', 'w')
with open('C:\\Users\\PAVILION\\Downloads\\dataset_3363_4.txt', 'r') as s:
    for line in s:
        line = line.strip()
        line = line.split(';')
        a = int(line[1])
        b = int(line[2])
        c = int(line[3])
        sum_a += int(a)
        sum_b += int(b)
        sum_c += int(c)
        count += 1
        avr = float((a + b + c) / 3)
        print(avr)
        avr_str = str(avr)
        ouf.write(avr_str + '\n')
    avr_a = float(sum_a / count)
    avr_b = float(sum_b / count)
    avr_c = float(sum_c / count)
    print(avr_a, avr_b, avr_c)
    str_a = str(avr_a)
    str_b = str(avr_b)
    str_c = str(avr_c)
    sum_str = (str_a + ' ' + str_b + ' ' + str_c)
    ouf.write(sum_str)
s.close()