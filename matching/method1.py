from matching.imagematchingstrategy import ImageMatchingStrategy
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from matching.findhamdist import findHammingDistances
import numpy as np
import time
from basefunctions import *
from matching.countvotes import *

class MatchingMethod1(ImageMatchingStrategy):
    
    def match_images(self, bit_des_img, bit_des_etalons):
        allhammingdistances = []
        for bit_des_etalon in bit_des_etalons:
            hammingdistances = findHammingDistances(bit_des_img, bit_des_etalon)
            allhammingdistances.append(hammingdistances)
        minhammingdistances, closestetalon = findClosest(allhammingdistances)
        votesnumber = countVotes(len(allhammingdistances), minhammingdistances, closestetalon, 64)
        return votesnumber