import cv2
import matplotlib.pyplot as plt


def converttobin(n):
    return [int(digit) for digit in f'{n:08b}']

def convertDescriptor(descriptor):
    return [bit for byte in descriptor for bit in converttobin(byte)]

def convertAllDescriptors(descriptors):
    return [convertDescriptor(descriptor) for descriptor in descriptors]

def makeImgGray(image):
    imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return imagegray

def findKeypoints(imagegray, features):
    (keypoints, des) = features.detectAndCompute(imagegray, None)
    return des

def drawKeypointsMatches(image1, image2, matches, keypoints1, keypoints2):
    out = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:50], None, flags=0)
    plt.figure()
    plt.imshow(out)
