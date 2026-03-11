import re
path = r'd:\mm\myArt\build_files.sh'
with open(path, 'r') as f:
    text = f.read()

# Update the build_files to bypass the PEP 668 managed environment block on Vercel
text = text.replace('pip install -r requirements.txt', 'python3 -m pip install -r requirements.txt --break-system-packages')

with open(path, 'w') as f:
    f.write(text)
