import qrcode
import os
url = input('URL: ')
def generate():
    img = qrcode.make(url)
    type(img)
    img.save('qr.png')
    print('QR Generated.')

generate()