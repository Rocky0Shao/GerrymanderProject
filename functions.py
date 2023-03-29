
import cv2
import numpy as np

import math




def generate_mask(input_image,a,b,c,d,e,f):
    input_image_copy = cv2.cvtColor(input_image,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([a,c,e])
    higher_blue = np.array([b,d,f])
    mask = cv2.inRange(input_image_copy,lower_blue,higher_blue, cv2.THRESH_BINARY)
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    mask = cv2.dilate(mask,kernal,iterations = 3)
    return mask



def find_contour_circle_radius(contour):
    contour_area = cv2.contourArea(contour)
    contour_circle_radius = (contour_area /math.pi)**0.5
    return int(contour_circle_radius)

def find_biggest_contour(contours):
    """RETURNS THE CONTOUR, AND THEN THE INDEX OF SAID CONTOUR"""
    biggest = 0
    for x in range(len(contours)):
        if cv2.contourArea(contours[x]) > cv2.contourArea(contours[biggest]):
            biggest = x
    return contours[biggest], biggest


def find_contour_containing_point(currentindex, contours, hierarchy, clickpoint):
    for i in range(len(contours)):
        if cv2.pointPolygonTest(contours[i], clickpoint, False) > 0:
            return contours[i], i
    return None
def sort_contours(contours):
    sortedContours = sorted(contours, key=lambda contour: -cv2.contourArea(contour))
    
    return sortedContours


    
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


def find_contour_aspect_ratio(contour,color_image, draw=True):
    box= cv2.minAreaRect(contour)
    points = cv2.boxPoints(box)
    asint = np.int0(points)
    
    if len(asint) > 0:
        if draw:
            cv2.drawContours(color_image,[asint],0,(255,255,0),3) #DRAWS BOXES
        center, dimensions, angle= cv2.minAreaRect(contour)
        width,height = dimensions
        try:
            ratio = height/width
            if ratio > 1: ratio = width/height
            return ratio*100,width,height
        except:
            return 0
    return 0

def solidityTest(contourindex, colorimg, contours, hierarchy, draw = True):
    solidity = 0
    current_contour = contours[contourindex]

    if draw:
        cv2.drawContours(colorimg, current_contour,0,(255,255,0),3)
    try:
        center, dimensions, angle= cv2.minAreaRect(current_contour)
        width,height = dimensions
        
        bounding_area = width * height
        area_of_contour = cv2.contourArea(current_contour)
    except:
        pass

    if hierarchy[0][contourindex][2] != -1:
            # Iterate through child contours
            child = hierarchy[0][contourindex][2]
            while child != -1:
                # Access child contour and do something with it
                child_contour = contours[child]

                cv2.drawContours(colorimg, child_contour,0,(255,255,0),3)
                area_of_contour -= cv2.contourArea(child_contour)
                # Move to next child contour
                child = hierarchy[0][child][0]
    
    solidity = area_of_contour / bounding_area
    return solidity



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



