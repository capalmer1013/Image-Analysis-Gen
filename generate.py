from PIL import Image, ImageFilter
import pickle
import random

width = raw_input('input image width: ')
height = raw_input('input image height: ')

with open('graph.pk1', 'rb') as graphFile:
    G = pickle.load(graphFile)
    print 'balls'

    im = Image.new('P', (width, height))
    im.convert('P', palette=G.palette, colors=10)
    pixels = im.load()

    currentState = 0

    for y in range(0, height):
        for x in range(0, width):
            pixels[x, y] = currentState

            if x+1 < width and y > 0:
                # not furthest right or top row
                leftState = pixels[x, y]
                topState = pixels[x+1, y-1]
                listOfStateProb = findStateProbabilities(leftState, topState)


            elif x+1 < width:
                # not furthest right but is top row
                print ''

            elif y > 0:
                # not the top row but futhest right
                print ''

            else:
                #furthest right and top row
                print ''

            pixels[x,y] = currentState


def findNextState(stateProbabilities):
    randomFloat = random.random()
    for i in range(len(stateProbabilities)):
        if stateProbabilities[i].getFloat() > 0:
            if stateProbabilities[i].getFloat() > randomFloat:
                return i
            else:
                randomFloat = randomFloat - stateProbabilities[i].getFloat()


def findStateIndex(state, Graph):
    for i in range(0, len(Graph.listOfNodes)):
        if Graph.listOfNodes[i].pixel == state:
            return i


def findStateProbabilities(left, top):
    leftList = []
    topList = []
    totalList = []

    if left is not None:
        leftList = left.right
    if top is not None:
        topList = top.bottom

    if len(leftList) == 0 or len(topList) == 0:
        if len(leftList) == 0:
            return topList
        if len(topList) == 0:
            return leftList
    else:
        for e in leftList:
            tempNode = e['node']
            # tempWeight = a rational
            tempWeight = e['weight']

            for f in topList:
                if f['node'] == tempNode:
                    tempWeight.numerator += f['weight'].numerator
                    tempWeight.denominator += f['weight'].denominator

            totalList.append({'node': tempNode, 'weight': tempWeight})

    return totalList
