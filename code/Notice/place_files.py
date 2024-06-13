import os
import shutil
from pypdf import PdfReader

def place_biometrics_appointment(file):
    try:
        pdf = PdfReader(file)
        page_text = pdf.pages[0].extract_text()
        name_section = page_text.split("ACCOUNT NUMBER USCIS A#")[1]
        name = name_section.split("PLEASE READ THIS ENTIRE NOTICE CAREFULLY.")[0].strip().split("\n")[4].title()
        filename = f"Biometrics Appointment - {name}.pdf"
        return name, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None

def place_receipt_notice(file):
    try:
        pdf = PdfReader(file)
        pdf_text = pdf.pages[0].extract_text()
        array = pdf_text.split("Alien Number Name")[1].split("Please see")[0].split('\n')[1].split(" ")
        array.reverse()
        array.pop()
        array.pop()
        array.pop()
        array.reverse()
        name = []
        index = 1
        while (index < len(array)):
            name.append(f"{array[index]}")
            index+=1
        name.append(array[0])
        name = " ".join(name).replace(",","").title()
        filename = f"Receipt Notice - {name}.pdf"
        return name, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None

def place_i589(file):
    try:
        pdf = PdfReader(file)
        page_text = pdf.pages[0].extract_text()
        main_text = page_text.split("Executive Office for Immigration Review\n")[1].split("Applicant:")[0].split("\n")[0].removesuffix(" ")
        names = [main_text]
        name = names[0]
        filename = f"I589 - {names[0]}.pdf"
        return name, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None

def place_interview(file):
    try:
        pdf = PdfReader(file)
        data = pdf.pages[0].extract_text()
        name = data.split("matter.")[1].split("\n")[1]
        timezone = 'PM'
        if('AM' in name): timezone = 'AM'
        name = name.split(timezone)[1].split(',')
        name.reverse()
        name = " ".join(name).title()
        filename = f"Interview Notice - {name}.pdf"
        return name, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None

functions = [place_receipt_notice, place_biometrics_appointment, place_i589, place_interview]
keyWords = ["Notice Type: Receipt Notice", "FOR BIOMETRICS SUBMISSION, YOU MUST BRING", "Do you also want to apply for", "Interview on eligibility for asylum and withholding of removal (Form I-589)OFFICE"]
folderNames = ["Receipt Notice", "Biometrics Appointment", "I-589", "Interview Notice"]

def finalize(group, file, index):
    if not group[0] or not group[1]:
        print(f"Skipping file {file} due to extraction errors.")
        return

    if not os.path.exists(folderNames[index]):
        os.mkdir(folderNames[index])

    new_location = os.path.join(folderNames[index], group[1])
    shutil.move(file, new_location)

files = [file for file in os.listdir() if file.endswith(".pdf")]

def __main__(files):
    for file in files:
        for keyWord in keyWords:
            if PdfReader(file).pages[0].extract_text().find(keyWord) != -1:
                finalize(functions[keyWords.index(keyWord)](file), file, keyWords.index(keyWord))
                break

os.chdir("Notice")
__main__(files)