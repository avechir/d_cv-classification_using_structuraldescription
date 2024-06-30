def findClosest(allhammingdistances):
    minhammingdistances = []
    closestetalon = []
    for j in range(len(allhammingdistances[0])):
        mindistance = 256
        etalon = 5
        for i in range(len(allhammingdistances)): 
            if (allhammingdistances[i][j]<mindistance):
                mindistance = allhammingdistances[i][j]
                etalon = i
        minhammingdistances.append(mindistance)
        closestetalon.append(etalon)
    return minhammingdistances, closestetalon

def countVotes(numofetalons, minhammingdistances, closestetalon, threshold):
    votesnumber = []
    for x in range(numofetalons):
        count = 0
        for i in range(len(closestetalon)):
            if (closestetalon[i] == x):
                if(minhammingdistances[i]<=threshold):
                    count = count + 1
        votesnumber.append(count)
    return votesnumber