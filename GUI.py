from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tabula import read_pdf, convert_into

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)



#list all tables
tables = read_pdf(filename, pages='17')

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