from scipy.spatial.distance import hamming
def findMedoid(bit_descriptor):
        result = 128000
        medoid = []
        for desc1 in bit_descriptor:
            sum_distance = 0
            for desc2 in bit_descriptor:
                distance = hamming(desc1, desc2)*len(desc1)
                sum_distance = sum_distance + distance
            if (sum_distance<result):
                result = sum_distance
                medoid = desc1
        return medoid, result