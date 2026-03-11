path = r'd:\mm\myArt\myArt\settings.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

import_pymysql = '''import dj_database_url
import pymysql
pymysql.install_as_MySQLdb()
'''
text = text.replace('import dj_database_url', import_pymysql)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
