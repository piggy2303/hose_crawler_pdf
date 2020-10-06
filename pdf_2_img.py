import os
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import PIL

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

list_pdf = os.listdir('./data/')
count_all = len(list_pdf)
file_error = open("result_error.txt", "a+")

list_jpg = os.listdir("./data_jpg/")
set_jpg = set()
for i in list_jpg:
    i = i.split("_")[1]
    i = int(i)
    print(i)
    set_jpg.add(i)


print(list_pdf)

count = 0

for f in list_pdf:
    try:
        if int(f.split("_")[1].split(".")[0]) in set_jpg:
            print("skip", f)
        else:
            print(count, count_all)
            print("doing ", f)
            ff = "./data/"+f
            images = convert_from_path(ff)

            for i, image in enumerate(images):
                newfilename = f[:-4] + "_page" + str(i + 1) + '.jpg'
                newfilename = './data_jpg/' + newfilename
                print("saving ", newfilename)
                image = image.save(newfilename)

    except Exception as error:
        error = str(error)
        print(error)
        file_error.write(f+"\n")
        file_error.write(error+'\n')

    count = count + 1


file_error.close()
