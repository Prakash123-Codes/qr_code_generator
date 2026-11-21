import qrcode

data = input("Enter the URL Of Your Website:").strip()        #strip is used to remove any white spaces in the website
filename = input("Enter the name of the file to save the QR Code: ").strip()
qr = qrcode.QRCode(box_size=10, border=5)        #box_size is used to set the size of the QR Code and border is used to set the border of the QR Code
qr.add_data(data)        #add_data is used to add the data to the QR Code
image = qr.make_image(fill_color="black", back_color="white")        #make_image is used to create the QR Code image
image.save(filename) #save is used to save the QR Code image
print("QR Code Generated Successfully!")