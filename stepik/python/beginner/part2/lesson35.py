s = str(input())
word = s[:1]
count = 1
result = ''
for x in s[1:]:
    if x != word:
        result += (word + str(count))
        word = x
        count = 1
    else:
        count += 1
result += (word + str(count))
print(result)