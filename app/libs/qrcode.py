from io import BytesIO
from base64 import b64encode

import qrcode


def qrcode_base64img(data):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()

    buf = BytesIO()
    img.save(buf)
    img_data = buf.getvalue()
    encoded_img = b64encode(img_data)
    return encoded_img