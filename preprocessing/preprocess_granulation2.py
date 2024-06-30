from preprocessing.preprocessingstrategy import PreprocessingStrategy
from scipy.spatial.distance import hamming
from basefunctions import *

class GranulationStartedFromMin(PreprocessingStrategy):
    def findMinHammingDistances(self, bit_descriptors1):
        minhammingdistances = []
        for desc1 in bit_descriptors1:
            min_distance = 256
            descriptor2 = []
            arr = []
            for desc2 in bit_descriptors1:
                distance = hamming(desc1, desc2)*len(desc1)
                if(distance>0):
                    if (min_distance>distance):
                        min_distance = distance
                        descriptor2 = desc2
            arr.append(min_distance)
            arr.append(desc1)
            arr.append(descriptor2)
            minhammingdistances.append(arr)
        return minhammingdistances

    def granulation(self, sorted_mindistances):
        del_list = []
        descriptors = [sublist[1] for sublist in sorted_mindistances]
        result_len = len(descriptors)/2
        # result_len = 250
        for i in range(len(sorted_mindistances)):
            if(len(descriptors)>result_len):
                if ((sorted_mindistances[i][1] not in del_list) and (sorted_mindistances[i][2] not in del_list)):
                    descriptors.remove(sorted_mindistances[i][1])
                    del_list.append(sorted_mindistances[i][1])
        return descriptors

    def descriptors_preprocessing(self, bit_des_etalons):
        reduced_desc_etalons = []
        for bit_des_etalon in bit_des_etalons:
            mindistances = self.findMinHammingDistances(bit_des_etalon)
            sorted_mindistances = sorted(mindistances, key=lambda x: x[0])
            reduceddesc = self.granulation(sorted_mindistances)
            reduced_desc_etalons.append(reduceddesc)
        return reduced_desc_etalons
        