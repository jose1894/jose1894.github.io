from pathlib import Path
from pypdf import PdfReader

pdf_path = Path(__file__).parent.parent / 'es' / 'CV-ATS-ES-SEPT-2025.pdf'
if not pdf_path.exists():
    print(f'ERROR: PDF no encontrado en {pdf_path}')
    raise SystemExit(1)

reader = PdfReader(str(pdf_path))
texts = []
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    texts.append(f'--- PAGE {i} ---\n' + (text or ''))

print('\n'.join(texts))
