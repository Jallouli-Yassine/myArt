import re, os

path = r'd:\mm\myArt\myArt\settings.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Whitenoise Middleware
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in text:
    text = text.replace(
        "'django.middleware.security.SecurityMiddleware',", 
        "'django.middleware.security.SecurityMiddleware',\n    'whitenoise.middleware.WhiteNoiseMiddleware',"
    )

# Static and Cloudinary
cloudinary_settings = '''
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary configurations 
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
'''
text += cloudinary_settings

# Database modification
db_setting = '''DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )
}'''
if 'default' in text and 'dj_database_url' not in text:
    text = re.sub(r'DATABASES = \{.*?\n}', db_setting, text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
