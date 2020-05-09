n = int(input())
team = [[] for i in range(n)]
dictionary = {}
# full_text = []
# errors = []
dictionary['a'] = [0, 7, 2, 3, 0]
print(dictionary['a'][1])
for results in range(n):
    results = str(input()).split(';')
    
    print(results)
#     a = int(results[1])
#     b = int(results[2])
#     c = int(results[3])
#
# l = int(input())
# for text in range(l):
#     text = [str(i) for i in input().lower().split()]
#     full_text += text
# for check in full_text:
#     if check not in dictionary:
#         errors += [check]
# errors_to_print = set(errors)
# print(*errors_to_print, sep='\n')