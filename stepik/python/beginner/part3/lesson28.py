classes = [[] for i in range(11)]
with open('C:\\Users\\PAVILION\\Downloads\\dataset_3380_5.txt', 'r') as file:
    for line in file:
        classNumber = line.split('\t')[0]
        height = line.split('\t')[2]
        classes[int(classNumber) - 1].append(int(height))
print(classes)
for i in range(len(classes)):
    if len(classes[i]) == 0:
        print(str(i + 1) + ' -')
    else:
        print(str(i + 1) + ' ' + str(float(sum(classes[i])) / len(classes[i])))