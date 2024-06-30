import cv2
import csv
import time
from basefunctions import *
from imageprocessing import *
from matching.matching_contextclass import MatchContextClass
from matching.method1 import MatchingMethod1
from preprocessing.preprocessing_contextclass import PreprocessContextClass
from preprocessing.preprocess_granulation1 import GranulationWithThreshold
from preprocessing.preprocess_granulation2 import GranulationStartedFromMin
from preprocessing.preprocess_simpleremove import SimpleRemoving

features = cv2.ORB_create(500)

image1 = cv2.imread('etalonimages//sparrow3.jpg')
image1gray = makeImgGray(image1)
image2 = cv2.imread('etalonimages//synychka1.jpg')
image2gray = makeImgGray(image2)
image3 = cv2.imread('etalonimages//lastivka1.jpg')
image3gray = makeImgGray(image3)
image4 = cv2.imread('etalonimages//pigeon5.jpg')
image4gray = makeImgGray(image4)
image5 = cv2.imread('etalonimages//raven1.jpg')
image5gray = makeImgGray(image5)

des2 = findKeypoints(image1gray, features)
bit_des_etalon1 = convertAllDescriptors(des2)

des2 = findKeypoints(image2gray, features)
bit_des_etalon2 = convertAllDescriptors(des2)

des2 = findKeypoints(image3gray, features)
bit_des_etalon3 = convertAllDescriptors(des2)

des2 = findKeypoints(image4gray, features)
bit_des_etalon4 = convertAllDescriptors(des2)

des2 = findKeypoints(image5gray, features)
bit_des_etalon5 = convertAllDescriptors(des2)

bit_des_etalons = [bit_des_etalon1, bit_des_etalon2, bit_des_etalon3, bit_des_etalon4, bit_des_etalon5]

image6 = cv2.imread('notetalonimages//duck2.jpg')
image6gray = makeImgGray(image6)
image7 = cv2.imread('notetalonimages//jay2.jpg')
image7gray = makeImgGray(image7)
image8 = cv2.imread('notetalonimages//starling3.jpg')
image8gray = makeImgGray(image8)

originalimages = [image1gray, image2gray, image3gray, image4gray, image5gray, image6gray, image7gray, image8gray]

method1 = MatchingMethod1()
matcher = MatchContextClass(method1)

granulation1 = GranulationWithThreshold()
imgpreprocessor = PreprocessContextClass(granulation1)
reduced_descset_etalons1 = imgpreprocessor.descriptors_preprocessing(bit_des_etalons)
reduced_descset_etalons1 = imgpreprocessor.descriptors_preprocessing(reduced_descset_etalons1)

granulation2 = GranulationStartedFromMin()
imgpreprocessor.set_strategy(granulation2)
reduced_descset_etalons2 = imgpreprocessor.descriptors_preprocessing(bit_des_etalons)
reduced_descset_etalons2 = imgpreprocessor.descriptors_preprocessing(reduced_descset_etalons2)

preprocessing3 = SimpleRemoving()
imgpreprocessor.set_strategy(preprocessing3)
reduced_descset_etalons3 = imgpreprocessor.descriptors_preprocessing(bit_des_etalons)
reduced_descset_etalons3 = imgpreprocessor.descriptors_preprocessing(reduced_descset_etalons3)

allimages = []
for img in originalimages:
    originalimage = img
    rotatedimg1 = rotate_20_degrees(img)
    rotatedimg2 = rotate_minus20_degrees(img)
    resizedimg1 = scale_up(img)
    resizedimg2 = scale_down(img)
    rotated1resized1 = scale_up(rotatedimg1)
    rotated1resized2 = scale_down(rotatedimg1)
    rotated2resized1 = scale_up(rotatedimg2)
    rotated2resized2 = scale_down(rotatedimg2)
    imagesoptions = [originalimage, rotatedimg1, rotatedimg2,
                      resizedimg1, resizedimg2,
                     rotated1resized1, rotated1resized2, rotated2resized1, rotated2resized2]
    allimages.append(imagesoptions)

results = []
timeres = []
for i in range(len(allimages)):
    imageresults = []
    timeresfor1img = []
    for j in range(len(allimages[0])):
        method_results = []
        methodtimeres = []
        print("image " + str(i) + " " + str(j))
        des1 = findKeypoints(allimages[i][j], features)
        bit_des_img = convertAllDescriptors(des1)

        # without granulation
        matcher.set_strategy(method1)
        start = time.time()
        result_method1 = matcher.match_images(bit_des_img, bit_des_etalons)
        end = time.time()
        methodtimeres.append(end-start)
        method_results.append(result_method1)
        
        # granulation with threshold
        start = time.time()
        result_granulation1method1 = matcher.match_images(bit_des_img, reduced_descset_etalons1)
        end = time.time()
        methodtimeres.append(end-start)
        method_results.append(result_granulation1method1)

        # granulation by distance
        start = time.time()
        result_granulation2method1 = matcher.match_images(bit_des_img, reduced_descset_etalons2)
        end = time.time()
        methodtimeres.append(end-start)
        method_results.append(result_granulation2method1)

        # simple removing
        start = time.time()
        result_simpleremoving = matcher.match_images(bit_des_img, reduced_descset_etalons3)
        end = time.time()
        methodtimeres.append(end-start)
        method_results.append(result_simpleremoving)
        
        imageresults.append(method_results)
        timeresfor1img.append(methodtimeres)
    results.append(imageresults)
    print(imageresults)
    timeres.append(timeresfor1img)
print("\ntime in seconds:")
print(timeres)

accuracies = []
for img in results:
    img_accuracies = []
    for transformedimg in img:
        transformedimg_accuracies = []
        for method in transformedimg:
            method_accuracies = []
            maxelem1st = max(method)
            maxelem2nd = 0
            for elem in method:
                if(elem>maxelem2nd and elem != maxelem1st):
                    maxelem2nd = elem
            accuracy = (maxelem1st-maxelem2nd)/sum(method)
            transformedimg_accuracies.append(round(accuracy, 3))
        img_accuracies.append(transformedimg_accuracies)
    accuracies.append(img_accuracies)
    
print(accuracies)

accuracies2d = [item for sublist in accuracies for item in sublist]
print(accuracies2d)

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(accuracies2d)
