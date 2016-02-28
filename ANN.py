from PIL import Image, ImageFilter

class Rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        self.initialized = True

    def success(self):
        if self.initialized:
            self.numerator += 1
            # self.denominator += 1

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

    def addNode(self, node):

        self.listOfNodes.append(node)

    def addEdge(self, fromNode, toNode, weight, direction):
        indexString = str(self.listOfNodes.index(fromNode))+'-'+str(self.listOfNodes.index(toNode))
        self.dictOfEdges[indexString] = {'fromNode': fromNode, 'toNode': toNode, 'weight': weight, 'direction': direction}

    def saveGraph(self, graphName):
        print "save graph"
    def loadGraph(self, graphName):
        print "load graph"



class Node:
    def __init__(self, pixel):
        self.pixel = pixel
        self.top = []
        self.left = []
        self.right = []
        self.bottom = []

    def __eq__(self, other):
        return self.pixel == other.pixel

    def addTop(self, topNode):
        found = False
        if topNode is not None:
            for e in self.top:
                e['weight'].failure()
                if e['node'] == topNode:
                    e['weight'].success()
                    found = True
                    break

            if not found:
                self.top.append({'node': topNode, 'weight': Rational()})

    def addLeft(self, leftNode):
        found = False
        if leftNode is not None:
            for e in self.left:
                e['weight'].failure()
                if e['node'] == leftNode:
                    e['weight'].success()
                    found = True
                    break

            if not found:
                self.left.append({'node': leftNode, 'weight': Rational()})

    def addRight(self, rightNode):
        found = False
        if rightNode is not None:
            for e in self.right:
                e['weight'].failure()
                if e['node'] == rightNode:
                    e['weight'].success()
                    found = True
                    break

            if not found:
                self.right.append({'node': rightNode, 'weight': Rational()})

    def addBottom(self, bottomNode):
        found = False
        if bottomNode is not None:
            for e in self.bottom:
                e['weight'].failure()
                if e['node'] == bottomNode:
                    e['weight'].success()
                    found = True
                    break

            if not found:
                self.bottom.append({'node': bottomNode, 'weight': Rational()})




    # def addTop(self, topNode):
    # def addLeft(self, leftNode):
    # def addRight(self, rightNode):
