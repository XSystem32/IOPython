
import requests
r = requests.get('https://api.github.com/orgs/python-elective-fall-2019/repos')

with open('requests.txt','r') as fr:
    #fr.write(r.text)
    print(fr.read())
