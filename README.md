# GerrymanderProject
This is a gerrymander project for Precal (Shaun)

### Members:
    Gene Wicaksono
    Rocky Shao
    Lucas Matthingly

### Goal:
    input an image and determine:
        (1) the contiguos of this district
        (2) the compactness of this district
    
### Setup:
    1.download python 3 <br>
    2.download an IDE that supports python <br>
    3.create a new empty folder <br>
    4.right click the folder, select "open in terminal" <br>
    5.type in the following commands in the terminal:
            (1):    git clone   https://github.com/Rocky0Shao/GerrymanderProject.git
            (2):    pip install opencv-python

### GUI
<img src = "Readme_imgs\GUI.png">
Upon running this program, 3 windows will open. The first has sliders, which allow ou do configure different color filters, and display different elements of our analysis.

 The second is the display window. Upon filtering districts, ideal circles will be drawn along with contiguousness and solidity values. You also have the ability to select different districts by clicking on them. Finally, there is a filtering window. Our filter method relies on an HSV filter for colors. The filter window assists the user in finding their desired HSV thresholds for the districts they wish to analyze.
 <img src = "Readme_imgs\Selection.png">

### About:
Here is our program that can detect the factors of voting districts that contribute to gerrymandering. 
Gerrymandering, the manipulation of district boundaries to benefit a particular political party or group, 
is a serious issue that undermines the integrity of democratic elections.  
It can result in the unfair representation of certain communities, the suppression of minority voices, 
and the consolidation of power in the hands of a select few.  


Our program aims to allow the user to input an image of a voting district and establish the values of the contiguous and solidity of the district.

We define solidity as the area of a contour subtracted by the areas of all child contours, divided by the area of the parent contour's 
onvex hull.
If we have parent contour $C_p$, $n$ child contours denoted by $C_c$, and the convex hull of the parent contour, $H$, solidity would be defined as:
$$\frac {\left(C_p - \left({C_{c_1}}+ {C_{c_2}}+ {C_{c_3}}+\dots +{C_{c_n}}\right)\right)} {H}$$

A convex hull is a boundary which a line segment connecting any two points within the boundary does not intersect the boundary.

Compactness of a voting district is measured in a different way. 
If the shape of the voting district is a perfect circle, the compactness will be 100%.
The general formula for compactness is: 4pi * (A/P^2), where A is the area of the district and P is the parameter of the district.
For visualizatoin, a circle that has the same area as the distric will appear upon the district

These values will allow the user to then calculate whether or not the district has fallen victim to political gerrymandering or not.  
In addition, the program can aid the user in determining what group or groups have been suppressed.  


We hope that our program can lead to the removal of gerrymandered voting districts and the unfair representation of minority groups and communities.  
In turn, this will allow us to hold fair and impartial elections and promote greater transparency and acountability in the political process.  
We believe that developing a reliable and accurate tool to detect gerrymandering, 
we can ensure that all voices are heard and all communities are represented fairly in our democracy. 
>>>>>>> f3c5d4f227f8e1c548d3619b2cf802223fdc14c2
