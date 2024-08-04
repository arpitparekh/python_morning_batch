from reportlab.pdfgen import canvas

c = canvas.Canvas("reportlab_pdf.pdf")
c.drawString(500,500,"Hello World")
c.drawString(400,400,"Hello Krishna")
c.showPage()
c.save()