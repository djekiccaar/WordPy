from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tabula import read_pdf, convert_into
import PyPDF2
import re


filename = PyPDF2.PdfFileReader(r"VF505_V3_R7_P520MY.pdf")
NumPages = filename.getNumPages()
String = "Ignition Working Conditions Table"

def Pretraga(filename):
    NumPages = filename.getNumPages()
    for i in range(0, NumPages):
        PageObj = filename.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch != None:
            print(ResSearch)
            a=i+1
            print("Page Number = " + str(a))
    return a

#list all tables
pages=Pretraga(filename)
print(pages)
tables = read_pdf(r"VF505_V3_R7_P520MY.pdf", pages=str(pages))

table_number =1

for table in tables:
    #remove Nan columns
    table = table.dropna(axis="columns")

    if not table.empty:
        print(f"Table {table_number}")
        print(table)

        #convert the table dataframe into csv file
        table.to_csv(f'table{table_number}.csv')

        table_number += 1