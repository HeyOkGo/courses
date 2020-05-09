import requests

with open('C:\\Users\\PAVILION\\Downloads\\dataset_3378_3.txt', 'r') as link:
    for path in link:
        path = path.strip()
        path = path.split('/')
        path = path[7]

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

r = requests.get(url + path)
path = r.text

while path[0:2] != 'We':
    z = requests.get(url + path)
    path = z.text
print(path)