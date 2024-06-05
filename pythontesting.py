import requests

r = requests.get('https://www.musicgoround.com/products/GUEL/electric-guitars')
print(r.content)