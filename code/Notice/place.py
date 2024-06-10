import os
import shutil
from pypdf import PdfReader

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def extract_data(file, split_key, name_indices, name_separator=",", name_position=-1, prefix=""):
    try:
        pdf = PdfReader(file)
        page_text = pdf.pages[0].extract_text()
        split_text = page_text.split(split_key)[1]
        name_section = split_text.split("\n")[name_position].split(name_separator)
        name = " ".join([name_section[i].title() for i in name_indices]).strip()
        filename = f"{prefix} - {name}.pdf"
        return name, filename
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        return None, None

functions = [
    lambda file: extract_data(file, "Alien Number Name", range(1, 0, -1), name_position=1, prefix="Receipt Notice"),
    lambda file: extract_data(file, "ACCOUNT NUMBER USCIS A#", [4], prefix="Biometrics Appointment"),
    lambda file: extract_data(file, "Executive Office for Immigration Review\n", [0], name_separator="\n", prefix="I589"),
    lambda file: extract_data(file, "matter.", [-1], name_separator="AM" if "AM" in PdfReader(file).pages[0].extract_text() else "PM", prefix="Interview Notice")
]

keyWords = ["Notice Type: Receipt Notice", "FOR BIOMETRICS SUBMISSION, YOU MUST BRING", "Do you also want to apply for", "Interview on eligibility for asylum and withholding of removal (Form I-589)OFFICE"]
folderNames = ["Receipt Notice", "Biometrics Appointment", "I-589", "Interview Notice"]

def finalize(group, file, index):
    if not group[0] or not group[1]:
        print(f"Skipping file {file} due to extraction errors.")
        return
    os.makedirs(folderNames[index], exist_ok=True)
    shutil.move(file, os.path.join(folderNames[index], group[1]))

files = [file for file in os.listdir() if file.endswith(".pdf")]

def __main__(files):
    for file in files:
        text = PdfReader(file).pages[0].extract_text()
        for i, keyWord in enumerate(keyWords):
            if keyWord in text:
                finalize(functions[i](file), file, i)
                break

__main__(files)
