# Document Loader
#import libraries
import PyPDF2
import re

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text
    

if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('data/meeting_minutes.pdf')
    risk_count = 0
    for text in extracted_text:
        split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())

        if 'risk' in split_message:
            risk_count += 1

        print("Risks found:", risk_count)

# TODO:
    # pull text from pdf

    # pull text from word doc (DOCX)

    # pull text from plain text or email file