import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader(r"VF505_V3_R7_P520MY.pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "Ignition Working Conditions Table"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    ResSearch = re.search(String, Text)
    if ResSearch != None:
        print(ResSearch)
        a=i+1
        print("Page Number = " + str(a))