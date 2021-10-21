#Rob Kokochak

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
           if dataDict[rKey][2] not in centroids: #to avoid having duplicate centroid values
               centroids.append(dataDict[rKey][2]) #add to dictionary
               centroidKeys.append(rKey)  #add key to selected keys
               centroidCount = centroidCount + 1

    print("Centroids: ", centroids)
    return centroids

import math
def euclidD(dataList, centroid):
    sum = 0
    #calculate the distance between the 3rd val of dataList and val of centroid
    diff = abs(dataList[2]-centroid)
    return diff

def createClusters(k, centroidsList, dataDict, repeats):
    for aPass in range(repeats):
        print("\n****PASS", aPass + 1, "****")
        clusters = []
        #create list of k empty lists
        for i in range(k):
           clusters.append([])

        for aKey in dataDict:
            #calculate distance to centroid
           distances = []
           for clusterIndex in range(k):
                dtoC = euclidD(dataDict[aKey], centroidsList[clusterIndex])
                distances.append(dtoC)

           minDist = min(distances)  #find minimum distance
           index = distances.index(minDist)

           clusters[index].append(aKey) #add to cluster

        for clusterIndex in range(k):
            #recompute the centroids for each cluster.
            #The average of all data points in the cluster.
            #iterate through the points, create a running sum,
            #and divide by the number of points.
            sum = 0
            for item in clusters[clusterIndex]:
                sum += item
            if len(clusters[clusterIndex]) != 0:
                avg = sum / len(clusters[clusterIndex])
            centroidsList[clusterIndex] = avg #assign avg to centroids

        number = 1
        for c in clusters:    #output the clusters to the terminal
            print("\nCLUSTER", number,"\n")
            for key in c:
                print(dataDict[key], end = " ")
            print()
            number += 1


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
        depth = float(aLine[3])
        dataDict[key] = [long, lat, depth]

    return dataDict

def visualizeQuakes(dataFile):
    dataDict = readEarthquakeFile(dataFile) #a dict of locations/depths lists
    quakeCentroids = createCentroids(6, dataDict) #a list of 6 depth centroids
    clusters = createClusters(6, quakeCentroids, dataDict, 1)
    print("Drawing in window - will alert when done...")

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
        quakeT.speed(0)
        for aKey in clusters[clusterIndex]:
            lon = dataDict[aKey][0]
            lat = dataDict[aKey][1]
            quakeT.goto(lon * wFactor, lat * hFactor)
            quakeT.dot()
    print("Done")
    quakeWin.exitonclick() 

visualizeQuakes("earthquakes.csv")
