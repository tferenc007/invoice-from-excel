from ctypes import alignment
import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path

file_paths = glob.glob("invoices/*xlsx")
# print (file_paths)

for file_path in file_paths:
    
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    file_name = Path(file_path).stem
    invoice_nr, invoice_date = file_name.split("-")

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr.{invoice_nr}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Date: {invoice_date}', ln=2)

    df = pd.read_excel(file_path, sheet_name="Sheet 1")
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family='Times', size=12, style='B' )
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
    total_price = df["total_price"].sum()
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8,txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)

    pdf.set_font(family='Times', size=14, style='B' )
    pdf.cell(w=30, h=8, txt=f"The total prive is {total_price}", ln=1)

    pdf.set_font(family='Times', size=14, style='B' )
    pdf.cell(w=25, h=8, txt='PythonHow')
    pdf.image("pythonhow.png", w=10)



pdf.output("invoices.pdf")