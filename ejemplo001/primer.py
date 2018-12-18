import cv2

import pytesseract

im = cv2.imread("example_02.jpg")

texto = pytesseract.image_to_string(im)

print(texto)
