import re
from google.cloud import vision

def extract_text_from_image(client, image_bytes):
    """
    Extracts text from a given image using Google Cloud Vision OCR.
    """
    try:
        image = vision.Image(content=image_bytes)
        image_context = vision.ImageContext(language_hints=['zh-TW'])
        response = client.text_detection(image=image, image_context=image_context)
        texts = response.text_annotations

        if response.error.message:
            print(f"Error in OCR: {response.error.message}")
            return ""
        
        if texts:
            return texts[0].description.strip()
        else:
            return ""
    except Exception as e:
        print(f"Failed to extract text from image: {e}")
        return ""

def extract_all_numbers_in_parentheses(text):
    """
    Extracts all numbers found within parentheses in the text.
    """
    pattern = r'\((\d+)\)'
    return re.findall(pattern, text)
