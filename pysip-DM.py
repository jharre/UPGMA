import sys


hashOriginal = {}
hashClusters = {}
hashNewick = {}
codeHash = {}

data = None
codes = []
numOTU = None
distmatrix = []
temp = None

#print("Enter the name of the distance matrix file: \n")
fileinput = input("Enter the name of the distance matrix file: \n")
#fileinput.rstrip('\n')
#try:
infile1 = open(fileinput, "r+")
#except:
#    print("error opening input file 1\n")
#    exit()

with infile1:
    data = infile1.readline()
    numOTU = int(data.strip("\n"))
    data = infile1.readline()
    codes = data.rstrip("\n").split()

    for i in range(numOTU):
        codeHash[codes[i]] = i
        hashNewick[codes[i]] = codes[i]

        hashClusters[codes[i]] = {0 : codes[i]}

        for line in infile1:
            line = line.rstrip("\n").split()
            distmatrix.append(line)


print("\n    ")
print(codes)
print('\n')
for i in range(numOTU):
    print(codes[i] + ': ')
    for j in range(numOTU):
        print(distmatrix[i][j])
        hashOriginal[codes[i]] = {codes[j] : distmatrix[i][j]}
    print('\n')

MAXDIST = 999999
numClusters = numOTU
while numClusters > 1:
    smallest = MAXDIST
    smallestI = 0
    smallestJ = 0
    arrayClusters = hashClusters.keys()
    for i in range(numClusters - 1):
        for j in range(1, numClusters):
            tempDist = int(distmatrix[i][j])
            if tempDist > 0:
                if tempDist < smallest:
                    smallest = tempDist
                    smallestI = i
                    smallestJ = j
    clusterI = arrayClusters[smallestI]
    clusterJ = arrayClusters[smallestJ]
    merge = clusterI + clusterJ
    print("Merging Clusters: " + clusterI + " and " + clusterJ + " with distance " + distmatrix[i][j] + "\n")
    i = 0
    for j in range(len(clusterI)):
        hashClusters[merge] = hashClusters[clusterJ]  #issue is here
        i = i + 1
    for j in range(len(clusterJ)):
        hashClusters[merge] = hashClusters[clusterJ] #issue is here
        i = i + 1
    hashNewick[merge] = "(" + hashNewick[clusterI] + "," + hashNewick[clusterJ] + ")"
    del hashClusters[clusterI]
    del hashClusters[clusterJ]
    del hashNewick[clusterI]
    del hashNewick[clusterJ]
    numClusters = numClusters - 1

arrayClusters = hashClusters.keys()
print("\nNewick format" + hashNewick[arrayClusters[0]] + "\n")
