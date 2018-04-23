import requests

array=[
  "https://pdf.usaid.gov/pdf_docs/PA00MQ21.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00K389.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00J821.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00HXDX.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1H.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ26.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ23.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1N.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ24.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ27.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1S.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SXJW.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1V.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MT3Q.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ25.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1X.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1G.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SXQQ.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MQ1P.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00K5CD.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SXXC.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00KZBM.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SSKB.pdf",
  "https://pdf.usaid.gov/pdf_docs/PNADC916.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00KT8F.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00M35C.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MT2H.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MT2J.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SS6C.pdf",
  "https://pdf.usaid.gov/pdf_docs/PNADE355.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MM1F.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MM1D.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MM19.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MM1C.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00N53F.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00M45K.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SXJ6.pdf",
  "https://pdf.usaid.gov/pdf_docs/PDACR715.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00N78Q.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00JMWC.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00SV58.pdf",
  "https://pdf.usaid.gov/pdf_docs/PNADQ895.pdf",
  "https://pdf.usaid.gov/pdf_docs/PDABX568.pdf",
  "https://pdf.usaid.gov/pdf_docs/PNABW920.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00K3G1.pdf",
  "https://pdf.usaid.gov/pdf_docs/PNADQ102.pdf",
  "https://pdf.usaid.gov/pdf_docs/PNADE353.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00JXR1.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00MXNG.pdf",
  "https://pdf.usaid.gov/pdf_docs/PA00M1HD.pdf"
]

for url in array:
    if url.find('/'):
        fileName= url.rsplit('/', 1)[1]

    r = requests.get(url)
    with open(fileName, "wb") as code:
        code.write(r.content)
#url="https://pdf.usaid.gov/pdf_docs/PDAAJ649.pdf"
#if url.find('/'):
#    fileName= url.rsplit('/', 1)[1]
#r = requests.get(url)
#with open(fileName, "wb") as code:
#    code.write(r.content)
