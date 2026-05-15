from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

class ReportGenerator:
    def generate(self, findings):
        doc = SimpleDocTemplate("security_report.pdf")
        styles = getSampleStyleSheet()

        elements = []

        for finding in findings:
            elements.append(
                Paragraph(str(finding), styles['BodyText'])
            )

        doc.build(elements)