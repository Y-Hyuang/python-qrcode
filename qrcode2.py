# -*- coding:utf-8 -*-
'''
Created on 2016-1-5

@author: Hyuang
'''

import qrcode

qr = qrcode.QRCode(
     version=3,
     error_correction=qrcode.constants.ERROR_CORRECT_L,
     box_size=10,
     border=4,             
                   )
qr.add_data('https://pypi.python.org/pypi/qrcode/5.1')
qr.make(fit=True)
img = qr.make_image()
img.save('123.png')
img.show('123.png')