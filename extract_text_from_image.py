import pytesseract
from PIL import Image
import os

# Path to the Tesseract executable (change this according to your OS)
# For Windows, you need to provide the correct path to the Tesseract executable
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # For macOS
# For Linux, it may just work without needing to specify the path if installed via package manager

# Function to read image and extract text using Tesseract OCR
def extract_text_from_image(image_path):
    try:
        # Open the image using PIL
        img = Image.open(image_path)
        
        # Perform OCR to extract text
        text = pytesseract.image_to_string(img)

        # Return the extracted text
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to save the extracted text to a file
def save_text_to_file(text, output_path):
    try:
        # Open the output file and write the extracted text
        with open(output_path, 'w') as file:
            file.write(text)
        print(f"Text successfully saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    # Path to the image file of your handwritten page (e.g., page1.jpg)
    image_file = 'path/to/your/handwritten_image.jpg'  # Replace with your image path
    
    # Extract text from image
    extracted_text = extract_text_from_image(image_file)

    if extracted_text:
        # Output path where the text will be saved (to a flash drive)
        output_path = '/path/to/your/flash_drive/output.txt'  # Replace with the path to your flash drive
        
        # Save the extracted text to the output file
        save_text_to_file(extracted_text, output_path)

# Run the main function
if __name__ == "__main__":
    main()
