import json
path = r'd:\mm\myArt\vercel.json'
data = {
    "version": 2,
    "builds": [
        {
            "src": "myArt/wsgi.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "myArt/wsgi.py"
        }
    ]
}
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(data, f, indent=4)
