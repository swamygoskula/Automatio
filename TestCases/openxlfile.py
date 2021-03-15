from openpyxl import workbook

wb=workbook()
wb['Sheet'].title="report automation"
sh1=wb.active
sh1['A1'].value="name"
sh1['B1'].value="status"
sh1['A2'].value="python"
sh1['B2'].value="active"

wb.save("finalreport.slsx")