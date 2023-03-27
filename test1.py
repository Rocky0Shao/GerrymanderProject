import cv2 
import numpy as np
import functions as f


#this file should take in test1.jpg and return the contiguos, compactness of the blue districts.
input_image = cv2.imread("test1.jpg")

h, w, _ = input_image.shape

print(h, w)



mask = f.maskForTest1(input_image)
contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    cv2.drawContours(input_image,[contour],0,(0,255,0),3)
    aspect_ratio,width,height = f.find_contour_aspect_ratio(contour,input_image)
    circle_of_contor_radius = int(((width/2)**2+(height/2)**2)**0.5)
    center = f.find_contour_center(contour)
    cv2.circle(input_image, center, 5, (255,0,255), -1)
    cv2.circle(input_image,center,circle_of_contor_radius,(233,0,155),5)
    x,y = center
    cv2.putText(input_image,f.format_num( float(f"{aspect_ratio}")), center, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    solidity = f.solidityTest(contours[-1])
    cv2.putText(input_image, f.format_num(float(f"{solidity}")*100), (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)


cv2.imshow("input_image",input_image)
f.show_image("test1",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()