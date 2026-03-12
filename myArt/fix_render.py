path = r'd:\mm\myArt\render_build.sh'
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write('#!/usr/bin/env bash\n')
    f.write('set -o errexit\n\n')
    f.write('python -m pip install --upgrade pip\n')
    f.write('pip install -r requirements.txt\n')
    f.write('python manage.py collectstatic --no-input\n')
    f.write('python manage.py migrate\n')
