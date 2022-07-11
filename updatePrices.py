from logging import exception
from openpyxl import load_workbook
import yfinance
import openpyxl
from yahoo_fin.stock_info import *
from datetime import date
from readScreener import finvizData
sheet = load_workbook("D:/Programming/Repositories/screenerSettings/highVolumeTickers.xlsx")
sheetWrite = sheet.worksheets[0] #starting point??
index = 2
print("HEREWTF")

while(sheetWrite.cell(row = 1, column=index).value != None):
    if(sheetWrite.cell(row = 20, column=index).value == None): #checking to see if we need to update this ticker anymore
        for cellYIndex in range(13):
            if(sheetWrite.cell(row = 8 + cellYIndex, column=index).value == None):
                sheetWrite.cell(row = 8 + cellYIndex, column=index).value = round(get_live_price(sheetWrite.cell(row = 1, column=index).value),3) #get live price of company
                break
    index += 1


sheet.save("D:/Programming/Repositories/screenerSettings/highVolumeTickers.xlsx")
finvizData()