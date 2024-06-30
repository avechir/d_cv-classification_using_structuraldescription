from basefunctions import *
from matching.countvotes import countVotes
from matching.findhamdist import findDistancesToMedoids
from matching.imagematchingstrategy import ImageMatchingStrategy

class MatchingTriangleRuleMethod(ImageMatchingStrategy):

    def match_images(self, bit_des_img, dataforaccelerating):
        medoids, cmins, cmaxs = dataforaccelerating
        descriptors_medoids_distances = findDistancesToMedoids(bit_des_img, medoids)
        inequalitiesarray = []
        for i in range(len(descriptors_medoids_distances)):
            descriptorineqarr = []
            for j in range(len(descriptors_medoids_distances[0])):
                oneinequalityarr = []
                leftpart = abs(descriptors_medoids_distances[i][j] - cmaxs[j])
                rightpart = descriptors_medoids_distances[i][j] + cmins[j]
                oneinequalityarr.append(leftpart)
                oneinequalityarr.append(rightpart)
                descriptorineqarr.append(oneinequalityarr)
            inequalitiesarray.append(descriptorineqarr)

        print("left parts, cmax")
        minleftparts = []
        closestetalon = []
        for i in range(len(inequalitiesarray)):
            etalon = 5
            min_leftpart = 256
            for j in range(len(inequalitiesarray[0])):
                if (inequalitiesarray[i][j][0]<min_leftpart):
                    min_leftpart = inequalitiesarray[i][j][0]
                    etalon = j
            minleftparts.append(min_leftpart)
            closestetalon.append(etalon)

        votesnumber = countVotes(len(inequalitiesarray[0]), minleftparts, closestetalon, 256)
       
        return votesnumber