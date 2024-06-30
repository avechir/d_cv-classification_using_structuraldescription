from preprocessing.preprocessingstrategy import PreprocessingStrategy
from basefunctions import *
from preprocessing.findMedoid import findMedoid

class MedoidsFinder(PreprocessingStrategy):
    def descriptors_preprocessing(self, bit_des_etalons):
        etalons_medoids = []
        for bit_des_etalon in bit_des_etalons:
            medoid, result = findMedoid(bit_des_etalon)
            etalons_medoids.append(medoid)
        return etalons_medoids
        