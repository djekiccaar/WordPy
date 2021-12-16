import tabula

pdf_path="VF505_V3_R7_P520MY.pdf"

dfs=tabula.read_pdf(pdf_path,pages='17')

print(dfs[0])
