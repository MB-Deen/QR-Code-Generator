import qrcode
img = qrcode.make('https://biryanikadai.com.au')
img.save('qrcode.png')