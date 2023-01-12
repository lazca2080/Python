"""
날짜 : 2023/01/11
이름 : 박종협
내용 : 파이썬 외부 패키지모듈 실습하기
"""

from openpyxl import Workbook

# 새로운 엑셀파일 생성
workbook = Workbook()

# 첫벌째 시트 활성화
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '파이썬 엑셀 실습'
sheet.append(['a101', '김유신', '010-1234-1001', '25', '부산시'])
sheet.append(['a102', '김춘추', '010-1234-1002', '22', '부산시'])
sheet.append(['a103', '장보고', '010-1234-1003', '33', '부산시'])
sheet.append(['a104', '강감찬', '010-1234-1004', '44', '부산시'])
sheet.append(['a105', '이순신', '010-1234-1005', '45', '부산시'])

# 저장닫기
workbook.save('C:/Users/java2/Desktop/member.xlsx')
workbook.close()

print('프로그램 종료...')

