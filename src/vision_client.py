from google.cloud import vision
from google.oauth2 import service_account

def initialize_google_vision_client(json_path):
    """
    Initializes the Google Cloud Vision client using a JSON key file.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(json_path)
        client = vision.ImageAnnotatorClient(credentials=credentials)
        print("Google Cloud Vision client initialized successfully.")
        return client
    except Exception as e:
        print(f"Failed to initialize Google Cloud Vision client: {e}")
        return None
