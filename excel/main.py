from openpyxl import Workbook

wb = Workbook()
ws = wb.active 
ws.title = "Grades"

ws.append(["Name", "Score"])

ws.append(["Ayan", 95])
ws.append(["Dana", 85])

ws.save("grades.xlsx")
print("Файл был создан")