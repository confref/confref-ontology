#!/usr/bin/env python3
"""Write confref-ontology.ttl from the code blocks of confref-ontology.md (the source)."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
out, block = ["# Generated from confref-ontology.md by generate.py; edit that file.\n"], False
for line in (HERE / "confref-ontology.md").read_text(encoding="utf-8").splitlines(keepends=True):
    if line.startswith("```"):
        block = not block
        if not block:
            out.append("\n")
        continue
    if block:
        out.append(line)
(HERE / "confref-ontology.ttl").write_text("".join(out).rstrip("\n") + "\n", encoding="utf-8")
