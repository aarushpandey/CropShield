from PIL import Image
import numpy as np

healthy_leaf = Image.open("Data\\Maize\\Healthy\\4cdeda03-12be-4b7e-b141-5396aab92012.Jpg")
disease_leaf = Image.open("Data\\Maize\\Disease\\02_turcicum_leaf_blight\\2e22b706-6c2f-4ba5-96ec-be1fa5cc1358.Jpg")
pest_leaf = Image.open("Data\\Maize\\Insect-pests\\02_fall_armyworm\\Fall_Army_Worm157.jpg")
test_image = Image.open("C:\\Users\\aarus\\OneDrive\\Pictures\\Images\\Black n White dog.jpg")

mode = (test_image.mode)

# Obtaining the pixel matrix elements via recursion
# And Converting the pixel matrix to numpy array
pixel_array = []
for h in range(test_image.size[1]):
    pixel_array.append([])
    for w in range(test_image.size[0]):
        pixel_array[h].append(test_image.getpixel((w, h)))
pixels_numpy = np.array(pixel_array)

print(pixels_numpy.shape)
print(pixels_numpy.dtype)
print(pixels_numpy.size)



# Conversion and Saving
# gray_image = test_image.convert("L")
# gray_image.save("grayscale_image.png")

