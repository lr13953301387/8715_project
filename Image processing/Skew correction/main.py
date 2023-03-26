import cv2
import numpy as np

# Read the image and convert it to grayscale
img = cv2.imread("result.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarization
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


#cv2.imshow("thresh",thresh)
#cv2.waitKey(0)
# Connected domain analysis
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# Calculate the minimum bounding rectangle and rotation angle of all connected domains
angles = []
for cnt in contours:
    rect = cv2.minAreaRect(cnt) # return (center(x,y), (width,height), angle) tuple
    angle = rect[-1]
    if angle < -45:
        angle += 90 # The adjustment range is [-45,45]
    angle=int(angle)
    angles.append(angle)
    print(angle)

# Take the median of the rotation angles of all connected domains as the text skew angle
median_angle = np.median(angles)
s0=np.arange(1000)
for i in range(len(angles)):
    s0[angles[i]]=s0[angles[i]]+1
max_ang=0
ang=0
for i in range(0,90):
    print(str(i)+" "+str(angles[i]))
    if(s0[i]>max_ang):
        ang=i
        max_ang=s0[i]
median_angle=ang-90
print("test:"+str(ang))
# Rotate image by average angle
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, median_angle*-1 , 1.0)
rotated = cv2.warpAffine(thresh,M,(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)

# Show results
cv2.imshow("Original", img)
rotated=~rotated
cv2.imshow("Rotated", rotated)
cv2.imwrite("rotated.jpg",rotated)
cv2.waitKey(0)