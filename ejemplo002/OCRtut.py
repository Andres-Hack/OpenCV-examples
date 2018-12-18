import cv2
img=cv2.imread("diccionario/captcha2.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
ret,thresh=cv2.threshold(gray,47,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)
cv2.imshow("origibak",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
