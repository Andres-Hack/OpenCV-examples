import cv2
list1=[]
grid1=[]
img=cv2.imread('imagen.jpg')
C,H,W=img.shape[::-1]
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,47,255,cv2.THRESH_BINARY)
_,contours,_=cv2.findContours(thresh[:,0:H/2,],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    perimeter=cv2.arcLength(contours[i],True)
    if perimeter > 250 and perimeter < 350:
        cv2.drawContours(img,contours,i,(0,255,0),2)
        list1.append(i)
for x in list1:
        M=cv2.moments(contours[x])
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        # RESALTA LOS NUMERO QUE ESTAN JUNTOS
        #cv2.rectangle(img,(cx-40,cy-40),(cx+40,cy+40),(0,255,255),3)
        cropped=img[cy-40:cy+40,cx-40:cx+40]
        # IMPRIME EL PRIMER NUMERO DE LA IMAGEN
        #cv2.imshow("cropped",cropped)
        w,h,c=cropped.shape
        for i in range(10):
                template=cv2.imread("no"+str(i)+".png")
                result=cv2.matchTemplate(cropped,template,cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)
                if (max_val>0.9):
                        grid1.append(i)
print grid1[::-1]
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
