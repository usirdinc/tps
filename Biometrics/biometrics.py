import os
from pypdf import PdfReader

def provideData(file):           
    reader = PdfReader(file)
    rawnames = reader.pages[0].extract_text().split("CODE")[1].split("PLEASE")[0].split("\n")[4].split(" ")
    name = []
    for rawname in rawnames:
        rawname = rawname.capitalize()
        name.append(rawname)
    name = " ".join(name)

    data = reader.pages[0].extract_text().split("APPLICATION SUPPORT CENTER")[1].split("WHEN")[0].split("\n")

    address = " ".join([data[1],data[2],data[3].split("DATE")[0]]).replace("  "," ")
    date = data[4]
    time = data[5]

    print("\nName: ",name,"\nLocation: ", address, "\nDate: ", date, "\nTime: ", time,"\n") 

dir_path = os.path.dirname(os.path.realpath(__file__))


for root, dirs, files in os.walk(dir_path):
    for file in files: 
 
        if file.startswith('Biometric'):
            provideData(file)