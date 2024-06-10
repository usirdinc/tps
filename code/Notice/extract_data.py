from pypdf import PdfReader
import os

data = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
family = []

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

    if(len(data.split("\n")) > 2):
        familymembers = []
        for familymember in data.split("\n"):
            familymember = familymember.split(" ")
            familymember.pop()
            familymembers.append(" ".join(familymember))
        familymembers.pop()
        family.append(familymembers)

    return {"name": name, "alien_number": aNumbers[0]}

os.chdir("Biometrics Appointment")
extract_biometrics_appointment_data(os.listdir()[6])