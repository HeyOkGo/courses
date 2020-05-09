s = input()
i = 0
j = len(s) - 1
p = True
while i < j:
    if s[i] != s[j]:
        p = False
    i += 1
    j -= 1
if p:
    print('Yes')
else:
    print('No')