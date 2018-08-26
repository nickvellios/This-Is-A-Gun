# Nick Vellios
# For decoding 'thisisagun.png' found on https://codeisfreespeech.com
# Requires both the Pillow and requests libraries
# License: Unlicense. For more information, please refer to http://unlicense.org/
from PIL import Image
import requests
url = 'https://codeisfreespeech.com/gun.png'
img = Image.open(requests.get(url, stream=True).raw)
w, h = img.size;
px = list(img.getdata())
with open('Liberator.zip', 'w') as f:
    [f.write('%c%c%c' % px[w * x + y])
    for x in range(w) for y in range(h)]

