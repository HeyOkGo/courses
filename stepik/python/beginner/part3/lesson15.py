import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/833.txt'
#params = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url)
text = r.text.splitlines()
count = 0
for line in text:
    count += 1
print(count) # count strings
print(len(r.text)) # count words or letters