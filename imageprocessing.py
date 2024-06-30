import cv2
from scipy import ndimage

def rotate_20_degrees(image):
    rotatedimg = ndimage.rotate(image, 20)
    return rotatedimg

def rotate_minus20_degrees(image):
    rotatedimg = ndimage.rotate(image, -20)
    return rotatedimg

def scale_up(image):
    height, width = image.shape[:2]
    new_height = int(height * 1.2)
    new_width = int(width * 1.2)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def scale_down(image):
    height, width = image.shape[:2]
    new_height = int(height * 0.8)
    new_width = int(width * 0.8)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

