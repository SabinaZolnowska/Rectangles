from random import randint

class RandomRectangleSize:

    def __init__(self, maxWidth = 5000, maxHeight = 4000):
        self.width = randint(1,maxWidth)
        self.height = randint(1,maxHeight)
        self.group = None
        self.edgeProportion()

    def edgeProportion(self):
        if self.width <= self.height:
            proportionWidth = self.width/self.height
            proportionHeight = 1
        else:
            proportionHeight = self.height/self.width
            proportionWidth = 1

        if proportionWidth<1:
            if proportionWidth<0.75:
                self.group = "rectangleVertical"
            else:
                self.group = "squareV"
        elif proportionHeight<0.75:
            self.group = "rectangleHorizontal"
        else:
            self.group ="squareH"

