# qr code stands for for quick  responce  code.It is a 2D pictographic code used 
# for its fast readabality ans large soorage capacity 

# The information can be any kind of  data 
# steps  to follow 
# install modules qr code  create  an object  of qr code  clss 

# add data in qr code 
import qrcode 
qr=qrcode.QRCode(
    version=15, 
    box_size=10 ,
    border=5,

)
data="venkatesh jayappa mariyappanver"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='back',back_color="white")
img.save("text.png")
