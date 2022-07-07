pip install bcrypt
Collecting bcrypt
  Downloading bcrypt-3.2.2-cp36-abi3-win_amd64.whl (29 kB)
Collecting cffi>=1.1
  Downloading cffi-1.15.1-cp39-cp39-win_amd64.whl (179 kB)
     ---------------------------------------- 179.1/179.1 KB 10.6 MB/s eta 0:00:00
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     ---------------------------------------- 118.7/118.7 KB 6.8 MB/s eta 0:00:00
Installing collected packages: pycparser, cffi, bcrypt
Successfully installed bcrypt-3.2.2 cffi-1.15.1 pycparser-2.21
WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
You should consider upgrading via the 'C:\Users\mittp\AppData\Local\Programs\Python\Python39\python.exe -m pip install --upgrade pip' command.

C:\Users\mittp>python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import bcrypt
>>> password = b"abc123"
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
>>> hashed
b'$2b$12$S/eoUZtaiEY.YpGcbT4z3eh36bxUjk5dZmfdPpE1RuT33IassMgi6'
>>> pwd = bcrypt.checkpw(password, hashed)
>>> pwd
True
>>> if bcrypt.checkpw(password, hashed):
... print('password matched')
  File "<stdin>", line 2
    print('password matched')
    ^
IndentationError: expected an indented block
>>> if bcrypt.checkpw(password, hashed):
...    print('Password matched!')
... else:
...    print('wrong password')
...
Password matched!
>>>









