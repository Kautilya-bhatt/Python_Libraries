import qrcode
data=input("Enter the text or URL to generate QR code: ")
qr = qrcode.make(data)
qr.save("qr_code.png")
print("QR code generated and saved as qr_code.png")
