import pyqrcode  
import png  
from pyqrcode import QRCode  

url_string = "https://siska.binadarma.ac.id/"  

# Membuat QR code  
try:  
    qr_code = pyqrcode.create(url_string)  

    # Menyimpan QR code dalam format SVG  
    qr_code.svg("myqr.svg", scale=8)  

    # Menyimpan QR code dalam format PNG  
    qr_code.png("myqr.png", scale=6)  

    print("QR code berhasil dibuat!")  
except Exception as e:  
    print(f"Terjadi kesalahan: {e}")