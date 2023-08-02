# importing the opencv library
import cv2

# Getting the name of image from user (Image should be present in same folder)
source = input("Enter the name of image file with extension: ")

# By default, the image will have the name "image-new"
new = "image-new.jpg"

# Getting the scale of new image from user
scale = int(input("Enter the scale of new image: "))

# Reading the input file
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Can be used to show the input image
# cv2.imshow("title", src)
# cv2.waitKey(0)

# Changing the width and height of image
newWidth = int(src.shape[1] * scale/100)
newHeight = int(src.shape[0] * scale/100)

# Applying the new size to the image
output = cv2.resize(src, (newWidth, newHeight))

# Writing the new file to the destination
cv2.imwrite(new, output)


