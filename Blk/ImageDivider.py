from PIL import Image

suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

image = Image.open("./image/deck.jpg")
originX = originY = 0
lengthX = 56
lengthY = 81

for i in range(4):
    for j in range(13):
        image_cropped = image.crop((originX + lengthX * j, originY + lengthY * i, originX + lengthX * (j + 1), originY + lengthY * (i + 1)))
        image_cropped.save(f"./images/{ranks[j]}{suits[i]}.png")

image_cropped = image.crop((112, 326, 168, 408))
image_cropped.save(f"./images/backside.png")