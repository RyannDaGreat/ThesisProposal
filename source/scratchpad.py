import difflib
import re

def extract_section(filepath, start_label, end_markers):
    """Extract a section from a monolithic tex file."""
    with open(filepath) as f:
        lines = f.readlines()
    in_section = False
    section_lines = []
    for line in lines:
        if start_label in line:
            in_section = True
        if in_section:
            if any(m in line for m in end_markers) and start_label not in line:
                break
            section_lines.append(line)
    return ''.join(section_lines)

# Load all files
def load(path):
    with open(path) as f:
        return f.read()

papers = {
    "LSS": {
        "original": load("/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/.frenzy/kanchana_originals/LSS/sections/related_work.tex"),
        "thesis": load("/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/kanchana_example/report/src/1_LSS/sections/related_work.tex"),
    },
    "LocVLM": {
        "original": load("/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/.frenzy/kanchana_originals/LocVLM/sec/2_related.tex"),
        "thesis": load("/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/kanchana_example/report/src/2_LocVLM/sec/2_related.tex"),
    },
    "MVU": {
        "original": extract_section(
            "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/.frenzy/kanchana_originals/MVU/main.tex",
            r"\label{sec:related}", [r"\section{"]),
        "thesis": load("/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/kanchana_example/report/src/3_MVU/related.tex"),
    },
    "LTM": {
        "original": extract_section(
            "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/.frenzy/kanchana_originals/LTM/main.tex",
            r"\label{sec:related_work}", [r"\section{"]),
        "thesis": load("/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/kanchana_example/report/src/4_LTM/related.tex"),
    },
}

for name, data in papers.items():
    print("\n" + "=" * 80)
    print(f"  {name}: UNIFIED DIFF (original -> thesis)")
    print("=" * 80)
    orig_lines = data["original"].splitlines(keepends=True)
    thesis_lines = data["thesis"].splitlines(keepends=True)
    diff = difflib.unified_diff(
        orig_lines, thesis_lines,
        fromfile=f"{name}_original",
        tofile=f"{name}_thesis",
        lineterm=""
    )
    diff_text = ''.join(diff)
    if diff_text.strip():
        print(diff_text)
    else:
        print("  [IDENTICAL]")
