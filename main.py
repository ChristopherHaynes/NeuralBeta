from PIL import Image, ImageDraw
import random

from hold import Hold

# Messy global variables which need to be reformed into a class/config etc
# PROGRAM GLOBALS
save = True

# WALL GLOBALS
width = 600
height = 1200
xCount = 10
yCount = 20
cellWidth = int(width / xCount)
cellHeight = int(height / yCount)
gridThickness = 1

# HOLD GLOBALS
numberOfHolds = 8

# Create a new blank image
img = Image.new('RGBA', (width + gridThickness, height + gridThickness), color='white')

# Draw the "grid" for placement reference
draw = ImageDraw.Draw(img)

for y in range(0, yCount):
    for x in range(0, xCount):
        draw.rectangle([x * cellWidth, y * cellHeight, (x + 1) * cellWidth, (y + 1) * cellHeight], outline='black')

# Generate a list of hold positions, types and rotations
holds = list()
usedPositions = list()
for i in range(0, numberOfHolds):
    # Select a random hold image
    holdName = "res/hold" + str(random.randint(1, 10)) + ".png"
    # Determine the position
    # BUG: Due to the size of holds they can sometimes be partially placed out of the bounds of the wall
    holdGridX = random.randint(0, xCount)
    holdGridY = random.randint(0, yCount)
    # Determine the rotation
    rotation = random.randint(0, 90)
    negative = random.randint(0, 1)
    if negative:
        rotation = -rotation
    newHold = Hold(holdName, holdGridX, holdGridY, rotation)
    # Stop multiple holds being placed in the same position
    # BUG: Due to differing hold sizes there can still be an overlap
    if len(usedPositions) > 1:
        while (holdGridX, holdGridY) in usedPositions:
            holdGridX = random.randint(0, xCount)
            holdGridY = random.randint(0, yCount)
    holds.append(newHold)
    usedPositions.append((holdGridX, holdGridY))

# Draw the generated holds
for hold in holds:
    with Image.open(hold.name).convert('RGBA') as holdImg:
        holdImg = holdImg.rotate(hold.rotation, expand=1)
        img.paste(holdImg, ((hold.gridX * cellWidth) + int(holdImg.width / 2), (hold.gridY * cellHeight) + int(holdImg.height / 2)))

# Show/save the finished image
img.show()
if save:
    img.save('output/testImage.png', format='png')
