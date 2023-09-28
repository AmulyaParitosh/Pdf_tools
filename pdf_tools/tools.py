from io import BufferedReader
from pathlib import Path
from typing import Iterable
import PyPDF2

MERGER = PyPDF2.PdfMerger()

pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

for pdf_file in pdf_files:
    MERGER.append(pdf_file)

MERGER.write("merged.pdf")

MERGER.close()

def file_objs(paths: list[str]) -> Iterable[BufferedReader]:
    return [Path(path).open('rb') for path in paths]

def merge(files: Iterable[BufferedReader]):...
