import qrcode
from PIL import Image
import cv2

def generate_qr_code(data, filename="qrcode.png", box_size=10, border=4):
    """
    Generates a QR code from the provided data and saves it as an image.

    :param data: The data to encode in the QR code (string).
    :param filename: The filename to save the QR code image (string).
    :param box_size: The size of each box in the QR code grid (int).
    :param border: The thickness of the border (int).
    """
    # Create a QR Code object with specific configuration
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=box_size,  # Size of each box
        border=border,  # Thickness of the border
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")


if __name__ == "__main__":
    # Example data
    data_to_encode = "https://hackclub.com/arcade/recjveFymkceAsJK4/shop/"

    # Generate QR code
    generate_qr_code(data_to_encode, "myqr.png")
    cv2.imshow("myqr.png");
