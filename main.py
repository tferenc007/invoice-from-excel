from sys import path_hooks
from turtle import left
import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path

file_paths = glob.glob("invoices/*xlsx")
# print (file_paths)

for file_path in file_paths:
    df=pd.read_excel(file_path, sheet_name=None)

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    file_name = Path(file_path).stem
    invoice_nr = file_name.split("-")[0]
    pdf.set_font(family='Times', size=16, style='B')

    pdf.cell(w=50, h=8, tex='Invoice nr.')