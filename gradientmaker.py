from PIL import Image
from math import sqrt
from window import GradientWindow

width = 500
height = 500

color1 = (21, 235, 203)
color2 = (235, 21, 153)
p1 = (0, height/2)
p2 = (width, height/2)


image = Image.new("RGB", (width, height))
pixels = image.load()

def getPixelColor(x, y):
    coef1 = (sqrt( (p1[0]-x)**2 + (p1[1]-y)**2 )) / (sqrt(2) * width/2)
    coef2 = (sqrt((p2[0]-x)**2 + (p2[1]-y)**2)) / (sqrt(2) * height/2)

    r = interpolateColor(coef1, coef2, 0)
    g = interpolateColor(coef1, coef2, 1)
    b = interpolateColor(coef1, coef2, 2)
    color = (r,g,b)

    #print((coef1, coef2), (x, y), color)
    return color

def interpolateColor(coef1, coef2, colorIndex):
    weighted1 = coef1*color1[colorIndex]
    weighted2 = coef2*color2[colorIndex]
    ws = [weighted1, weighted2]

    ws.sort()

    return int((ws[0] + ws[1]) / 2)

for x in range(width):
    for y in range(height):
        pixels[x, y] = getPixelColor(x, y)

win = GradientWindow((500, 600), "GradientMaker")
win.set_image(image)
win.show()

#image.show()
