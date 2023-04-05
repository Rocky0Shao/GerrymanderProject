# GerrymanderProject
This is a gerrymander project for Precal (Shaun)

Members: Gene Wicaksono
         Rocky Shao
         Lucas Mattingly

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


### About:
Here is our program that can detect the factors of voting districts that contribute to gerrymandering. 
Gerrymandering, the manipulation of district boundaries to benefit a particular political party or group, 
is a serious issue that undermines the integrity of democratic elections.  
It can result in the unfair representation of certain communities, the suppression of minority voices, 
and the consolidation of power in the hands of a select few.  


Our program aims to allow the user to input an image of a voting district and establish the values of the contiguous and solidity of the district.

We define solidity as the area of a contour subtracted by the areas of all child contours, divided by the area of the parent contour's convex hull.
If we have parent contour $C_p$, $n$ child contours denoted by $C_c$, and the convex hull of the parent contour, $H$, solidity would be defined as:
$$\frac {\left(C_p - \sum_{1}^{n} {C_c}\right)} {H}$$

A convex hull is a boundary which a line segment connecting any two points within the boundary does not intersect the boundary.


These values will allow the user to then calculate whether or not the district has fallen victim to political gerrymandering or not.  
In addition, the program can aid the user in determining what group or groups have been suppressed.  




We hope that our program can lead to the removal of gerrymandered voting districts and the unfair representation of minority groups and communities.  
In turn, this will allow us to hold fair and impartial elections and promote greater transparency and acountability in the political process.  
We believe that developing a reliable and accurate tool to detect gerrymandering, 
we can ensure that all voices are heard and all communities are represented fairly in our democracy. 