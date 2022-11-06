
from openpyxl import Workbook
import csv

wb = Workbook()
wb.create_sheet(title='home_19', index=0)
wb.remove(wb['Sheet'])
ws = wb['home_19']
with open('home_18.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('home_19.xlsx')
ws.delete_cols(3)
wb.save('home_19.xlsx')

