from PIL import Image
import random
#var
# Define some houses
houses = [(100, 100), (200, 200), (300, 300), (400, 400)]
wayColor = (125, 125, 125)
houseColor = (255, 0, 0)
#set
# Create a white 500x500 image
img = Image.new('RGB', (500, 500), color='white')

def randomPlacing(x, y):
    startx, starty = x, y
    endx, endy = x+50, y+50

    for pixely in range(starty, endy):
        for pixelx in range(startx, endx):
            if random.randint(0, 1) == 1:
                img.putpixel((pixelx, pixely), wayColor)
#code

# Add houses to the image
for house in houses:
    x, y = house
    img.putpixel((x, y), (255, 0, 0))  # Red pixel at house location
    for offsetx in range(10):
        for offsety in range(10):
            img.putpixel((x+offsetx, y+offsety), (255, 0, 0))  # Red pixel around house location


# First placing
for y in range(0, 500, 50):
    for x in range(0, 500, 50):
        randomPlacing(x, y)




for round in range(10):
    # Algorithm here

    for y in range(0, 500, 50):
        for x in range(0, 500, 50):
            housePixels = 0
            wayPixels = 0

            startx, starty = x, y
            endx, endy = x+50, y+50


            for pixely in range(starty, endy):
                for pixelx in range(startx, endx):
                    if img.getpixel((pixelx, pixely)) == houseColor:
                        housePixels += 1
                    elif img.getpixel((pixelx, pixely)) == wayColor:
                        wayPixels += 1
                    
                    if not wayPixels == 0:
                        oldEfficiencyScore = housePixels/wayPixels
                    else:
                        oldEfficiencyScore = 0
                    print(f"Square at x:{pixelx} has reached score: {oldEfficiencyScore}")

            randomPlacing(x, y)

            



    # Save the image
    img.save('map.png')




for x in range(0, 500, 50):
    for y in range(0, 500, 50):
        img.putpixel((x, y), houseColor)   # Some Borders
        img.putpixel((x+1, y), houseColor)   # Some Borders
        img.putpixel((x+1, y+1), houseColor)   # Some Borders
        img.putpixel((x, y+1), houseColor)   # Some Borders

# Save the image
img.save('map.png')