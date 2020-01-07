from PIL import Image
from math import sqrt

class GradientBuilder:

    def __init__(self, width, height):
        self.size = (width, height)
        self.reset()

    def getPointsGradient(self, coords, colors):
        self.reset()

        if (len(coords) != len(colors)):
            print("Erreur: il n'y a pas autant de coordonnées que de couleurs")
            return self.image

        self.coords = coords
        self.colors = colors

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.pixels[x, y] = self.__getPixelColor(x, y)
        return self.image

    def __getPixelColor(self, x, y):
        coefs = []
        d_coefs = []
        sum_coefs = 0
        for coord in self.coords:
            coef = 1-((sqrt( (coord[0]-x)**2 + (coord[1]-y)**2 )) / self.size[0])
            sum_coefs += coef
            coefs.append(coef)

        for coef in coefs:
            d_coefs.append(coef/sum_coefs)

        r = self.__interpolatePixelSubColor(d_coefs, 0)
        g = self.__interpolatePixelSubColor(d_coefs, 1)
        b = self.__interpolatePixelSubColor(d_coefs, 2)
        color = (r,g,b)
        return color

    def __interpolatePixelSubColor(self, coefs, subColorIndex):
        ws = []
        for i, coef in enumerate(coefs):
            ws.append(coef*self.colors[i][subColorIndex])

        return int(sum(ws) / len(ws))

    def reset(self):
        self.image = Image.new("RGB", self.size)
        self.pixels = self.image.load()

        self.coords = []
        self.colors = []
