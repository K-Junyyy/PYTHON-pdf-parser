from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def read_pdf(file_name):
    output_string = StringIO()
    with open(file_name, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue()

text = read_pdf("./21_391_13.pdf")

attendanceStart = text.find("출석  의원")
attendanceEnd = text.find("국회  참석자")
attendance = text[attendanceStart:attendanceEnd]

def extractAttendance(str):
    start = attendance.find(str)
    result = attendance[start:]
    end = result.find("◯")
    return result[:end]

tmp = extractAttendance("출석  의원")
print(tmp)