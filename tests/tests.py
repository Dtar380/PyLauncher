from urllib import request, error
from time import sleep as s

def getInternetConnection():
        try:
            request.urlopen('https://www.google.com', timeout=1)
            return True
        except error.URLError:
            return False

for i in range(100):
    if getInternetConnection():
        print('Internet Connection')
    else:
        print('Not Internet Connection')
    s(0.5)