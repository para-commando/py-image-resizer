# py-image-resizer: Image Scaling with OpenCV

This Python script allows you to resize an image based on user-provided scaling percentages for the width and height. The image is read using OpenCV, resized, and then saved to the specified output directory.

## Features

- Load an image using OpenCV
- Resize the image based on user-provided width and height scaling percentages
- Save the modified image to a specified directory

## Prerequisites

- Python 3.x
- OpenCV (`cv2` module)
- `os` module (comes with Python)

You can install OpenCV using the following command:

```bash
pip install opencv-python
```

## Usage

1. Place your original image in the `non-modified-images` folder.
2. Run the script and provide the desired scaling percentages for width and height when prompted.
3. The script will resize the image according to the percentages and save the modified image in the `modified-images` folder.

## Sample Command to Run the Script

```bash
python image_scaling.py
```

### Example Input and Output
If you have an image called `garud-commando.jpg` in the `non-modified-images` directory, you will be asked to input the scaling percentages for the width and height. For example:

```bash
Enter width scale percentage: 50
Enter height scale percentage: 50
```

This will resize the image to 50% of its original width and height. The output image will be saved in the `modified-images` folder as `scaled_garud-commando.jpg`.
