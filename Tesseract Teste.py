import pytesseract as ocr
import cv2
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

phrase = ocr.image_to_string(cv2.imread('image com texto.png'), lang='por')
print(phrase)