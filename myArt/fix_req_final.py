path = r'd:\mm\myArt\requirements.txt'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('mysqlclient==2.2.8', 'PyMySQL==1.1.1\ncryptography==42.0.5')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
