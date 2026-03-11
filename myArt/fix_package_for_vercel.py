import os

path = r'd:\mm\myArt\package.json'
# We create a dummy package.json to trick vercel's autodetection if it really requires it, 
# although vercel.json uilds array should have been enough. Let's make sure it has one.

import json
data = {
  "engines": {
    "node": "18.x"
  }
}
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
