import cv2 
import numpy as np
import GerrymanderProject.functions as f



input_image = cv2.imread(r"C:\Users\labra\Gerry\test1.jpg")
mask = f.maskForTest1(input_image)
contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    cv2.drawContours(input_image,[contour],0,(0,255,0),3)
    aspect_ratio = f.find_contour_aspect_ratio(contour,input_image)



cv2.imshow("input_image",input_image)
f.show_image("test1",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()