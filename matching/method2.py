from matching.imagematchingstrategy import ImageMatchingStrategy
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
import time
from basefunctions import *
from matching.findhamdist import findHammingDistances

class MatchingMethod2(ImageMatchingStrategy):

    def findMinHammingDistances(self, hammingdistances):
        minhammingdistances = []
        count_less_than_64 = 0
        for element in hammingdistances:
            if element <= 64:
                count_less_than_64 += 1
                minhammingdistances.append(element)
        return count_less_than_64

    def match_images(self, bit_des_img, bit_des_etalons):
        less_than_threashold = []
        for bit_des_etalon in bit_des_etalons:
            hammingdistances = findHammingDistances(bit_des_img, bit_des_etalon)
            minhammingdistances_count = self.findMinHammingDistances(hammingdistances)
            less_than_threashold.append(minhammingdistances_count)
        
        return less_than_threashold