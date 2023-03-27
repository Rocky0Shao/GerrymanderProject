
import cv2
import numpy as np

import math




def maskForTest1(input_image):
    input_image_copy = cv2.cvtColor(input_image,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([85,43,93])
    higher_blue = np.array([130,255,255])
    mask = cv2.inRange(input_image_copy,lower_blue,higher_blue, cv2.THRESH_BINARY)
    kernal = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    mask = cv2.dilate(mask,kernal,iterations = 3)
    return mask



def find_biggest_contour(contours):
    sortedContours = sorted(contours, key=lambda contour: -cv2.contourArea(contour))
    biggest_contour=sortedContours[0]
    return biggest_contour

    
def find_contour_center(contour):
    #cv2.drawContours(frame,[biggest_contour],0,(0,255,0),3)
    moments = cv2.moments(contour)
    if moments['m00'] !=0:
        center=((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
        return center
    else:
        return (0,0)


'''convert an np 2d array into a list of tuples, represent contour points'''
def convert_contours_to_points(contour): 
    points_array=contour.tolist()
    points_tuple=[]#position of convex points
    for i in points_array:
        for c in i:
            c=tuple(c)
            points_tuple.append(c)
    return points_tuple
'''get the point on the ground'''


def find_contour_aspect_ratio(contour,color_image):
    box= cv2.minAreaRect(contour)
    points = cv2.boxPoints(box)
    asint = np.int0(points)
    
    if len(asint) > 0:
        cv2.drawContours(color_image,[asint],0,(255,255,0),5) #DRAWS BOXES
        center, dimensions, angle= cv2.minAreaRect(contour)
        width,height = dimensions
        
        ratio = height/width
        if ratio > 1: ratio = width/height
        return ratio*100
    return 0

def solidityTest(contour):
    try:
        center, dimensions, angle= cv2.minAreaRect(contour)
        width,height = dimensions
        
        bounding_area = width * height
        area_of_contour = cv2.contourArea(contour)
        return area_of_contour / bounding_area
    except:
        return 0

def find_contour_length(contour):
    contour_length = cv2.arcLength(contour,True)
    return contour_length



def show_image(window_name,img_to_show):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, img_to_show)

def format_num(num):
    formatted_num = "{:.1f}".format(num)
    return formatted_num  #returns a string

def putText(img,text,position,color):
    cv2.putText(img, text,position, cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)



