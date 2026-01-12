import pytesseract
from PIL import Image
import io


def extract_text(file) -> str:
    """
    Extract text from an uploaded image file using OCR.
    """

    try:
        # Read image bytes
        image_bytes = file.read()

        # Convert bytes to image
        image = Image.open(io.BytesIO(image_bytes))

        # Perform OCR
        text = pytesseract.image_to_string(image)

        return text.strip()

    except Exception as e:
        print("OCR Error:", e)
        return ""
