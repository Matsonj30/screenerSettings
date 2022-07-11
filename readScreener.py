
import requests
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Color, Fill, Font
from datetime import date


#returns the right most column in the excel sheet which is blank
#this is where we will start inputting new tickers found for the day
def startPoint(sheetWrite):
    startingPoint = 0
    colNumber = 1
    while sheetWrite.cell(row = 1, column = colNumber).value != None:
        colNumber += 1
    return colNumber

#retrieves finviz screener data 
def finvizData():
    sheet = load_workbook("D:/Programming/Repositories/screenerSettings/highVolumeTickers.xlsx")
    sheetWrite = sheet.worksheets[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    urls = ['https://finviz.com/screener.ashx?v=111&f=sh_float_u100,sh_relvol_o10&ft=4&o=volume',"https://finviz.com/screener.ashx?v=111&f=sh_float_u100,sh_relvol_o10&ft=4&o=volume&r=21"]
    
    for url in urls:
        screenerPage = requests.get(url, headers = headers).text
        tables = pd.read_html(screenerPage)
        tables = tables[-2] #this is the table we want from the many tables pandas read
        names = tables.iloc[1:, 1]
        industry = tables.iloc[1:, 4]
        marketCap = tables.iloc[1:,6]
        price = tables.iloc[1:,8]
        change = tables.iloc[1:,9]
        volume = tables.iloc[1:,10]

        startingPoint = startPoint(sheetWrite)
        tempStartPoint = startingPoint
        index = 1

        for name in names:
            sheetWrite.cell(row = 1, column = tempStartPoint).value = names[index] ##iterate each thing here
            sheetWrite.cell(row = 2, column = tempStartPoint).value = industry[index] ##iterate each thing here
            sheetWrite.cell(row = 3, column = tempStartPoint).value = date.today() ##iterate each thing here
            sheetWrite.cell(row = 4, column = tempStartPoint).value = volume[index] ##iterate each thing here
            sheetWrite.cell(row = 5, column = tempStartPoint).value = marketCap[index] ##iterate each thing here
            sheetWrite.cell(row = 6, column = tempStartPoint).value = price[index] ##iterate each thing here
            sheetWrite.cell(row = 7, column = tempStartPoint).value = change[index] ##iterate each thing here
    

            tempStartPoint += 1
            index += 1
        sheet.save(("D:/Programming/Repositories/screenerSettings/highVolumeTickers.xlsx"))
        