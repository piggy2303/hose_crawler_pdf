import requests

file_result = open("result.txt", "a+")
file_error = open("result_error.txt", "a+")

# 0 - 2000
# 4950106 - 4952106

arr_vn30 = [
    "BID",
    "CTG",
    "EIB",
    "FPT",
    "GAS",
    "HDB",
    "HPG",
    "KDH",
    "MBB",
    "MSN",
    "MWG",
    "NVL",
    "PLX",
    "PNJ",
    "POW",
    "REE",
    "ROS",
    "SAB",
    "SBT",
    "SSI",
    "STB",
    "TCB",
    "TCH",
    "VCB",
    "VHM",
    "VIC",
    "VNM",
    "VPB",
    "VRE"
]

for co_phieu_code in arr_vn30:
    try:
        link_list_data = 'https://tcanalysis.tcbs.com.vn/v1/news/activities?fData=' + \
            co_phieu_code+'&fType=tickers&size=1000'

        print(link_list_data)
        list_data = requests.get(link_list_data).json()
        list_data = list_data["listActivityNews"]

        arr_id = []
        for item in list_data:
            print(item["id"])
            arr_id.append(item["id"])

        for index_page in arr_id:
            link_page = "https://tcanalysis.tcbs.com.vn/v1/news/activity/" + \
                str(index_page)+"/detail"
            print(link_page)

            a = requests.get(link_page)
            a = a.json()
            a = a["content"].split('"')
            for i in a:
                if i[0:4] == "http" and i[-3:].lower() == "pdf":
                    print(i)
                    file_result.write(i+"\n")

    except Exception as error:
        error = str(error)
        print(error)

        file_error.write(co_phieu_code+"\n")
        file_error.write(link_page+"\n")
        file_error.write(error+'\n')

file_error.close()
file_result.close()
