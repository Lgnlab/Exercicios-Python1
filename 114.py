from urllib.request import urlopen
from urllib.error import URLError

try:
    urlopen("https://www.google.com")
    print('URL acessível!')
except URLError:
    print('Não foi possível acessar')
