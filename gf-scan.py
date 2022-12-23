import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
import sys

DEFAULT_THRESHOLD = 0.25

def query_is_in_image(query:str, target:str,threshold=DEFAULT_THRESHOLD, debug:bool=False)->bool:
    """Checks if query is in image.
    Args:
        query (str): path to query image
        image (str): path to target image
    """
    img1 = cv.imread(query,cv.IMREAD_GRAYSCALE) 
    img2 = cv.imread(target,cv.IMREAD_GRAYSCALE) 
    img3 = ~img2 # inverted target image

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    kp3, des3 = sift.detectAndCompute(img3,None)

    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    matches2 = bf.knnMatch(des1,des3,k=2)
    matches = matches + matches2

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < threshold*n.distance:
            good.append([m])
    if debug:
        img4 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        plt.imshow(img4),plt.show()

    if good:
        return True
    return False

# reads all images in a provided directory
def get_images(path:str)->list:
    """Returns a list of images in a directory.
    Args:
        path (str): path to directory
    """
    images = []
    for file in os.listdir(path):
        if file.endswith(".jpg") or file.endswith(".png"):
            images.append(os.path.join(path, file))
    return images

#print(query_is_in_image('gf-query.png', 'gf-example.jpg', debug=False))
#print(query_is_in_image('gf-query.png', 'gf-example2.jpg', debug=False))
#print(query_is_in_image('gf-query.png', 'gf-fake.jpg', debug=False))

if __name__ == '__main__':
    validate_yes = get_images('data/yes/')
    validate_no = get_images('data/no/')

    # makes a list of decimals incrementing by 0.05 from 0.05 to 0.95
    thresholds = np.arange(0.05, .50, 0.05)
    #print (thresholds)

    # for each threshold, check the relationship between the types of errors
    for threshold in thresholds:
        print(f"Threshold: {threshold}")

        tp = 0
        fn = 0
        for image in validate_yes:
            if not query_is_in_image('gf-query.png', image, threshold):
                #print('False negative: {}'.format(image))
                fn += 1
            else:
                #print('True positive: {}'.format(image))
                tp += 1
        print('False negative: {}, True positive: {}'.format(fn/len(validate_yes), tp/len(validate_yes)))

        fp = 0
        tn = 0
        for image in validate_no:
            if not query_is_in_image('gf-query.png', image, threshold):
                #print('True negative: {}'.format(image))
                tn += 1
            else:
                #print('False positive: {}'.format(image))
                #query_is_in_image('gf-query.png', image, threshold=.25,debug=True)
                fp += 1
        print('True negative: {}, False positive: {}'.format(tn/len(validate_no), fp/len(validate_no)))

        """
        if len(sys.argv) != 3:
            print('Usage: python3 gf-scan.py <query> <target>')
            sys.exit(1)
        print(query_is_in_image(sys.argv[1], sys.argv[2], debug=False))
        """

