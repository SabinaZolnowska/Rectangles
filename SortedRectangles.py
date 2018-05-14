from Refactory.RandomRectangleSize import RandomRectangleSize

class SortedRectangles(RandomRectangleSize):

    def __init__(self, size=100, maxWidth = 5000, maxHeight = 4000):
        self.RectangleHorizontal = list()
        self.RectangleVertical = list()
        self.SquareH = list()
        self.SquareV = list()
        self.size = size
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.createRadomRectangles()
        self.sortLists()

    def createRadomRectangles(self):
        for i in range(0, self.size):
            x = (RandomRectangleSize(self.maxWidth, self.maxHeight))
            if x.group == "rectangleHorizontal":
                self.RectangleHorizontal.append(x)
            elif x.group == "rectangleVertical":
                self.RectangleVertical.append(x)
            elif x.group == "squareH":
                self.SquareH.append(x)
            else:
                self.SquareV.append(x)


    def sortLists(self):
        self.RectangleHorizontal.sort(key=lambda x:x.width, reverse=True)
        self.RectangleVertical.sort(key=lambda x:x.height, reverse=True)
        self.SquareH.sort(key=lambda x:x.width, reverse=True)
        self.SquareV.sort(key=lambda x:x.height, reverse=True)


