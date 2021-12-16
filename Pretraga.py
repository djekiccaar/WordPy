import PyPDF2
import re

# Open the pdf file
object = PyPDF2.PdfFileReader(r"VF505_V3_R7_P520MY.pdf")

# Get number of pages
NumPages = object.getNumPages()

# Enter code here
String = "Ignition Working Conditions Table"

# Extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    if re.search(String,Text):
         print("Pattern Found on Page: " + str(i))