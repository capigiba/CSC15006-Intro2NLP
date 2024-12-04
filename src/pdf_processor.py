import os
import io
from PIL import Image
import fitz  # PyMuPDF
from src.image_utils import preprocess_image
from src.text_utils import extract_text_from_image
from src.file_handler import save_text_to_file

def process_single_image(image_path, texts_output_dir, client, counter):
    """
    Processes a single image: extracts text and saves to file.
    """
    image_filename = os.path.basename(image_path)
    print(f"\nProcessing OCR for {image_filename}...")
    
    image_bytes = preprocess_image(image_path)
    if image_bytes is None:
        print(f"Failed to preprocess image: {image_filename}. Skipping.")
        return
    
    text = extract_text_from_image(client, image_bytes)
    if not text:
        print(f"No text found in {image_filename}. Marking as undefined.")
        save_text_to_file(texts_output_dir, counter, "", image_filename)
        return
    
    save_text_to_file(texts_output_dir, counter, text, image_filename)

def extract_images_and_process(pdf_path, images_output_dir, texts_output_dir, client, starting_page=3, crop_margin=70):
    """
    Extracts images from a PDF, processes each image immediately, performs OCR, and saves the extracted text.
    """
    os.makedirs(images_output_dir, exist_ok=True)
    os.makedirs(texts_output_dir, exist_ok=True)
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Failed to open PDF file '{pdf_path}': {e}")
        return
    
    counter = -starting_page
    
    for page_index, page in enumerate(doc, start=1):
        print(f"\nProcessing Page {page_index}...")
        try:
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_data))
        except Exception as e:
            print(f"Failed to render page {page_index} to image: {e}")
            continue
        
        width, height = image.size
        left = crop_margin
        right = width - crop_margin
        image_cropped = image.crop((left, 0, right, height))
        
        new_width = image_cropped.width
        mid_point = new_width // 2
        left_image = image_cropped.crop((0, 0, mid_point, height))
        right_image = image_cropped.crop((mid_point, 0, new_width, height))
        
        # Process left image
        counter += 1
        left_image_filename = f"page_{page_index}_left.png"
        left_image_path = os.path.join(images_output_dir, left_image_filename)
        try:
            left_image.save(left_image_path)
            print(f"Saved left image: {left_image_path}")
        except Exception as e:
            print(f"Failed to save left image '{left_image_path}': {e}")
            continue
        process_single_image(left_image_path, texts_output_dir, client, counter)
        
        # Process right image
        counter += 1
        right_image_filename = f"page_{page_index}_right.png"
        right_image_path = os.path.join(images_output_dir, right_image_filename)
        try:
            right_image.save(right_image_path)
            print(f"Saved right image: {right_image_path}")
        except Exception as e:
            print(f"Failed to save right image '{right_image_path}': {e}")
            continue
        process_single_image(right_image_path, texts_output_dir, client, counter)
