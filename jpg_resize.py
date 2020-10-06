import os
import sys
from PIL import Image

max_size = 1654

list_img = os.listdir('./data_jpg/')
list_img_resize = os.listdir("./data_jpg_resize/")
count = 0

for item_img in list_img:
    print(count, "/", len(list_img))

    if item_img not in list_img_resize:
        img = Image.open('./data_jpg/' + item_img)

        width_org, height_org = img.size
        width_new = width_org
        height_new = height_org

        if width_org <= height_org:
            if height_org > max_size:
                height_new = max_size
                width_new = int(width_org*height_new/height_org)
                newsize = (width_new, height_new)
                img_new = img.resize(newsize)
                img_new = img_new.save("./data_jpg_resize/"+item_img)
        else:
            if width_org > max_size:
                width_new = max_size
                height_new = int(width_new*height_org/width_org)
                newsize = (width_new, height_new)
                img_new = img.resize(newsize)
                img_new = img_new.save("./data_jpg_resize/"+item_img)
    else:
        print("skip")

    count = count + 1
