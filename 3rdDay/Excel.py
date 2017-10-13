import xlwt


wb = xlwt.Workbook()
ws =wb.add_sheet("Sachin1")

#in python cells are referred with row and then column with 0 as starting
#in excel cells are referred with colum and then row for.e.g A1
ws.write(0,0,'test')
ws.write(2,0,199)

for x in range(10):
    ws.write(5,x,x*x)

wb.save('example.xls')    
