from PyPDF2 import PdfFileReader, PdfFileWriter

watermark = PdfFileReader("wtr.pdf").getPage(0)
reader = PdfFileReader("merged.pdf")
writer = PdfFileWriter()
watermarked_pdf = "merged_wtr.pdf"

for i in range(reader.getNumPages()):
    pdf_page = reader.getPage(i)
    pdf_page.mergePage(watermark)
    writer.addPage(pdf_page)

    with open(watermarked_pdf, "wb") as file:
        writer.write(file)