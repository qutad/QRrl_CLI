import qrcode 
import re 
import os 

url = input("Enter the URL: ").strip()
if url.lower() == "q" or url.lower() == "quit":
    exit()

# Function to validate URL format
def validate(url):
    url_patern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$"

    if re.match(url_patern, url):
        return True
    else:
        return False

if validate is False:
    print("Invalid URL format. Please enter a valid URL starting with http:// or https://")
    exit()

print("QR code was created in the directory: " + os.getcwd())

file_path = "qrcode.png"


qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)