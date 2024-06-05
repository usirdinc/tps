import os 
import base64
from flask import Flask, request, jsonify
from pypdf import PdfReader
from io import BytesIO

app = Flask(__name__)

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

    return {
        "name": name,
        "location": address,
        "date": date,
        "time": time
    }

@app.route('/process', methods=['POST'])
def process_pdf():
    try:
        data = request.json
        pdf_base64 = data['file']
        pdf_bytes = base64.b64decode(pdf_base64)
        pdf_file = BytesIO(pdf_bytes)
        result = provideData(pdf_file)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
