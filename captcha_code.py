import random
import string

print(string.ascii_uppercase)
print(string.digits)

characters = string.ascii_uppercase + string.digits
print(characters)


mygenerator = [random.choice(characters) for _ in range(7)]

str1 = ''
for _ in mygenerator:
    str1+=str(_)
print(str1)


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

img = Image.open("black and white.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype(Arial, 20)
# draw.text((x, y),"Sample Text",(r,g,b))
font = ImageFont.truetype("arial.ttf", 60)
draw.text((30, 70),str1,(255,255,255),font)
img.save('sample-out.jpg')
img.show()
img



def create_noise_curve(image):
        w, h = image.size
        x1 = random.randint(0, int(w / 5))
        x2 = random.randint(w - int(w / 5), w)
        y1 = random.randint(int(h / 5), h - int(h / 5))
        y2 = random.randint(y1, h - int(h / 5))
        points = [x1, y1, x2, y2]
        end = random.randint(160, 200)
        start = random.randint(0, 20)
        Draw(image).arc(points, start, end)
        image.save("arc1.jpg")
        return image
create_noise_curve(img)
img2 = Image.open("arc1.jpg")
import numpy as np
arr = np.array(img2)
print(np.shape(arr))
img2.show()


def create_noise_dots(image, width=3, number=300):
        draw = Draw(image)
        w, h = image.size
        while number:
            x1 = random.randint(0, w)
            y1 = random.randint(0, h)
            draw.line(((x1, y1), (x1 - 1, y1 - 1)), width=width)
            number -= 1
        return image
create_noise_dots(img2)
img3 = create_noise_dots(img2)
img3.show()



