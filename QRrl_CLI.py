import qrcode 
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
import re 
import os 


set_filcolor = "black"
set_roundfil = 0

url = input("Enter the URL: ").strip()

# function to validate URL format
def validate(url):
    url_patern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$"

    if re.match(url_patern, url):
        return True
    else:
        return False
if validate(url) is False:
    print("Invalid URL format. Please enter a valid URL starting with http:// or https://")
    exit()

if url.lower() == "q" or url.lower() == "quit":
    exit()

# customization
while True:
    cust = input("\nEnter what you want to customize.\n" 
                 "1 - round filling \n" 
                 "2 - done (by default) \n"
                 ": ").strip()
    
    if cust == '1':
        try:
            set_roundfil = float(input("Enter rounding ratio (0.0 - 1.0): "))
        except ValueError:
            print("\n ValleError: please enter a number")

    elif cust == '2':
        break
    elif cust.lower() in ["q", 'quit']:
        exit()
    else:
        print("\n Invalid option, try again.")




print("QR code was created in the directory: " + os.getcwd())
file_path = "qrcode.png"

# qrcode presets
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_M,
    box_size = 10,
    border = 4
)
qr.add_data(url)

img = qr.make_image(
    back_color = "white",
    image_factory = StyledPilImage,
    module_drawer = RoundedModuleDrawer(radius_ratio = set_roundfil)
                     )
img.save(file_path)