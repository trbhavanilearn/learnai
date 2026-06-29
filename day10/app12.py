from pypdf import PdfReader

pdf_path = "Sachin.pdf"

reader = PdfReader(pdf_path)
print("Metadata:", reader.metadata)

text = ""

for i, page in enumerate(reader.pages):
    text += page.extract_text() + "\n"

print(text)