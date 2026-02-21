import difflib

# Read original
with open('/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/1_Peekaboo/alltex.tex') as f:
    lines = f.readlines()

# Lines 440-452 (1-indexed)
orig_lines = lines[439:452]

# Read thesis
with open('/Users/ryan/CleanCode/Sandbox/RP_Dumps/ThesisProposal/source/src/1_Peekaboo/related_work_thesis.tex') as f:
    thesis_lines = f.readlines()

# Normalize original: replace \modelname with Peekaboo
norm_orig = []
for line in orig_lines:
    line = line.replace('\\modelname', 'Peekaboo')
    norm_orig.append(line)

# Show unified diff
diff = list(difflib.unified_diff(
    [l.rstrip('\n') for l in norm_orig],
    [l.rstrip('\n') for l in thesis_lines],
    fromfile='original (normalized)',
    tofile='thesis',
    lineterm=''
))

for d in diff:
    print(d)

print("\n\n=== CHARACTER-LEVEL COMPARISON (ignoring section header and label) ===")

# Strip the section header and label from both, then compare body text
orig_body = ''.join(norm_orig[2:])  # skip \section and \label lines
thesis_body = ''.join(thesis_lines[2:])  # skip \section and \label lines

if orig_body == thesis_body:
    print("BODY TEXT IS IDENTICAL (after \\modelname -> Peekaboo expansion)")
else:
    print("BODY TEXT DIFFERS!")
    sm = difflib.SequenceMatcher(None, orig_body, thesis_body)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal':
            print(f"  {tag}: orig[{i1}:{i2}]={repr(orig_body[i1:i2])} -> thesis[{j1}:{j2}]={repr(thesis_body[j1:j2])}")
