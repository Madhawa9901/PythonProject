import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\Users\\Madhawa\\Desktop\\work\\python\\image5.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cla = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(8,8))
cla_img = cla.apply(gray)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(cla_img, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 100, 10)

# Find contours in the edge map
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank canvas for the vector design
canvas = np.zeros_like(image)

# Approximate contours with polygonal curves and draw them on the canvas
for contour in contours:
    epsilon = 0.001 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Smooth the approximated curve using the Ramer-Douglas-Peucker algorithm
    epsilon_smooth = 0.1 * epsilon
    approx_smooth = cv2.approxPolyDP(approx, epsilon_smooth, True)

    cv2.drawContours(canvas, [approx_smooth], -1, (0, 255, 0), 2)

# Save the vector design as an image
cv2.imwrite("vector_design.jpg", canvas)

# Display the original image and the vector design
cv2.imshow("Original Image", image)
cv2.imshow("Vector Design", canvas)
#cv2.imshow("Vector Design", cla_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
