from tika import parser

pdf_path = "./21_391_11.pdf" 

# PDF 파일에서 텍스트를 추출
raw_pdf = parser.from_file(pdf_path) 
contents = raw_pdf['content']
contents = contents.strip()

print(contents)

attendanceStart = contents.find("출석 의원")
attendanceEnd = contents.find("국회 참석자")
attendance = contents[attendanceStart:attendanceEnd]

def extractAttendance(str):
    start = attendance.find(str)
    result = attendance[start:]
    end = result.find("◯")
    return result[:end]

tmp = extractAttendance("출석 의원")
# print(tmp.split())