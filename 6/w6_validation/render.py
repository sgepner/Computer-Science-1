#!/usr/bin/env python3
"""Export clean notebook for local browser visual inspection (branch only)."""
from pathlib import Path
import nbformat
from nbconvert import HTMLExporter
p=Path(__file__).resolve().parents[1]/'Wykład 6.ipynb'
nb=nbformat.read(p,as_version=4)
exporter=HTMLExporter(template_name='lab')
exporter.exclude_input_prompt=True
exporter.exclude_output_prompt=True
html,_=exporter.from_notebook_node(nb)
out=Path(__file__).parent/'results'
out.mkdir(exist_ok=True)
(out/'lecture.html').write_text(html)
print(out/'lecture.html')
