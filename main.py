import os
from src.config import Config
from src.vision_client import initialize_google_vision_client
from src.pdf_processor import extract_images_and_process

def main():
    # Load configuration
    config = Config('config.yaml')
    
    pdf_file = config.get('pdf_file')
    json_key_path = config.get('json_key_path')
    images_output_directory = config.get('images_output_directory')
    texts_output_directory = config.get('texts_output_directory')
    starting_page = config.get('starting_page', 3)
    crop_margin = config.get('crop_margin', 60)
    
    # Check if PDF exists
    if not os.path.exists(pdf_file):
        print(f"PDF file '{pdf_file}' does not exist. Exiting.")
        return
    
    # Initialize Google Cloud Vision client
    client = initialize_google_vision_client(json_key_path)
    if not client:
        print("Exiting due to Vision API initialization failure.")
        return
    
    # Extract images from PDF and process OCR immediately
    print("\nStarting image extraction from PDF and OCR processing...")
    extract_images_and_process(
        pdf_path=pdf_file,
        images_output_dir=images_output_directory,
        texts_output_dir=texts_output_directory,
        client=client,
        starting_page=starting_page,
        crop_margin=crop_margin
    )
    print("\nImage extraction and OCR processing completed.")

if __name__ == "__main__":
    main()
