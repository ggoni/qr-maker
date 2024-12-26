import qrcode
import sys

def create_qr(url: str) -> None:
    """
    Creates a QR code image from a given URL and saves it as 'output.png'
    
    Args:
        url (str): The URL to encode in the QR code
    """
    qr_code_img = qrcode.make(url)
    with open("output.png", "wb") as f:
        qr_code_img.save(f)

def main():
    """
    Main function that handles command line arguments and calls create_qr
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    create_qr(url)
    print(f"QR code has been created as 'output.png'")

if __name__ == "__main__":
    main()