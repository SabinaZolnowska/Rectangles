from Refactory.SortedRectangles import SortedRectangles


class MatchPictureAndCI(SortedRectangles):

    def __init__(self, size=100, maxWidth = 5000, maxHeight = 4000, errorDPI = 100):
        self.inch = 25.4
        self.sortedListsRandomPictures = SortedRectangles(400, maxWidth, maxHeight)
        self.sortedListsRandomCI = SortedRectangles(size, maxWidth=200, maxHeight=300)
        self.MatchedCIandPictures = {"CI": [], "Pictures": [], "EmptyCI": [], "NotUsedPictures": []}
        self.errorDPI = errorDPI
        #self.simpleMatchCIandPictures()
        self.complexMatch()

    def checkDPI(self, ci, picture):
        if picture.height/(ci.height/self.inch) < self.errorDPI:
            if picture.width/(ci.width/self.inch) < self.errorDPI:
                return "Incorrect"
            else:
                return "Low Height"
        elif picture.width/(ci.width/self.inch) < self.errorDPI:
            return "Low Width"
        else:
            return "Correct"

    def simpleMatchCIandPictures(self):
        while(self.sortedListsRandomCI.SquareV):
            if self.sortedListsRandomPictures.SquareV:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[0])
                del self.sortedListsRandomCI.SquareV[0]
                del self.sortedListsRandomPictures.SquareV[0]
            elif self.sortedListsRandomPictures.SquareH:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[0])
                del self.sortedListsRandomCI.SquareV[0]
                del self.sortedListsRandomPictures.SquareH[0]
            elif self.sortedListsRandomPictures.RectangleVertical:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[0])
                del self.sortedListsRandomCI.SquareV[0]
                del self.sortedListsRandomPictures.RectangleVertical[0]
            elif self.sortedListsRandomPictures.RectangleHorizontal:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[0])
                del self.sortedListsRandomCI.SquareV[0]
                del self.sortedListsRandomPictures.RectangleHorizontal[0]
        while(self.sortedListsRandomCI.SquareH):
            if self.sortedListsRandomPictures.SquareH:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[0])
                del self.sortedListsRandomCI.SquareH[0]
                del self.sortedListsRandomPictures.SquareH[0]
            elif self.sortedListsRandomPictures.SquareV:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[0])
                del self.sortedListsRandomCI.SquareH[0]
                del self.sortedListsRandomPictures.SquareV[0]
            elif self.sortedListsRandomPictures.RectangleHorizontal:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[0])
                del self.sortedListsRandomCI.SquareH[0]
                del self.sortedListsRandomPictures.RectangleHorizontal[0]
            elif self.sortedListsRandomPictures.RectangleVertical:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[0])
                del self.sortedListsRandomCI.SquareH[0]
                del self.sortedListsRandomPictures.RectangleVertical[0]
        while(self.sortedListsRandomCI.RectangleVertical):
            if self.sortedListsRandomPictures.RectangleVertical:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[0])
                del self.sortedListsRandomCI.RectangleVertical[0]
                del self.sortedListsRandomPictures.RectangleVertical[0]
            elif self.sortedListsRandomPictures.SquareV:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[0])
                del self.sortedListsRandomCI.RectangleVertical[0]
                del self.sortedListsRandomPictures.SquareV[0]
            elif self.sortedListsRandomPictures.SquareH:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[0])
                del self.sortedListsRandomCI.RectangleVertical[0]
                del self.sortedListsRandomPictures.SquareH[0]
            elif self.sortedListsRandomPictures.RectangleHorizontal:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[0])
                del self.sortedListsRandomCI.RectangleVertical[0]
                del self.sortedListsRandomPictures.RectangleHorizontal[0]
        while(self.sortedListsRandomCI.RectangleHorizontal):
            if self.sortedListsRandomPictures.RectangleHorizontal:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[0])
                del self.sortedListsRandomCI.RectangleHorizontal[0]
                del self.sortedListsRandomPictures.RectangleHorizontal[0]
            elif self.sortedListsRandomPictures.SquareH:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[0])
                del self.sortedListsRandomCI.RectangleHorizontal[0]
                del self.sortedListsRandomPictures.RectangleHorizontal[0]
            elif self.sortedListsRandomPictures.SquareV:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[0])
                del self.sortedListsRandomCI.RectangleHorizontal[0]
                del self.sortedListsRandomPictures.SquareV[0]
            if self.sortedListsRandomPictures.RectangleVertical:
                self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[0])
                del self.sortedListsRandomCI.RectangleHorizontal[0]
                del self.sortedListsRandomPictures.RectangleVertical[0]


    def complexMatchCISquareV(self):
        index = 0
        condition = 0
        while (self.sortedListsRandomCI.SquareV):
            if self.sortedListsRandomPictures.SquareV and condition == 0:
                lenghtPictureSquareV = len(self.sortedListsRandomPictures.SquareV)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.SquareV[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[index])
                    del self.sortedListsRandomCI.SquareV[0]
                    del self.sortedListsRandomPictures.SquareV[index]
                    index = 0
                elif DPI=="Low Width":
                    index = index + 1
                    if index < lenghtPictureSquareV:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.SquareV[index])
                    else:
                        condition = 1
                        index = 0
                else:
                    condition = 1
                    index = 0

            elif self.sortedListsRandomPictures.SquareH and condition == 1:
                lenghtPictureSquareH = len(self.sortedListsRandomPictures.SquareH)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.SquareH[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[index])
                    del self.sortedListsRandomCI.SquareV[0]
                    del self.sortedListsRandomPictures.SquareH[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureSquareH:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.SquareH[index])
                    else:
                        condition = 2
                        index = 0
            elif self.sortedListsRandomPictures.RectangleVertical and condition == 2:
                lenghtPictureRectangleVertical = len(self.sortedListsRandomPictures.RectangleVertical)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.RectangleVertical[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[index])
                    del self.sortedListsRandomCI.SquareV[0]
                    del self.sortedListsRandomPictures.RectangleVertical[index]
                    index = 0
                elif DPI == "Low Width":
                    index = index + 1
                    if index < lenghtPictureRectangleVertical:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.RectangleVertical[index])
                    else:
                        condition = 3
                        index = 0
                else:
                    condition = 3
                    index = 0

            elif self.sortedListsRandomPictures.RectangleHorizontal and condition == 3:
                lenghtPictureRectangleHorizontal = len(self.sortedListsRandomPictures.RectangleHorizontal)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareV[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[index])
                    del self.sortedListsRandomCI.SquareV[0]
                    del self.sortedListsRandomPictures.RectangleHorizontal[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureRectangleHorizontal:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareV[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                    else:
                        condition = 4
                        index = 0
                else:
                    condition = 4
                    index = 0

            else:
                self.MatchedCIandPictures["EmptyCI"].append(self.sortedListsRandomCI.SquareV[0])
                del self.sortedListsRandomCI.SquareV[0]

    def complexMatchCISquareH(self):
        index = 0
        condition = 0
        while (self.sortedListsRandomCI.SquareH):
            if self.sortedListsRandomPictures.SquareH and condition == 0:
                lenghtPictureSquareH = len(self.sortedListsRandomPictures.SquareH)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.SquareH[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[index])
                    del self.sortedListsRandomCI.SquareH[0]
                    del self.sortedListsRandomPictures.SquareH[index]
                    index = 0
                elif DPI=="Low Width":
                    index = index + 1
                    if index < lenghtPictureSquareH:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.SquareH[index])
                    else:
                        condition = 1
                        index = 0
                else:
                    condition = 2
                    index = 0
            elif self.sortedListsRandomPictures.SquareV and condition == 1:
                lenghtPictureSquareV = len(self.sortedListsRandomPictures.SquareV)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.SquareV[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[index])
                    del self.sortedListsRandomCI.SquareH[0]
                    del self.sortedListsRandomPictures.SquareV[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureSquareV:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.SquareV[index])
                    else:
                        condition = 2
                        index = 0
                else:
                    condition = 2
                    index = 0
            elif self.sortedListsRandomPictures.RectangleHorizontal and condition == 2:
                lenghtPictureRectangleHorizontal = len(self.sortedListsRandomPictures.RectangleHorizontal)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[index])
                    del self.sortedListsRandomCI.SquareH[0]
                    del self.sortedListsRandomPictures.RectangleHorizontal[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureRectangleHorizontal:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                    else:
                        condition = 3
                        index = 0
                else:
                    condition = 3
                    index = 0
            elif self.sortedListsRandomPictures.RectangleVertical and condition == 3:
                lenghtPictureRectangleVertical = len(self.sortedListsRandomPictures.RectangleVertical)
                DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.RectangleVertical[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.SquareH[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[index])
                    del self.sortedListsRandomCI.SquareH[0]
                    del self.sortedListsRandomPictures.RectangleVertical[index]
                    index = 0
                elif DPI == "Low Width":
                    index = index + 1
                    if index < lenghtPictureRectangleVertical:
                        DPI = self.checkDPI(self.sortedListsRandomCI.SquareH[0], self.sortedListsRandomPictures.RectangleVertical[index])
                    else:
                        condition = 4
                        index = 0
                else:
                    condition = 4
                    index = 0
            else:
                self.MatchedCIandPictures["EmptyCI"].append(self.sortedListsRandomCI.SquareH[0])
                del self.sortedListsRandomCI.SquareH[0]

    def complexMatchCIRectangleV(self):
        index = 0
        condition = 0
        while (self.sortedListsRandomCI.RectangleVertical):
            if self.sortedListsRandomPictures.RectangleVertical and condition == 0:
                lenghtPictureRectangleVertical = len(self.sortedListsRandomPictures.RectangleVertical)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.RectangleVertical[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[index])
                    del self.sortedListsRandomCI.RectangleVertical[0]
                    del self.sortedListsRandomPictures.RectangleVertical[index]
                    index = 0
                elif DPI=="Low Width":
                    index = index + 1
                    if index < lenghtPictureRectangleVertical:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.RectangleVertical[index])
                    else:
                        condition = 1
                        index = 0
                else:
                    condition = 1
                    index = 0
            elif self.sortedListsRandomPictures.SquareV and condition == 1:
                lenghtPictureSquareV = len(self.sortedListsRandomPictures.SquareV)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.SquareV[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[index])
                    del self.sortedListsRandomCI.RectangleVertical[0]
                    del self.sortedListsRandomPictures.SquareV[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureSquareV:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.SquareV[index])
                    else:
                        condition = 2
                        index = 0
                else:
                    condition = 2
                    index = 0
            elif self.sortedListsRandomPictures.SquareH and condition == 2:
                lenghtPictureSquareH = len(self.sortedListsRandomPictures.SquareH)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.SquareH[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[index])
                    del self.sortedListsRandomCI.RectangleVertical[0]
                    del self.sortedListsRandomPictures.SquareH[index]
                    index = 0
                elif DPI == "Low Width":
                    index = index + 1
                    if index < lenghtPictureSquareH:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.SquareH[index])
                    else:
                        condition = 3
                        index = 0
                else:
                    condition = 3
                    index = 0
            elif self.sortedListsRandomPictures.RectangleHorizontal and condition ==3:
                lenghtPictureRectangleHorizontal = len(self.sortedListsRandomPictures.RectangleHorizontal)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[index])
                    del self.sortedListsRandomCI.RectangleVertical[0]
                    del self.sortedListsRandomPictures.RectangleHorizontal[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureRectangleHorizontal:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleVertical[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                    else:
                        condition = 4
                        index = 0
                else:
                    condition = 4
                    index = 0
            else:
                self.MatchedCIandPictures["EmptyCI"].append(self.sortedListsRandomCI.RectangleVertical[0])
                del self.sortedListsRandomCI.RectangleVertical[0]


    def complexMatchCIRectangleH(self):
        index = 0
        condition = 0
        while (self.sortedListsRandomCI.RectangleHorizontal):
            if self.sortedListsRandomPictures.RectangleHorizontal and condition == 0:
                lenghtPictureRectangleHorizontal = len(self.sortedListsRandomPictures.RectangleHorizontal)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleHorizontal[index])
                    del self.sortedListsRandomCI.RectangleHorizontal[0]
                    del self.sortedListsRandomPictures.RectangleHorizontal[index]
                    index = 0
                elif DPI=="Low Width":
                    index = index + 1
                    if index < lenghtPictureRectangleHorizontal:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.RectangleHorizontal[index])
                    else:
                        condition = 1
                        index = 0
                else:
                    condition = 1
                    index = 0
            elif self.sortedListsRandomPictures.SquareH and condition == 1:
                lenghtPictureSquareH = len(self.sortedListsRandomPictures.SquareH)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.SquareH[index])
                if DPI=="Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareH[index])
                    del self.sortedListsRandomCI.RectangleHorizontal[0]
                    del self.sortedListsRandomPictures.SquareH[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureSquareH:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.SquareH[index])
                    else:
                        condition = 2
                        index = 0
                else:
                    condition = 2
                    index = 0
            elif self.sortedListsRandomPictures.SquareV and condition == 2:
                lenghtPictureSquareV = len(self.sortedListsRandomPictures.SquareV)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.SquareV[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.SquareV[index])
                    del self.sortedListsRandomCI.RectangleHorizontal[0]
                    del self.sortedListsRandomPictures.SquareV[index]
                    index = 0
                elif DPI == "Low Height":
                    index = index + 1
                    if index < lenghtPictureSquareV:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.SquareV[index])
                    else:
                        condition = 3
                        index = 0
                else:
                    condition = 3
                    index = 0
            elif self.sortedListsRandomPictures.RectangleVertical and condition == 3:
                lenghtPictureRectangleVertical = len(self.sortedListsRandomPictures.RectangleVertical)
                DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.RectangleVertical[index])
                if DPI == "Correct":
                    self.MatchedCIandPictures["CI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                    self.MatchedCIandPictures["Pictures"].append(self.sortedListsRandomPictures.RectangleVertical[index])
                    del self.sortedListsRandomCI.RectangleHorizontal[0]
                    del self.sortedListsRandomPictures.RectangleVertical[index]
                    index = 0
                elif DPI == "Low Width":
                    index = index + 1
                    if index < lenghtPictureRectangleVertical:
                        DPI = self.checkDPI(self.sortedListsRandomCI.RectangleHorizontal[0], self.sortedListsRandomPictures.RectangleVertical[index])
                    else:
                        condition = 4
                        index = 0
                else:
                    condition = 4
                    index = 0
            else:
                self.MatchedCIandPictures["EmptyCI"].append(self.sortedListsRandomCI.RectangleHorizontal[0])
                del self.sortedListsRandomCI.RectangleHorizontal[0]




    def complexMatch(self):
        self.complexMatchCISquareV()
        self.complexMatchCISquareH()
        self.complexMatchCIRectangleV()
        self.complexMatchCIRectangleH()











y = MatchPictureAndCI()


for i in range(0, len(y.MatchedCIandPictures["CI"])):
    print("Picture: width = " + str((y.MatchedCIandPictures["Pictures"][i]).width) + " height = " + str((y.MatchedCIandPictures["Pictures"][i]).height))
    print("CI: width = " + str((y.MatchedCIandPictures["CI"][i]).width) + " height = " + str((y.MatchedCIandPictures["CI"][i]).height))

for i in range(0, len(y.MatchedCIandPictures["Pictures"])):
    print("Picture: width = " + str((y.MatchedCIandPictures["Pictures"][i]).width) + " height = " + str((y.MatchedCIandPictures["Pictures"][i]).height))
    print("CI: width = " + str((y.MatchedCIandPictures["CI"][i]).width) + " height = " + str((y.MatchedCIandPictures["CI"][i]).height))

print("-----------------------------------------------------------------------")
print("Amount of empty CI: " + str(len(y.MatchedCIandPictures["EmptyCI"])))

for i in range(0, len(y.MatchedCIandPictures["EmptyCI"])):
    print("Empty CI: width = " + str((y.MatchedCIandPictures["EmptyCI"][i]).width) + " height = "+ str((y.MatchedCIandPictures["EmptyCI"][i]).height))

