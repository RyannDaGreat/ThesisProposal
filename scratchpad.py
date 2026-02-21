import re
import os

base = "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/3_MAGICK/sec"
files = [
    "1_intro_thesis.tex",
    "2_relatedwork_thesis.tex",
    "3_method_thesis.tex",
    "4_results_thesis.tex",
    "5_conclusion_thesis.tex",
]

all_labels = set()
all_refs = set()

for fname in files:
    fpath = os.path.join(base, fname)
    with open(fpath) as f:
        content = f.read()

    labels = re.findall(r"\\label\{([^}]+)\}", content)
    refs = re.findall(r"\\(?:c?C?ref)\{([^}]+)\}", content)

    for l in labels:
        all_labels.add(l)
    for r in refs:
        all_refs.add(r)

print("LABELS defined:")
for l in sorted(all_labels):
    print(f"  {l}")

print(f"\nREFS used:")
for r in sorted(all_refs):
    print(f"  {r}")

# Check for refs without corresponding labels
missing = all_refs - all_labels
if missing:
    print(f"\nWARNING - refs without labels in these files (may be defined elsewhere):")
    for m in sorted(missing):
        print(f"  {m}")
else:
    print("\nAll refs have matching labels within these files.")
