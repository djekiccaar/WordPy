from tabula import read_pdf, convert_into

pdf_file="VF505_V3_R7_P520MY.pdf"
#list all tables
tables = read_pdf(pdf_file, pages='all')

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