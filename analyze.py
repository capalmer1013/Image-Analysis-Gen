from PIL import Image, ImageFilter
import ANN

G = ANN.AnnGraph()

def analyzeSquare(square, left, top, right, bottom):
    newnode = ANN.Node(square)
    newnode.addBottom(bottom)
    G.addNode(newnode)

def analyzePixel(pixel, left, top, right, bottom):
    newnode = ANN.Node(pixel)

    if newnode not in G.listOfNodes:
        newnode.addBottom(bottom)
        newnode.addTop(top)
        newnode.addLeft(left)
        newnode.addRight(right)
        G.addNode(newnode)
    else:
        i = G.listOfNodes.index(newnode)
        G.listOfNodes[i].addBottom(bottom)
        G.listOfNodes[i].addTop(top)
        G.listOfNodes[i].addLeft(left)
        G.listOfNodes[i].addRight(right)