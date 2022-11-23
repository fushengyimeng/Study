import xlrd


xlsx = xlrd.open_workbook('simple2.xls')

sheet1 = xlsx.sheets()[0]

print(sheet1.row_values(0))