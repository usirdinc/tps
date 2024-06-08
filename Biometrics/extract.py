import os
import shutil
from pypdf import PdfReader

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def extract_biometrics_appointment(file):
    try:
        pdf = PdfReader(file)
        page_text = pdf.pages[0].extract_text()

        # Extracting the applicant's name
        try:
            name_section = page_text.split("ACCOUNT NUMBER USCIS A#")[1]
            name = name_section.split("PLEASE READ THIS ENTIRE NOTICE CAREFULLY.")[0].strip().split("\n")[4].title()
        except IndexError:
            raise ValueError("Error extracting name from the PDF.")

        # Extracting the location and date/time of appointment
        try:
            main_text = page_text.split("APPLICATION SUPPORT CENTER")[1].split("WHEN")[0].split("DATE AND TIME OF APPOINTMENT\n")
            location = main_text[0].replace("  ", " ").replace("\n", " ").strip()
            date_raw = main_text[1].split("\n")[0]
            date = f"{months[int(date_raw.split('/')[0]) - 1]} {date_raw.split('/')[1].lstrip('0')}, {date_raw.split('/')[2]}"
            time = main_text[1].split("\n")[1]
        except IndexError:
            raise ValueError("Error extracting appointment details from the PDF.")

        data = f"Location: {location}\nDate: {date}\nTime: {time}\n"
        filename = f"Biometrics Appointment - {name}.pdf"

        return name, data, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None, None

def extract_receipt_notice(file):
    try:
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
        filename = "Receipt Notice - " + names[0] + ".pdf"

        return names[0], data, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None, None

def extract_i589(file):
    try:
        pdf = PdfReader(file)
        page_text = pdf.pages[0].extract_text()
        data = "i-589"
        main_text = page_text.split("Executive Office for Immigration Review\n")[1].split("Applicant:")[0].split("\n")[0].removesuffix(" ")
        names = [main_text]
        filename = f"I589 - {names[0]}.pdf"
        return names[0], data, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None, None

functions = [extract_receipt_notice, extract_biometrics_appointment, extract_i589]
keyWords = ["Notice Type: Receipt Notice", "WHEN YOU APPEAR AT THE ASC FOR BIOMETRICS SUBMISSION, YOU MUST BRING", "Do you also want to apply for withholding of removal under the Convention Against Torture?"]
folderNames = ["Receipt Notice", "Biometrics Appointment", "I-589"]
families = []

def finalize(group, file, index):
    if not group[0] or not group[1] or not group[2]:
        print(f"Skipping file {file} due to extraction errors.")
        return

    if not os.path.exists(folderNames[index]):
        os.mkdir(folderNames[index])

    if index == 0 and len(group[1].split("\n")) > 2:
        memberArray = []
        members = group[1].split("\n")
        members.pop()
        for member in members:
            name = []
            member = member.split(" ")
            member.pop()
            for word in member:
                name.append(word)
            name = " ".join(name)
            memberArray.append(name)
        families.append(memberArray)
    
    new_location = os.path.join(folderNames[index], group[2])
    shutil.move(file, new_location)

files = [file for file in os.listdir() if file.endswith(".pdf")]

def __main__(files):
    for file in files:
        for keyWord in keyWords:
            if PdfReader(file).pages[0].extract_text().find(keyWord) != -1:
                finalize(functions[keyWords.index(keyWord)](file), file, keyWords.index(keyWord))
                break
    for family in families:
        for member in family:
            for name in (os.listdir("./Biometrics Appointment")):
                index = os.listdir("./Biometrics Appointment").index(name)
                originalName = name
                name = name.split("- ")[1].split(".pdf")[0]
                if(name == member):
                    if not os.path.exists(f"./Biometrics Appointment/Biometrics Appointments - {family[0]}"):
                        os.mkdir(f"./Biometrics Appointment/Biometrics Appointments - {family[0]}")
                    shutil.move(
                        os.path.join("./Biometrics Appointment", os.listdir("./Biometrics Appointment")[index]),
                        os.path.join(f"./Biometrics Appointment",f"Biometrics Appointments - {family[0]}", f"{originalName}")
                    )
                break

__main__(files)



