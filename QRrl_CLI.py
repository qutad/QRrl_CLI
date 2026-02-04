import qrcode
import os
import re
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

def is_valid_url(url):
    """Checks if the string follows a standard URL format."""
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$"
    return bool(re.match(pattern, url))

def get_rounding_ratio():
    """Handles the user input for the QR module rounding."""
    while True:
        choice = input("\nCustomize QR?\n 1 - Set rounding ratio\n 2 - Done (default)\n: ").strip().lower()
        
        if choice in ['q', 'quit']:
            exit()
        elif choice == '2':
            return 0.0
        elif choice == '1':
            try:
                ratio = float(input("\nEnter rounding ratio (0.0 - 1.0): "))
                if 0.0 <= ratio <= 1.0:
                    return ratio
                print("\n!!!Please enter a value between 0.0 and 1.0!!!")
            except ValueError:
                print("\n!!!Error: Please enter a valid number!!!")
        else:
            print("\n!!!Invalid option, try again!!!")

def generate_qr(data, rounding_ratio):
    """Handles the QR generation logic."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    
    return qr.make_image(
        back_color="white",
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(radius_ratio=rounding_ratio)
    )

def main():
    user_url = input("\nEnter the URL (or 'q' or 'quit' to quit): ").strip()
    
    if user_url.lower() in ['q', 'quit']:
        return

    if not is_valid_url(user_url):
        print("\n!!!Invalid URL format. Use 'http://' or 'https://' !!! \n")
        return

    rounding_ratio = get_rounding_ratio()
    
    # Process and Save
    img = generate_qr(user_url, rounding_ratio)
    file_name = "qrcode.png"
    img.save(file_name)
    
    print(f"\nSuccess! QR code saved to: {os.path.join(os.getcwd(), file_name)}\n")

if __name__ == "__main__":
    main()