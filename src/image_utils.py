import cv2

def preprocess_image(image_path):
    """
    Preprocesses the image to enhance OCR accuracy.
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print(f"Failed to read image: {image_path}")
        return None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(blurred)
    is_success, buffer = cv2.imencode(".png", enhanced)
    if not is_success:
        print(f"Failed to encode image: {image_path}")
        return None
    return buffer.tobytes()
