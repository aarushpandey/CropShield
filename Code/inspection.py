import os
from PIL import Image

root = "C:\\Users\\aarus\\OneDrive\\Desktop\\Aarush\\Hackathons\\Crop Pest Detection\\Rice_and_Maize_Dataset\\Data"

for crop in ["Rice", "Maize"]:
    print(f"\n{crop.upper()}")

    # print(os.walk(os.path.join(root, crop)))
    for category, dirs, files in os.walk(os.path.join(root, crop)):
        images = []
        # print(category)
        for f in files:
            
            if f.lower().endswith("jpg"):
                image = Image.open(os.path.join(root, crop, category, f))
                width, height = image.size
                # print((width, height))
                r = width/height
                print(r)
                images.append(f)
                # print(f)
                

        # print(len(images))

    