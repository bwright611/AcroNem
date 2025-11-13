import re
import sys
from docx import Document
from docx.shared import Inches
import spacy
import nltk
import json
import argparse

#!/usr/bin/env python3
"""
acrofind.py - simple acronym finder
Usage:
    python acrofind.py [paths...] [-r] [--min LEN] [--json] [-v]
If no paths are given, reads from stdin.
"""


ACRO_RE = re.compile(
        r"""(
                (?:[A-Z]\.){2,}         # dotted acronyms like U.S.A.
                |
                \b(?:(?:[A-Z]{2,}|(?:[a-z]*[A-Z][a-z]*){2,}|[A-Z](?:[-&][A-Z]+)+)\d*|\d+[A-Z]|[A-Z]\d+)\b  # consecutive caps like NASA or X-99
        )""",
        re.VERBOSE,
)

def importAcronymList(file_path: str) -> set[str]:
        return 0

"""
 def find_acronyms_in_text(text: str, min_len: int = 2) -> Counter:
        #Return counter of acronyms found in text.
        matches = (m.group(0) for m in ACRO_RE.finditer(text))
        normalized = (m.rstrip(".") for m in matches) 
        filtered = (m for m in normalized if len(m.replace(".", "")) >= min_len)
        return Counter(filtered)
"""

def importWordDocx(file_path: str) -> str:
        """Extract text from a .docx file."""
        doc = python-docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
                full_text.append(para.text)
        return "\n".join(full_text)

def main(argv: list[str] | None = None) -> int:
        document = Document('TARCES Technical Volume - Test.docx')
        # document.save('newTarces.docx')
        
        acronym_list = []
        found_in_paragraphs = []

        print("\nSearching in paragraphs:")
        for paragraph in document.paragraphs:
                acronym_matches = ACRO_RE.findall(paragraph.text)
                if acronym_matches:
                        acronym_list.extend(acronym_matches)

        print("\nSearching in tables...")
        for table in document.tables:
                for row in table.rows:
                        for cell in row.cells:
                                acronym_matches = ACRO_RE.findall(cell.text)
                                if acronym_matches:
                                        acronym_list.extend(acronym_matches)
        exclude_list = ['1366E', '141B', '175F', '175X', '181D', '220D', '31000B', '400S', '881F', 'A001', 'A002', 'A004', 'A006', 'A007', 'A010', 'A011', 'A012', 'A013', 'A022', 'A026', 'A027', 'COMMAND', 'COMMUNICATIONS', 'COMPUTERS', 'CONOPS', 'CONTROL', 'INTELLIGENCE', 'TACTICAL', 'TECHNICAL', 'SYSTEMS', 'REMOTE']
        deduped_acronym_list = list(set(acronym_list))
        sorted_acronym_list = sorted(deduped_acronym_list, key=lambda v: v.upper())
        sorted_acronym_list = [x for x in sorted_acronym_list if x not in exclude_list]
        print(sorted_acronym_list)
        print(f"The number of acronyms is: {len(sorted_acronym_list)}")



"""
                        # acronym_list.append(match.group(0))
                        if match.group(0) not in acronym_list:
                                acronym_list.append(match.group(0))
                                print("Acronym Found: ", {match.group(0)})
                                print("Paragraph Text: ", paragraph_text)
"""

"""     
        for paragraph in document.paragraphs:
                if search_term in paragraph.text:
                        found_in_paragraphs.append(paragraph.text)

        if found_in_paragraphs:
                print(f"Found '{search_term}' in the following paragraphs:")
                for p_text in found_in_paragraphs:
                        print(f"- {p_text}")
        else:
                print(f"'{search_term}' not found in any paragraph.")
"""
                

if __name__ == "__main__":
        sys.exit(main())
