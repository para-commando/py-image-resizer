import cv2

def is_integer(value):
    return isinstance(value, int)


# cv2.IMREAD_UNCHANGED: This flag tells OpenCV to load the image as is,
image = cv2.imread("./non-modified-images/garud-commando.jpg",cv2.IMREAD_UNCHANGED)
# cv2.imshow("garud-commando-image",image)

width_scale_percentage=input("Enter width scale percentage ")
height_scale_percentage=input("Enter height scale percentage ")

try:

    width_scale_percentage = int(width_scale_percentage)
    height_scale_percentage = int(height_scale_percentage)
# Check if it's an integer
    if is_integer(height_scale_percentage) and is_integer(width_scale_percentage):

        new_height_percentage = height_scale_percentage / 100
        # shape 0 holds the image height
        scaled_height = int(image.shape[0] * new_height_percentage);

        new_width_percentage= width_scale_percentage/100
        # shape 1 holds the image width
        scaled_width= int(image.shape[1]*new_width_percentage);

        modified_image= cv2.resize(image, (scaled_width, scaled_height))
        cv2.imwrite('scaledImage.jpg',modified_image)
    else:
        print("Input is not an integer.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


# decides for how long the image should be available for display in miliseconds, setting it to 0 makes it available until we manually close it
# cv2.waitKey(0)