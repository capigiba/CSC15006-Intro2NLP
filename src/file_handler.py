import os
import re

def save_text_to_file(output_dir, counter, text, image_filename):
    """
    Saves the extracted text to a file named based on the counter and numbers in parentheses.
    """
    from src.text_utils import extract_all_numbers_in_parentheses

    numbers_in_parentheses = extract_all_numbers_in_parentheses(text)
    if numbers_in_parentheses:
        sanitized_numbers = '_'.join([f"({num})" for num in numbers_in_parentheses])
        filename = f"{counter}_{sanitized_numbers}.txt"
    else:
        filename = f"{counter}_undefined.txt"

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, filename)

    # Handle filename duplication
    suffix = 1
    original_output_file = output_file
    while os.path.exists(output_file):
        if numbers_in_parentheses:
            output_file = os.path.join(output_dir, f"{counter}_{sanitized_numbers}_{suffix}.txt")
        else:
            sanitized_image_name = os.path.splitext(image_filename)[0]
            output_file = os.path.join(output_dir, f"{counter}_undefined_{sanitized_image_name}_{suffix}.txt")
        suffix += 1

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved text to {output_file}")
    except Exception as e:
        print(f"Failed to save text to {output_file}: {e}")
