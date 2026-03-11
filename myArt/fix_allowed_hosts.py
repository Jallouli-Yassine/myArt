path = r'd:\mm\myArt\myArt\settings.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(\"ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.pythonanywhere.com']\", \"ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*', '.onrender.com']\")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
