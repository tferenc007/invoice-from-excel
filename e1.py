import glob 
from fpdf import FPDF
from pathlib import Path
import pandas as pd

file_paths = glob.glob("e1/*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_font(family='Times', size=16, style='B')

for file_path in file_paths:
    file_name = Path(file_path).stem
    pdf.add_page()
    pdf.cell(w=0, h=12, txt=file_name.title(), ln=1)
    with open(file_path) as f:
        names = f.read()

    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=names)

pdf.output("animals.pdf")


