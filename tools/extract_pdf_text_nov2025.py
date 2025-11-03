#!/usr/bin/env python3
"""Extrae texto de es/cv_ats-es-nov-2025.pdf a tools/cv_nov2025.txt

Requiere: pypdf (pip install pypdf)
"""
from pathlib import Path
try:
    from pypdf import PdfReader
except Exception as e:
    raise SystemExit("pypdf no está disponible. Instala con: python -m pip install pypdf")

pdf_path = Path(__file__).resolve().parent.parent / 'es' / 'cv_ats-es-nov-2025.pdf'
out_path = Path(__file__).resolve().parent / 'cv_nov2025.txt'

if not pdf_path.exists():
    raise SystemExit(f"PDF no encontrado en: {pdf_path}")

reader = PdfReader(str(pdf_path))
all_text = []
for page in reader.pages:
    try:
        text = page.extract_text()
    except Exception:
        text = None
    if text:
        all_text.append(text)

out_path.write_text("\n\n".join(all_text), encoding='utf-8')
print(f"Texto extraído a: {out_path}")
