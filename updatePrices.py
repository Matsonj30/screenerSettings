from logging import exception
from openpyxl import load_workbook
import yfinance
import openpyxl
from yahoo_fin.stock_info import *
from datetime import date
from readScreener import finvizData
sheet = load_workbook("D:/Programming/Repositories/screenerSettings/highVolume.xlsx")
sheetWrite = sheet.worksheets[0] #starting point??
index = 2
while(sheetWrite.cell(row = index, column=1).value != None):
    if(sheetWrite.cell(row = index, column=21).value == None): #checking to see if we need to update this ticker anymore
        for cellXIndex in range(14):
            if(sheetWrite.cell(row = index, column = 8 + cellXIndex).value == None):
                sheetWrite.cell(row = index, column = 8 + cellXIndex).value = round(get_live_price(sheetWrite.cell(row = index, column=1).value),3) #get live price of company, rounded 3 decimal spots
                break
    index += 1


sheet.save("D:/Programming/Repositories/screenerSettings/highVolume.xlsx")
finvizData()