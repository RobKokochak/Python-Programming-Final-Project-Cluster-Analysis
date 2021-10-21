#Rob Kokochak

import math

def euclidD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        sum = sum + diff
        
    euclidDistance = math.sqrt(sum)
    return euclidDistance

dataFile = open("data.txt", "r")
_2dPoints = []

for line in dataFile: #make list of 2d points within their own list
    lineSplit = line.split()
    x = float(lineSplit[0])
    y = float(lineSplit[1])
    _2dPoints.append([x,y])

distances = []
for point in _2dPoints:
    distances.append([]) #create list of lists for each point's distance to others

#calculate each point's distance to every point, including itself
spot = 0
for point in _2dPoints:
    for comparePoint in _2dPoints:
        distance = euclidD(point,comparePoint)
        distances[spot].append(distance)
    spot += 1

#top row of table
print("{0:7s}".format(" "), end = "") 
for point in range(len(_2dPoints)):
    print("{0:s}{1:<6d}".format("P",point+1), end = "")
print("")

#table
for point in range(len(_2dPoints)):
    print("{0:<7s}".format("P" + str(point+1)), end = '')
    for distance in range(len(distances[point])):
          print("{0:<7.2f}".format(distances[point][distance]), end = '')
    print("")
    
    
    
