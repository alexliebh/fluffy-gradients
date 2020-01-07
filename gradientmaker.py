from window import GradientWindow
from gradient import GradientBuilder

image_height = 500
image_width = 500

p1 = (0, image_width/2)
p2 = (image_height, image_width/2)
p3 = (0, 0)

color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)

gb = GradientBuilder(image_height, image_width)
image = gb.getPointsGradient([p1, p2], [color1, color2])

win = GradientWindow((500, 600), "GradientMaker")
win.setup_ui()
win.set_image(image)

#image.show()
