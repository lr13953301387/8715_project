import cv2
import numpy as np

# Copy image function
def clone(img):
    height = img.shape[0]
    width = img.shape[1]
    img2=np.zeros((height,width),np.uint8)
    for i in range(0,height):
        for j in range(0,width):
            img2[i,j]=img[i,j]
    return img2
# Read image file
img = cv2.imread("1.jfif")
#img=cv2.imread("3.jfif")
#img=cv2.imread("J249.jfif")
#img=cv2.imread("5.jfif")

# Get image size
height = img.shape[0]
width = img.shape[1]

# Reduce the size of the image by half to speed up processing
img = cv2.resize(img,(height//2,width//2))
cv2.imshow("input",img)
# Convert to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(str(height)+","+str(width))
# Adaptive thresholding, parameters can be adjusted as needed
# Otsu's thresholding method, parameters can be adjusted as needed
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Convert to black background and white image for easier processing
binary=~binary
# Find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the largest contour (white) on a blank black image
mask = np.zeros_like(gray)

# Traversing the contours and removing the border lines
for i in range(len(contours)):
    rect = cv2.minAreaRect(contours[i])
    center, (width, height), angle = rect
    # print(str(width)+" "+str(height))
    cv2.drawContours(mask, contours, i, 255, -1)
    # Remove lines
    if(width<10 and height>30):
        cv2.drawContours(mask, contours, i, 0, -1)
    if(height<10 and width>30):
        cv2.drawContours(mask, contours, i, 0, -1)
    # Remove contours that are too large
    if(height>100 or width>100):
        cv2.drawContours(mask,contours,i,0,-1)

# cv2.imshow("binary",binary)
# cv2.imshow("Mask", mask)
# cv2.waitKey(0)

# Setting dilation size for morphological dilation operation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))

# Performing dilation operation on the image
mask1=clone(mask)
mask1=cv2.medianBlur(mask1, 3)
dilated = cv2.dilate(mask1, kernel)

# Display original image and processed image
#cv2.imshow("Original", img)
#cv2.imshow("Dilated", dilated)
# Find contours
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Select the regions containing characters to be retained
mask2 = np.zeros_like(gray)
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area > 6200:
        cv2.drawContours(mask2, contours, i, 255, -1)

# Draw the largest contour (white) onto a blank black image
#cv2.imshow("mask2",mask2)
#cv2.imshow("Binary",binary)

# Create character region map
mask3=np.zeros_like(gray)
h = mask3.shape[0]
w = mask3.shape[1]
# Retain character regions
for i in range(0,h):
    for j in range(0,w):
        if(mask2[i,j]==255 and binary[i,j]==255):
            mask3[i,j]=255

# If the character is too large and the noise is small, it will be considered as the result
result0=clone(mask3)
cv2.namedWindow("win")

#cv2.imshow("mask2", mask2)
#cv2.imshow("mask3",mask3)
#cv2.imshow("Original", img)
#cv2.imshow("Binary", binary)
# Find contours
contours, hierarchy = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Remove the large boundaries
for i in range(len(contours)):
    rect = cv2.minAreaRect(contours[i])
    center, (width, height), angle = rect
    if(width>30 or height>30):
        cv2.drawContours(mask3, contours, i, 0, -1)
#cv2.imshow("re",mask3)

# Morphological expansion, the expansion size is selected as 15
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
# Dilate the image
mask1=clone(mask3)
dilated = cv2.dilate(mask1, kernel)
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the index and area of a large contour
mask4 = np.zeros_like(gray)
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area > 5000:
        cv2.drawContours(mask4, contours, i, 255, -1)

# Keep characters within character boundaries
result=np.zeros_like(gray)
for i in range(0,h):
    for j in range(0,w):
        if(mask4[i,j]==255 and binary[i,j]==255):
            result[i,j]=255
#v2.imshow("result1",result)

# Remove border
contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    rect = cv2.minAreaRect(contours[i])
    center, (width, height), angle = rect
    if(width>30 or height>30):
        cv2.drawContours(result, contours, i, 0, -1)

BLACK = [0,0,0]
#cv2.imshow("_result",result)
print(result.shape)
# Execute if(0) when the text is large, and if(1) if the text is small
if(0):
    # Boundary expansion
    constant = cv2.copyMakeBorder(result,200,200,200,200,cv2.BORDER_CONSTANT,value=BLACK)
    # Black and white
    constant=~constant
    cv2.imshow("constant",constant)

    h = constant.shape[0]
    w = constant.shape[1]
#rect=(int(w/2-500),int(h/2-500),1000,1000)
    # The new image size is set to 1000, 1000
    x=int(w/2-500)
    y=int(h/2-500)
    w=1000
    h=1000
    crop = constant[y:h + y, x:w + x]
    cv2.imshow("crop",crop)
    # Zoom to 2000, 2000
    img = cv2.resize(img, (35 , 35))
    cv2.imwrite("result.jpg", crop)
else:
    # Read in the previously processed image result0 here
    constant = cv2.copyMakeBorder(result0, 200, 200, 200, 200, cv2.BORDER_CONSTANT, value=BLACK)
    cv2.imshow("constant", constant)
    constant = ~constant

    h = constant.shape[0]
    w = constant.shape[1]
    # rect=(int(w/2-500),int(h/2-500),1000,1000)
    x = int(w / 2 - 500)
    y = int(h / 2 - 500)
    w = 1000
    h = 1000
    crop = constant[y:h + y, x:w + x]
    cv2.imshow("crop", crop)
    img = cv2.resize(img, (35, 35))
    cv2.imwrite("result.jpg",crop)

cv2.waitKey(0)
cv2.destroyAllWindows()