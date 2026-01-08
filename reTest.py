import re

'''
ACRO_RE = re.compile(
        r"""(
                (?:[A-Z]\.){2,}         # dotted acronyms like U.S.A.
                |
                \b(?:(?:[A-Z]{2,}|(?:[a-z]*[A-Z][a-z]*){2,}|[A-Z](?:[-&][A-Z]+)+)\d*|\d+[A-Z]|[A-Z]\d+)\b  # consecutive caps like NASA or X-99
        )""",
        re.VERBOSE,
)
'''
ACRO_RE = re.compile(r'''
    (                                   # ── whole match ──
        (?:[A-Z]\.){2,}                 #   dotted acronyms:  U.S.A.,  N.A.S.A.
      | \b
        (?:                             #   ── “real” acronyms ──
            \d+[A-Z]{1,}                #   2FA , 3GPP               (digits → caps)
          | [A-Z]\d+                    #   C5I  (caps → digits)
          | [A-Z]\d+[A-Z]                 # C5I, X9Y   (cap‑digit‑cap)
          | [A-Z]{2,}                   #   ARROW, ATS, US, WAN …   (plain all‑caps)
          | [A-Z]+(?:[-&/][A-Z]+)+      #   USB‑C, TSM‑X, O&M, AN/PRC (caps separated by – & /)
          | [a-z]{2,}                   #   bps, ft, km, KPI …      (all‑lower units)
          | [a-z]+/[a-z]+               #   ft/s                    (lower‑case slash)
          | [A-Z]{2,}[a-z]+             #   MMWave, MIL‑SPEC        (caps‑then‑lower)
          | [A-Za-z]*[A-Z][A-Za-z]*[a-z][A-Za-z]*   # mixed‑case with at least one lower‑case letter
        )
        \b
    )
''', re.VERBOSE)

tests = [
    "2FA","AN/PRC","ARROW","ATS","bps","C5I","CAD","CONOPS","CUI","DAS","DID",
    "DoDAF","ECP","EDP","ft","ft/s","Gbps","km","KPI","MB","MIL-SPEC",
    "MMWave","MTBF","MTTR","O&M","OTDR","P25","PM","TAE","TLS","TSM",
    "TSM-X","USB-C","US","WAN"
]



for t in tests:
    if ACRO_RE.search(t):
        print(f"✔ {t}")
    else:
        print(f"✘ {t}")