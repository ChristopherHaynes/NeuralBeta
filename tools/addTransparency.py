from PIL import Image

for i in range(1, 11):
    holdName = "res/hold" + str(i) + ".png"
    newHoldName = "res/hold" + str(i) + "T.png"
    image = Image.open(holdName)
    image = image.convert('RGBA')

    newImage = []
    for item in image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)

    image.putdata(newImage)
    image.save(newHoldName)