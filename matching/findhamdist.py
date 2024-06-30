from scipy.spatial.distance import hamming
def findHammingDistances(bit_descriptors1, bit_descriptors2):
        hammingdistances = []
        for desc1 in bit_descriptors1:
            min_distance = 256
            for desc2 in bit_descriptors2:
                distance = hamming(desc1, desc2)*len(desc1)
                min_distance = min(min_distance, distance)
            hammingdistances.append(min_distance)
        return hammingdistances

def findDistancesToMedoids(bit_descriptors1, medoids):
        allhammingdistances = []
        for desc1 in bit_descriptors1:
            hammingdistances = []
            for desc2 in medoids:
                distance = hamming(desc1, desc2)*len(desc1)
                hammingdistances.append(distance)
            allhammingdistances.append(hammingdistances)
        return allhammingdistances