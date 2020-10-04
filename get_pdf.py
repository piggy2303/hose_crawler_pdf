import requests
import os

list_file = open("result.txt", "r")
list_pdf = os.listdir("./data/")

file_error = open("result_error.txt", "a+")

print(list_pdf)

count = 1
for link_pdf in list_file:
    link_pdf = link_pdf.strip()

    file_name = "vn30_"+str(count).zfill(3)+".pdf"
    if file_name not in list_pdf:
        print("download ", count, link_pdf)

        try:
            a = requests.get(link_pdf, timeout=30)
            save_pdf = open('./data/'+file_name, 'wb')
            save_pdf.write(a.content)
            save_pdf.close()
        except Exception as error:
            error = str(error)
            print(error)
            file_error.write(link_pdf+"\n")
            file_error.write(error+'\n')

    count = count + 1

file_error.close()
