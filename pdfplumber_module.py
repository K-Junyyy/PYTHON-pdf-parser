import pdfplumber

text =""
with pdfplumber.open("./21_391_13.pdf") as pdf:
    print("총 페이지는 ",len(pdf.pages))
    for i in range(len(pdf.pages)):
        now_page = pdf.pages[i]
        text += now_page.extract_text()

attendanceStart = text.find("출석 의원")
attendanceEnd = text.find("국회 참석자")
attendance = text[attendanceStart:attendanceEnd]

def extractAttendance(str):
    start = attendance.find(str)
    result = attendance[start:]
    end = result.find("◯")
    print(result[:end])

extractAttendance("출석 의원")