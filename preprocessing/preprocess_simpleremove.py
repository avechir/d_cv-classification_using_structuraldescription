from preprocessing.preprocessingstrategy import PreprocessingStrategy
from basefunctions import *

class SimpleRemoving(PreprocessingStrategy):
    def remove250desc(self, bit_des_etalon):
        etalon_250descriptors = []
        i=0
        for des in bit_des_etalon:
            if(i%2==0):
                etalon_250descriptors.append(des)
            i+=1
        return etalon_250descriptors

    def descriptors_preprocessing(self, bit_des_etalons):
        reduced_desc_etalons = []
        for bit_des_etalon in bit_des_etalons:
            reduceddesc = self.remove250desc(bit_des_etalon)
            reduced_desc_etalons.append(reduceddesc)
        return reduced_desc_etalons
        