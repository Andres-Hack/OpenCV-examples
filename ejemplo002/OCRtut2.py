import cv2
list1=[]
img=cv2.imread('test2.png')
C,H,W=img.shape[::-1]
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,47,255,cv2.THRESH_BINARY)
_,contours,_=cv2.findContours(thresh[:,0:H/2,],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    perimeter=cv2.arcLength(contours[i],True)
    if perimeter > 250 and perimeter < 350:
        cv2.drawContours(img,contours,i,(0,255,0),2)
        list1.append(i)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
