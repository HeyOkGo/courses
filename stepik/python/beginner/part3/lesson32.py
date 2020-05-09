d = int(input())
dictionary = []
full_text = []
errors = []
for words in range(d):
    words = str(input().lower())
    dictionary += [words]
l = int(input())
for text in range(l):
    text = [str(i) for i in input().lower().split()]
    full_text += text
for check in full_text:
    if check not in dictionary:
        errors += [check]
errors_to_print = set(errors)
print(*errors_to_print, sep='\n')