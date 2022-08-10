import cv2
import numpy as np
import os


imgPaths="G:/U-2-Net-master/mask create/img/"

for images in os.listdir(imgPaths):
    # Read image
    img = cv2.imread(imgPaths+images)
    hh, ww = img.shape[:2]

    # threshold on white
    # Define lower and uppper limits
    lower = np.array([2, 2, 2])
    upper = np.array([255, 255, 255])

    # Create mask to only select black
    thresh = cv2.inRange(img, lower, upper)

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # invert morp image
    mask = 255 - morph

    # apply mask to image
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite("G:/U-2-Net-master/mask create/mask/"+images, morph)
   