import os
import shutil
from pypdf import PdfReader
    
os.chdir("Notice")
families = []

os.chdir("Receipt Notice")
for file in os.listdir():
    text = PdfReader(file).pages[0].extract_text()
    mainData = text.split("Applicant(s):\nAlien Number Name")[1].split("\nPlease see the additional")[0].split("\n")
    if '' in mainData:
        mainData.remove('')
    if ' ' in mainData:
        mainData.remove(" ")
    if len(mainData) > 1:
        family = []
        for item in mainData:
            item = item.split(" ")
            aNumber = "".join([item[0],item[1],item[2]])
            name = []
            count = 4
            while count < len(item):
                name.append(item[count])
                count+=1
            name.append(item[3])
            name = " ".join(name).replace(",","").title()
            family.append(name)
        families.append(family)

os.chdir("../Biometrics Appointment")

for family in families:
    if not os.path.exists(f"Biometrics Appointment - {family[0]}"):
        os.mkdir(f"Biometrics Appointment - {family[0]}")
    for familyMember in family:
        original_path = f"Biometrics Appointment - {familyMember}.pdf"
        new_path = os.path.join(f"Biometrics Appointment - {family[0]}",f"Biometrics Appointment - {familyMember}.pdf")
        if os.path.exists(original_path):
            shutil.move(original_path, new_path)

for file in os.listdir():
    if not file.endswith('.pdf'):
        if len(os.listdir(file)) == 0:
            os.removedirs(file)