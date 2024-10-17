import cv2

# cv2.IMREAD_UNCHANGED: This flag tells OpenCV to load the image as is,
image = cv2.imread("./non-modified-images/garud-commando.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("garud-commando-image",image)
# decides for how long the image should be available for display in miliseconds, setting it to 0 makes it available until we manually close it
cv2.waitKey(0)