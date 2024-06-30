from preprocessing.preprocessingstrategy import PreprocessingStrategy
from scipy.spatial.distance import hamming
from basefunctions import *
from preprocessing.findMedoid import findMedoid

class DataForAccelerationFinder(PreprocessingStrategy):
    def findMedoyidClosest(self, bit_descriptor, medoyid):
        min_distance = 256
        mindistance_des = []
        distances = []
        for des in bit_descriptor:
            distance = hamming(des, medoyid)*len(medoyid)
            distances.append(distance)
            if (distance<min_distance and distance>0):
                min_distance = distance
                mindistance_des = des
        return min_distance, mindistance_des
    
    def findMedoyidFurthest(self, bit_descriptor, medoyid):
        max_distance = 0
        maxdistance_des = []
        for des in bit_descriptor:
            distance = hamming(des, medoyid)*len(medoyid)
            if (distance > max_distance):
                max_distance = distance
                maxdistance_des = des
        return max_distance, maxdistance_des
    
    def descriptors_preprocessing(self, bit_des_etalons):
        etalons_medoids = []
        cmins = []
        cmaxs = []
        for bit_des_etalon in bit_des_etalons:
            medoyid, result = findMedoid(bit_des_etalon)
            etalons_medoids.append(medoyid)
            min_distance, mindistance_des = self.findMedoyidClosest(bit_des_etalon, medoyid)
            cmins.append(min_distance)
            max_distance, maxdistance_des = self.findMedoyidFurthest(bit_des_etalon, medoyid)
            cmaxs.append(max_distance)
        return etalons_medoids, cmins, cmaxs