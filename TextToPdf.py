from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=15)

f = open("myfile.txt", "r")

for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='L')

pdf.output("mygfg.pdf")