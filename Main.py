import cv2 
import numpy as np
import functions as f


#this file should take in test1.jpg and return the contiguos, compactness of the blue districts.

# input_image = cv2.imread("test1.jpg")
# low_H = 85
# high_H = 130
# low_S = 43
# high_S = 255
# low_V = 93
# high_V = 255



# input_image = cv2.imread("test2.jpg")
# low_H = 0
# high_H = 255
# low_S = 77
# high_S = 255
# low_V = 0
# high_V = 255



# input_image = cv2.imread("test3.jpg")
# low_H = 53
# high_H = 129
# low_S = 60
# high_S = 255
# low_V = 0
# high_V = 255

input_image = cv2.imread("test4.jpg")
low_H = 0
high_H = 3
low_S = 17
high_S = 255
low_V = 0
high_V = 255

<<<<<<< HEAD



<<<<<<< HEAD:test1.py
mask = f.maskForTest1(input_image,low_H,high_H,low_S,high_S,low_V,high_V)
=======
=======
>>>>>>> test
mask = f.generate_mask(input_image,low_H,high_H,low_S,high_S,low_V,high_V)
>>>>>>> test:Main.py
contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
contours = f.sort_contours(contours)
for contour in contours:
    try:
        cv2.drawContours(input_image,[contour],0,(0,0,0),3)
        aspect_ratio,width,height = f.find_contour_aspect_ratio(contour,input_image)
        circle_of_contor_radius = f.find_contour_circle_radius(contour)
        center = f.find_contour_center(contour)
        cv2.circle(input_image, center, 5, (0,0,155), -1)
        cv2.circle(input_image,center,circle_of_contor_radius,(233,0,155),3)
        x,y = center
        cv2.putText(input_image,f.format_num( float(f"{aspect_ratio}")), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        solidity = f.solidityTest(contour)
        cv2.putText(input_image, f.format_num(float(f"{solidity}")*100), (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        break
    except:
        continue


cv2.imshow("input_image",input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()