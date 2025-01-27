##Description
This script demonstrates the use of adaptive thresholding and simple thresholding techniques on an image. Adaptive thresholding is particularly useful for images with varying lighting conditions, as it calculates thresholds for smaller regions of the image, resulting in better differentiation between foreground and background.

##Features
Converts the input image to grayscale.
Applies simple thresholding to produce a binary image.
Applies adaptive thresholding using the Gaussian method for better accuracy in uneven lighting scenarios.
Displays the original image along with the results of simple and adaptive thresholding.
##Prerequisites
Python 3.x
OpenCV library (cv2)
A folder named imgs containing the input image (happy.jpg).
##How to Run
Place your input image (happy.jpg) inside the imgs folder.
Execute the script:
bash
Copy
Edit
python adaptive_thresholding.py
Two windows will display the results:
Adaptive Threshold Image
Simple Threshold Image
##Customization
To change the image, replace happy.jpg with your desired image in the imgs folder.
Modify the adaptiveThreshold parameters for different effects:
blockSize: Adjust the size of the region to calculate the threshold.
C: Change this constant for fine-tuning threshold calculation.
