import cv2
import os

#read image
i=1
imgPaths="G:/U-2-Net-master/train_data/gt_aug"
for images in os.listdir(imgPaths):
    img_grey = cv2.imread(imgPaths+'/'+images, cv2.IMREAD_GRAYSCALE)
    # define a threshold
    thresh = 30

    # threshold the image
    img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

    #save image
    cv2.imwrite('G:/U-2-Net-master/'+str(i)+'.png',img_binary) 
    i+=1