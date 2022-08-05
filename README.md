# share_io

-----

## Added Features
1. Signup
2. login
3. search
4. change password
5. like feature
6. upload images
7. read and edit blog
8. Markdown editor

## Upcoming Features
1. TinyMC WYSIWYG editor
2. Email forgot password

### To Generate Secret key run the below code
```
 from django.core.management.utils import get_random_secret_key
 print(get_random_secret_key())
 ```
1. copy the generated key
2. create `secrets.py` in share_io folder
3. paste the key as string with variable name 'SECRETE_KEY'

*Don't forget to initiate database inside secrets.py*