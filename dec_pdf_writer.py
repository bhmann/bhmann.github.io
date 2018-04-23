import requests

array=["PDAAJ649","PDAAJ447","PNAAD299","PNAAK119"]
for x in array
    url = "https://pdf.usaid.gov/pdf_docs/"+ x +".pdf"

    if url.find('/'):
        fileName= url.rsplit('/', 1)[1]

# download the file contents in binary format
    r = requests.get(url)

# open method to open a file on your system and write the contents
    with open(fileName, "wb") as code:
        code.write(r.content)
