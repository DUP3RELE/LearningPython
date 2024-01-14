import requests

url = 'https://api.pwnedpasswords.com/range/' + '5baa6'
res = requests.get(url)
print(res)