import qrcode
import os
def print_banner():
    banner = '''
  _   _ _______ ______ _____  __ ___  
 | \ | |__   __|  ____|  __ \/_ |__ \ 
 |  \| |  | |  | |__  | |__) || |  ) |
 | . ` |  | |  |  __| |  ___/ | | / / 
 | |\  |  | |  | |____| |     | |/ /_ 
 |_| \_|  |_|  |______|_|     |_|____|  
''' 
    print(banner)


def generate():
    img = qrcode.make(url)
    type(img)
    img.save('qr.png')
    print('QR Generated.')

print_banner()

url = input('QR Code Generator, please enter the URL: ')

generate()