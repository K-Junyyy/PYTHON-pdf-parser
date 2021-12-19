import pdftotext

filename = "./21_391_13.pdf"

with open(filename, "rb") as f:
    pdf = pdftotext.PDF(f)

for page in pdf:
    print(page)

