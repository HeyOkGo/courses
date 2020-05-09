dictionary ={}
dictionary_2 = {}

string_1 = str(input())
cipher_string_1 = str(input())

for i in range(len(string_1)):
    dictionary[string_1[i]] = cipher_string_1[i]

for i in range(len(cipher_string_1)):
    dictionary[cipher_string_1[i]] = string_1[i]

to_code = ''

string_2 = str(input())
for w in string_2:
    if w in dictionary:
        to_code += dictionary[w]

to_uncode = ''

cipher_string_2 = str(input())
for u in cipher_string_2:
    if u in dictionary_2:
        to_uncode += dictionary_2[u]

print(to_code)
print(to_uncode)