#create a QR code generator for online payment
import qrcode
from PIL import Image
#taking upi id as  input
upi_id=input("Enter your UPI id=")
#payment url = upi://pay?pa=UPI_ID&apn=Name&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment url based on the upi id 
phonepe_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each paytm app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#to save the images in file
phonepe_qr.save("phonepe_png")
paytm_qr.save("phonepe_png")
google_pay_qr.save("phonepe_png")

#display qr codes
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")