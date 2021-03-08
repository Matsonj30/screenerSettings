from openpyxl import load_workbook
import yfinance
import openpyxl
from yahoo_fin import stock_info
from datetime import date


print(stock_info.get_live_price("BWEN"))
info = yfinance.Ticker("BWEN")
print(info.info["dayHigh"]) #can get anything using the brackets, we want to track its highs for the day
print(info.info)

sheet = load_workbook("D:/Programming/Python/projects/ScreenerUpdates/ScreenerTest.xlsx")
sheetAlter = sheet.worksheets[0] #starting point??

#goes through the spreadsheet and looks for the right most column thats open, then inserts the date there, and returns the column starting point
def setDate():
    startingPoint = 0
    while sheetAlter.cell(row = 1, column = 8 + startingPoint).value is not None:
        startingPoint += 1
    sheetAlter.cell(row = 1, column = 8 + startingPoint).value = date.today()
    return startingPoint

columnVal = setDate() + 8 #curval we want to check for the day
curRow = 3

while sheetAlter.cell(row = curRow, column = 1).value is not None:
    sheetAlter.cell(row = curRow, column = columnVal).value = stock_info.get_live_price(sheetAlter.cell(row = curRow, column = 1).value)
    curRow += 1



sheet.save("D:/Programming/Python/projects/ScreenerUpdates/ScreenerTest.xlsx")