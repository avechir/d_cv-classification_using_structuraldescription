from matching.imagematchingstrategy import ImageMatchingStrategy
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.spatial.distance import hamming
import numpy as np
import time
from basefunctions import *
from matching.countvotes import *
from matching.findhamdist import findDistancesToMedoids

class MatchingMethodByMedoids(ImageMatchingStrategy):

    def match_images(self, bit_des_img, bit_des_etalons_medoyids):
        descriptors_medoyids_distances = findDistancesToMedoids(bit_des_img, bit_des_etalons_medoyids)
        
        transposed_descriptors_medoyids_distances = [[descriptors_medoyids_distances[j][i] for j in range(len(descriptors_medoyids_distances))] for i in range(len(descriptors_medoyids_distances[0]))]
        minhammingdistances, closestetalon = findClosest(transposed_descriptors_medoyids_distances)
        votesnumber = countVotes(len(transposed_descriptors_medoyids_distances), minhammingdistances, closestetalon, 256)
        
        return votesnumber