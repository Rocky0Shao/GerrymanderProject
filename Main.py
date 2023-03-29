#import opencv and numpy
import cv2  
import numpy as np
import functions as f


#change this to threshold different images
target_image = "test5.jpg"




#trackbar callback fucntion to update HSV value
def callback(x):
    global H_low,H_high,S_low,S_high,V_low,V_high,show_district_center,show_district_box,show_ideal_circle,puttext,draw_contour
    #assign trackbar position value to H,S,V High and low variable
    H_low = cv2.getTrackbarPos('low H','controls')
    H_high = cv2.getTrackbarPos('high H','controls')
    S_low = cv2.getTrackbarPos('low S','controls')
    S_high = cv2.getTrackbarPos('high S','controls')
    V_low = cv2.getTrackbarPos('low V','controls')
    V_high = cv2.getTrackbarPos('high V','controls')
    show_district_center = cv2.getTrackbarPos('show_center','controls')
    show_district_box = cv2.getTrackbarPos('show_box','controls')
    show_ideal_circle = cv2.getTrackbarPos('show_circle','controls')
    puttext = cv2.getTrackbarPos('put_text','controls')
    draw_contour=cv2.getTrackbarPos('draw_contour','controls')
    
def mouseCallback(event, x, y, flags, param):
    global clickpoint
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"CLICKED AT ({x},{y})")

        clickpoint = (x, y)



#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10)


#global variable
H_low = 0
H_high = 180
S_low= 0
S_high = 255
V_low= 0
V_high = 255

show_district_center = 0
show_district_box = 0
show_ideal_circle = 0
draw_contour = 0
puttext = 0


clickpoint = None


#create trackbars for high,low H,S,V 
cv2.createTrackbar('low H','controls',0,180,callback)
cv2.createTrackbar('high H','controls',180,180,callback)

cv2.createTrackbar('low S','controls',0,255,callback)
cv2.createTrackbar('high S','controls',255,255,callback)

cv2.createTrackbar('low V','controls',0,255,callback)
cv2.createTrackbar('high V','controls',255,255,callback)

cv2.createTrackbar('draw_contour','controls',0,1,callback)
cv2.createTrackbar('show_box','controls',0,1,callback)
cv2.createTrackbar('show_circle','controls',0,1,callback)
cv2.createTrackbar('show_center','controls',0,1,callback)
cv2.createTrackbar('put_text','controls',0,1,callback)


print("got here")
while(1):
    try:
        #read source image
        img=cv2.imread(target_image)
        #convert sourece image to HSC color mode
        mask = f.generate_mask(img,H_low,H_high,S_low,S_high,V_low,V_high)
        #masking HSV value selected color becomes black
        res = cv2.bitwise_and(img, img, mask=mask)



        #show image

        # f.show_image('res',res)

        contours, hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


        biggest_contour, biggest_contour_index = f.find_biggest_contour(contours)
        if clickpoint:
            if f.find_contour_containing_point(biggest_contour_index, contours, hierarchy, clickpoint):
                biggest_contour, biggest_contour_index = f.find_contour_containing_point(biggest_contour_index, contours, hierarchy, clickpoint)
                print("SUCCESSFUL CLICK")
        aspect_ratio, width,height = f.find_contour_aspect_ratio(biggest_contour,img, False)

        if draw_contour ==1:
            for c in contours:
                cv2.drawContours(img,[c],0,(0,0,0),3)
            
        if show_district_box ==1:
            aspect_ratio,width,height = f.find_contour_aspect_ratio(biggest_contour,img)
            
        circle_of_contor_radius = f.find_contour_circle_radius(biggest_contour)
        center = f.find_contour_center(biggest_contour)
        
        if show_district_center==1:
            cv2.circle(img, center, 5, (0,0,155), -1)
            
        if show_ideal_circle == 1:
            cv2.circle(img,center,circle_of_contor_radius,(233,0,155),3)
            
        x,y = center
        solidity = f.solidityTest(biggest_contour_index, img, contours, hierarchy, True)
        
        if puttext ==1:
            
            cv2.putText(img, "Solidity score:"+ f.format_num(float(f"{solidity}")*100), (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(img,"Contiguousness score:"+ f.format_num( float(f"{aspect_ratio}")), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        # Verti = np.concatenate((res, img), axis=0)
        f.show_image('output',img)
        f.show_image('input',res)
        cv2.setMouseCallback("output", mouseCallback)
        cv2.waitKey(1)
    except:
        pass
