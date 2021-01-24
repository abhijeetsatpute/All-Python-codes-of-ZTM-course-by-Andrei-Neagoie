from PIL import Image , ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

#Returns image object
print(img)

#Prints image format (JPEG)
print(img.format)

#Prints image size (Resolution)
print(img.size)

#Prints image mode (RGB / GreyScale)
print(img.mode)

#Prints file name of image with path
print(img.filename)

#Image filtering
#BLUR
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'PNG')

#SMOOTH
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png', 'PNG')

#SHARPEN
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharp.png', 'PNG')

#Convert to GreyScale
filtered_img = img.convert('L')
filtered_img.save('grey.png', 'PNG')

#show() opens the file
filtered_img.show()

#rotate() rotates the Image
c = filtered_img.rotate(180)

#resize the image
resized_img = img.resize((100,50))    # but this can ruin the aspect ratio hence we use thumbnail method
resized_img.save("resized.png", "png")

#CROP
box = (100,100,400,400)
cropped_img = img.crop(box)
cropped_img.save("cropped_img.png", "png")

img.thumbnail((100,50))    # it will keep max. 50*50 aspect ratio, it can be like 30*50, but it won't exceed 50 pixels
img.save("thumbnailed.png", "png")
