import cv2
import numpy as np

# Load the image of the statue
image = cv2.imread("C:\\Users\\Madhawa\\Desktop\\work\\python\\image5.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, threshold = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# Find contours in the binary image
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty image to draw the contours
contour_image = np.zeros_like(image)

# Iterate over the contours and approximate them with a polygonal curve
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(contour_image, [approx], 0, (255, 255, 255), 2)

# Save the vectorized image to a file
cv2.imshow("Vector Design", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()