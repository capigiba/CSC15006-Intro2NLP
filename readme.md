# PDF OCR Extraction Project

## Overview

This project processes a PDF file by extracting images from each page, performing OCR (Optical Character Recognition) using Google Cloud Vision API, extracting numbers within parentheses from the text, and saving the results to text files with structured filenames.

## Project Structure
```
project/
├── config.yaml
├── main.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── vision_client.py
│   ├── image_utils.py
│   ├── text_utils.py
│   ├── file_handler.py
│   └── pdf_processor.py
└── README.md
```

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure `config.yaml`

- Update the `config.yaml` file with the appropriate paths and settings.