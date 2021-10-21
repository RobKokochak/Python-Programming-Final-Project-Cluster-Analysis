import turtle
import csv
import random

def createCentroids(k, dataDict):
    centroids=[]
    centroidCount = 0
    centroidKeys = []        #list of unique keys

    while centroidCount < k:
       rKey = random.randint(1, len(dataDict))
       if rKey not in centroidKeys:   #if key not already selected
           centroids.append(dataDict[rKey]) #add to dictionary
           centroidKeys.append(rKey)  #add key to selected keys
           centroidCount = centroidCount + 1

    print("Centroids: ", centroids)
    return centroids

import math
def euclidD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        sum = sum + diff
        
    euclidDistance = math.sqrt(sum)
    return euclidDistance

def createClusters(k, centroids, dataDict, repeats):
    for aPass in range(repeats):
        print("****PASS", aPass + 1, "****")
        clusters = []           #create list of k empty lists
        for i in range(k):
           clusters.append([])

        for aKey in dataDict:  #calculate distance to centroid
           distances = []
           for clusterIndex in range(k):
                dtoC = euclidD(dataDict[aKey], centroids[clusterIndex])
                distances.append(dtoC)

           minDist = min(distances)  #find minimum distance
           index = distances.index(minDist)

           clusters[index].append(aKey) #add to cluster

        dimensions = len(dataDict[1])  #recompute the clusters
        for clusterIndex in range(k):
           sums = [0] * dimensions     #init sum for each dimension
           for aKey in clusters[clusterIndex]:
               dataPoints = dataDict[aKey]
               for ind in range(len(dataPoints)): #calculate sums
                   sums[ind] = sums[ind] + dataPoints[ind]
           for ind in range(len(sums)):  #calculate average
               clusterLen = len(clusters[clusterIndex])
               if clusterLen != 0:       #do not divide by 0
                  sums[ind] = sums[ind] / clusterLen

           centroids[clusterIndex] = sums #assign avg to centroids

        for c in clusters:    #output the clusters
           print("CLUSTER")
           for key in c:
               print(dataDict[key], end = " ")
           print()

    return clusters



def readEarthquakeFile(filename):
    dataFile = open(filename, "r") 
    csvReader = csv.reader(dataFile) 
    titles = next(csvReader)        #read and skip titles
    dataDict = {}
    key = 0

    for aLine in csvReader:
        key = key + 1               #key is the line number
        lat = float(aLine[1])       #extract latitude
        long = float(aLine[2])      #extract longitude
        dataDict[key] = [long, lat]

    return dataDict

def visualizeQuakes(dataFile):
    dataDict = readEarthquakeFile(dataFile)
    quakeCentroids = createCentroids(6, dataDict)
    clusters = createClusters(6, quakeCentroids, dataDict, 3)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(445, 253)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()

    colorList = ["red","lawngreen","blue","orange","cyan","yellow"]

    for clusterIndex in range(6):
        quakeT.color(colorList[clusterIndex]) #choose cluster color
        for aKey in clusters[clusterIndex]:
            lon = dataDict[aKey][0]
            lat = dataDict[aKey][1]
            quakeT.goto(lon * wFactor, lat * hFactor)
            quakeT.dot()
    quakeWin.exitonclick() 

visualizeQuakes("earthquakes.csv")
