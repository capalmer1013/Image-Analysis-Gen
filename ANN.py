from PIL import Image, ImageFilter

class Rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        self.initialized = False

    def success(self):
        if self.initialized:
            self.numerator += 1
            self.denominator += 1

        else:
            self.numerator += 1
            self.initialized = True

    def failure(self):
        if self.initialized:
            self.denominator += 1
        else:
            self.initialized = True


class AnnGraph:
    def __init__(self):
        self.listOfNodes = []
        self.dictOfEdges = {}
        # will be a dictionary of lists
        self.edgeWeights = {}

    def addNode(self, node):

    def addEdge(self, fromNode, toNode, weight):

    def saveGraph(self, graphName):

    def loadGraph(self, graphName):



class Node:
    def __init__(self, imageSquare):
        self.arrayOfPixels = []

