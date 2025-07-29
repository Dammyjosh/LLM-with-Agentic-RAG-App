import os
import markdown2
from fpdf import FPDF
import re

def generate_markdown_report(summaries, filename="reports/ai_report.md"):
    os.makedirs("reports", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 🧠 Insight Report\n\n")
        for i, item in enumerate(summaries, 1):
            f.write(f"## {i}. {item['title']}\n")
            f.write(f"**URL**: {item['url']}\n\n")
            f.write(f"{item['summary']}\n\n")
    return filename

def remove_unicode(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)



def convert_md_to_pdf(md_file, pdf_file="reports/ai_report.pdf"):
    with open(md_file, "r", encoding="utf-8") as f:
        html = markdown2.markdown(f.read())

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in html.splitlines():
        clean_line = remove_unicode(line)  # 👈 Remove emojis and other Unicode
        pdf.multi_cell(0, 10, clean_line)

    pdf.output(pdf_file)
    return pdf_file





import re

def remove_unicode(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)
