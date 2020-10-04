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
file_error = open("result_error.txt", "a+")

list_jpg = os.listdir("./data_jpg/")

print(list_pdf)

for f in list_pdf:
    ff = "./data/"+f
    try:
        print("doing ", f)
        images = convert_from_path(ff)

        for i, image in enumerate(images):
            newfilename = f[:-4] + "_page" + str(i + 1) + '.jpg'
            if newfilename not in list_jpg:
                newfilename = './data_jpg/' + newfilename
                print("saving ", newfilename)
                image = image.save(newfilename)
            else:
                print("done ", newfilename)
    except Exception as error:
        error = str(error)
        print(error)
        file_error.write(f+"\n")
        file_error.write(error+'\n')


file_error.close()
