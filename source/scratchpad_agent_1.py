import re
from collections import Counter

files = {
    "1_Peekaboo": "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/1_Peekaboo/related_work_thesis.tex",
    "2_DiffIllusions": "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/2_DiffIllusions/related_work_thesis.tex",
    "3_MAGICK": "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/3_MAGICK/sec/2_relatedwork_thesis.tex",
    "4_GWTF": "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/4_GWTF/sec/2_related_work_thesis.tex",
    "5_MotionV2V": "/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/5_MotionV2V/sec/relatedworks_thesis.tex",
}

all_cites = {}
all_topics = {}

for name, path in files.items():
    with open(path) as f:
        text = f.read()

    # Extract cite keys
    cite_matches = re.findall(r'\\cite\{([^}]+)\}', text)
    keys = []
    for m in cite_matches:
        keys.extend([k.strip() for k in m.split(',')])
    all_cites[name] = sorted(set(keys))

    # Word count (strip latex commands loosely)
    stripped = re.sub(r'\\[a-zA-Z]+\{[^}]*\}', '', text)
    stripped = re.sub(r'\\[a-zA-Z]+', '', stripped)
    stripped = re.sub(r'[{}~\\]', ' ', stripped)
    words = stripped.split()
    word_count = len(words)

    print(f"\n{'='*70}")
    print(f"FILE: {name}")
    print(f"{'='*70}")
    print(f"Citation count: {len(all_cites[name])} unique keys")
    print(f"Approx word count: {word_count}")
    print(f"Citations: {all_cites[name]}")

# Build overlap matrix
print(f"\n\n{'='*70}")
print("CITATION OVERLAP MATRIX")
print(f"{'='*70}")

file_names = list(all_cites.keys())
# Find citations appearing in multiple files
cite_to_files = {}
for name, cites in all_cites.items():
    for c in cites:
        cite_to_files.setdefault(c, []).append(name)

shared = {k: v for k, v in cite_to_files.items() if len(v) > 1}
print(f"\nShared citations ({len(shared)} total):")
for cite, fnames in sorted(shared.items(), key=lambda x: -len(x[1])):
    print(f"  {cite:45s} -> {fnames}")

# Pairwise overlap
print(f"\nPairwise overlap counts:")
for i, n1 in enumerate(file_names):
    for j, n2 in enumerate(file_names):
        if j > i:
            overlap = set(all_cites[n1]) & set(all_cites[n2])
            if overlap:
                print(f"  {n1} <-> {n2}: {len(overlap)} shared ({', '.join(sorted(overlap))})")
            else:
                print(f"  {n1} <-> {n2}: 0 shared")
