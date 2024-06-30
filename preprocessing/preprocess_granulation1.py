from preprocessing.preprocessingstrategy import PreprocessingStrategy
from scipy.spatial.distance import hamming
from basefunctions import *

class GranulationWithThreshold(PreprocessingStrategy):
    def granulationfunction(self, desc_etalon):
        for desc1 in desc_etalon:
            min_distance = 256
            descriptor2 = []
            for desc2 in desc_etalon:
                distance = hamming(desc1, desc2)*len(desc1)
                if(distance>0):
                    if (min_distance>distance):
                        min_distance = distance
                        descriptor2 = desc2
            if (min_distance <= 64):
                desc_etalon.remove(desc1)
        return desc_etalon

    def descriptors_preprocessing(self, bit_des_etalons):
        import copy
        desc_etalons = copy.deepcopy(bit_des_etalons)
        reduced_desc_etalons = []
        for desc_etalon in desc_etalons:
            reduceddesc = self.granulationfunction(desc_etalon)
            reduced_desc_etalons.append(reduceddesc)
        return reduced_desc_etalons
        