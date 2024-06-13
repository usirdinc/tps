from pypdf import PdfReader
import os
import json

data = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
family = []
dataFamily = {}
os.chdir("Notice")
def extract_biometrics_appointment_data(file):
    name = str(file).split("Biometrics Appointment - ")[1].split(".pdf")[0]
    pdf = PdfReader(file)
    page_text = pdf.pages[0].extract_text()
    main_text = page_text.split("APPLICATION SUPPORT CENTER")[1].split("WHEN")[0].split("DATE AND TIME OF APPOINTMENT\n")
    aNumber = "".join(page_text.split("USCIS A#")[1].split("CODE")[0].split("\n")[1].split(" "))
    location = main_text[0].replace("  ", " ").replace("\n", " ").strip()
    date_raw = main_text[1].split("\n")[0]
    date = f"{months[int(date_raw.split('/')[0]) - 1]} {date_raw.split('/')[1].lstrip('0')}, {date_raw.split('/')[2]}"
    time = main_text[1].split("\n")[1]
    return {"name": name, "biometrics_location": location, "biometrics_date": date, "biometrics_time": time, "alien_number": aNumber}

def extract_receipt_notice_data(file):
    name = str(file).split("Receipt Notice - ")[1].split(".pdf")[0]
    originalName = str(file).split("Receipt Notice - ")[1].split(".pdf")[0]
    pdf = PdfReader(file)
    page_text = pdf.pages[0].extract_text()
    data = ""
    aNumbers = []
    names = []

    main_text = page_text.split("Applicant(s):\nAlien Number Name")[1].split("\nPlease see the additional")[0].split("\n")
    for main_line in main_text:
        if len(main_line) > 1:
            aNumber = "".join([main_line.split(" ")[0], main_line.split(" ")[1], main_line.split(" ")[2]])
            name_array = main_line.split(main_line.split(" ")[2] + " ")[1].split(", ")
            aNumbers.append(aNumber)
            names.append(name_array[1].title() + " " + name_array[0].title())

    for name in names:
        data += name + " " + aNumbers[names.index(name)] + "\n"

    hasFamily = False

    if(len(data.split("\n")) > 2):
        familymembers = []
        for familymember in data.split("\n"):
            familymember = familymember.split(" ")
            familymember.pop()
            familymembers.append(" ".join(familymember))
        familymembers.pop()
        family.append(familymembers)
        hasFamily = True
        dataFamily[originalName] = {}
        for familymember in familymembers:
            dataFamily[originalName][familymember] = {}
            dataFamily[originalName][familymember]["alien_number"] = aNumbers[familymembers.index(familymember)]
            dataFamily[originalName][familymember]["name"] = familymember
            dataFamily[originalName][familymember]["biometrics_date"] = "No Biometrics Yet"
            dataFamily[originalName][familymember]["biometrics_location"] = "No Biometrics Yet"
            dataFamily[originalName][familymember]["biometrics_time"] = "No Biometrics Yet"

    return {"name": name, "alien_number": aNumbers[0], "hasFamily": hasFamily}

def extract_interview_notice_data(file):
    name = str(file).split("Interview Notice - ")[1].split(".pdf")[0]
    pdf = PdfReader(file)
    page_text = pdf.pages[0].extract_text()
    addressList = page_text.split("Interview")[0].split("\n")  
    alien_number = f"A{page_text.split("A Number: ")[1].split("ASYLUM")[0].split("\n")[0].split(" ")[0]}"
    mainText = page_text.split("matter.")[1].split("Sincerely")[0].split("\n")[1]

    address = " ".join([addressList[1],addressList[2],addressList[3]])
    if(mainText.__contains__("PM")):
        splitter = "PM"
    else:
        splitter = "AM"

    array = mainText.split(splitter)[0].split(" ")
    time = array[5] + " " + splitter
    array.pop()
    array.pop()
    date = " ".join(array)
    return {"name": name, "alien_number": alien_number, "interview_date": date, "interview_time": time, "interview_location": address}

os.chdir("Receipt Notice")
for file in os.listdir():
    dataParts = extract_receipt_notice_data(file)
    data[dataParts["alien_number"]] = dataParts
    data[dataParts["alien_number"]]["biometrics_date"] = "No Biometrics Yet"
    data[dataParts["alien_number"]]["biometrics_location"] = "No Biometrics Yet"
    data[dataParts["alien_number"]]["biometrics_time"] = "No Biometrics Yet"
    data[dataParts["alien_number"]]["hasFamily"] = False
    data[dataParts["alien_number"]]["interview_date"] = "No Interview Yet"
    data[dataParts["alien_number"]]["interview_time"] = "No Interview Yet"
    data[dataParts["alien_number"]]["interview_location"] = "No Interview Yet"
os.chdir("../")

os.chdir("Biometrics Appointment")
for file in os.listdir():

    if(file.endswith(".pdf")):
        dataParts = extract_biometrics_appointment_data(file)
        data[dataParts["alien_number"]] = dataParts
        data[dataParts["alien_number"]]["hasFamily"] = False
        data[dataParts["alien_number"]]["interview_date"] = "No Interview Yet"
        data[dataParts["alien_number"]]["interview_time"] = "No Interview Yet"
        data[dataParts["alien_number"]]["interview_location"] = "No Interview Yet"

    elif(file.startswith("Biometrics Appointment") and not file.endswith(".pdf")):
        os.chdir(file)
        familyData = {}
        mainPerson = file.split("- ")[1]
        for familyMember in os.listdir():
            dataParts = extract_biometrics_appointment_data(familyMember)
            familyData[dataParts["name"]] = dataParts
            if(dataParts["name"] == mainPerson):
                data[dataParts["alien_number"]] = dataParts
                data[dataParts["alien_number"]]["hasFamily"] = True
                data[dataParts["alien_number"]]["interview_date"] = "No Interview Yet"
                data[dataParts["alien_number"]]["interview_time"] = "No Interview Yet"
                data[dataParts["alien_number"]]["interview_location"] = "No Interview Yet"
        dataFamily[mainPerson] = familyData
        os.chdir("../")

os.chdir("../")
os.chdir("Interview Notice")

for file in os.listdir():
    dataParts = extract_interview_notice_data(file)
    data[dataParts["alien_number"]]["interview_date"] = dataParts["interview_date"]
    data[dataParts["alien_number"]]["interview_time"] = dataParts["interview_time"]
    data[dataParts["alien_number"]]["interview_location"] = dataParts["interview_location"]

os.chdir("../")
os.chdir("../")
with open("data.json","w") as json_file:
    json.dump(data, json_file, indent=4, sort_keys=True)
with open("family.json","w") as json_file:
    json.dump(dataFamily, json_file, indent=4, sort_keys=True)