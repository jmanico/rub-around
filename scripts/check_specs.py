#!/usr/bin/env python3
"""Check documentation integrity without claiming application verification."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = ['REQUIREMENTS.md', 'DESIGN.md', 'ARCHITECTURE.md', 'SECURITY.md', 'AGENTS.md']
ID = r'(?:FR|NFR|OQ|DQ|AQ|DR|SC|OD|WQ|AC)-\d+(?:\.\d+)?'
texts = {name: (ROOT / name).read_text() for name in FILES}
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def slug(value):
    value = re.sub(r'[^\w\- ]', '', value.lower())
    return value.replace(' ', '-')

anchors = {}
definitions = {}
for name, text in texts.items():
    anchors[name] = set(re.findall(r'<a id="([^"]+)"', text))
    anchors[name].update(slug(h) for h in re.findall(r'^#{1,6} (.+)$', text, re.M))
    defs = re.findall(r'^#{2,6} (' + ID + r')\s*$', text, re.M)
    defs += re.findall(r'^- \*\*(' + ID + r'):?\*\*', text, re.M)
    defs += re.findall(r'^\| (AC-\d+) \|', text, re.M)
    defs += re.findall(r'<a id="[^"]+"></a>(' + ID + r')', text)
    for identifier in defs:
        check(identifier not in definitions, f'Duplicate definition: {identifier}')
        definitions[identifier] = name
    check(not re.search(r'TO BE DECIDED|\bUNKNOWN\b|\bTBD\b|\bPROPOSED\b|\bBLOCKED\b|<<[^>]+>>|\{\{[^}]+\}\}', text),
          f'Unresolved marker in {name}')

owners = {'FR': 'REQUIREMENTS.md', 'NFR': 'REQUIREMENTS.md', 'OQ': 'REQUIREMENTS.md',
          'AC': 'REQUIREMENTS.md', 'DQ': 'DESIGN.md', 'AQ': 'ARCHITECTURE.md',
          'DR': 'ARCHITECTURE.md', 'SC': 'SECURITY.md', 'OD': 'SECURITY.md', 'WQ': 'AGENTS.md'}
for identifier, name in definitions.items():
    check(owners[identifier.split('-')[0]] == name, f'Wrong owner: {identifier} in {name}')
for name, text in texts.items():
    for identifier in set(re.findall(r'\b' + ID + r'\b', text)):
        check(identifier in definitions, f'Undefined ID {identifier} in {name}')

# Local file and fragment links, plus registry/audit destinations.
def check_target(target, source):
    if re.match(r'https?://', target):
        return
    filename, _, fragment = target.partition('#')
    filename = filename or source
    check((ROOT / filename).exists(), f'Missing local target {target} in {source}')
    if fragment:
        check(fragment in anchors.get(filename, set()), f'Missing anchor {target} in {source}')

for name, text in texts.items():
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        check_target(target, name)

register = json.loads((ROOT / 'decision-register.json').read_text())
audit = json.loads((ROOT / 'specification-audit.json').read_text())
for item in register['queue']:
    check(item['status'] in ['RESOLVED', 'DEFERRED'], f'Unanswered topic {item["order"]}')
    check_target(item['resolution_reference'], item['owner_file'])
    if item['status'] == 'DEFERRED':
        check(item['decision_id'] == 'OD-015', 'Unexpected deferred decision')
        check(bool(item.get('blocks')) and bool(item.get('resume_when')), 'Incomplete deferral')
check(not (ROOT / 'THREAT_MODEL.md').exists(), 'Threat model was requested to remain uncreated')
for item in audit['inventory']:
    check(bool(item['destinations']), f'Unmapped inventory entry {item}')
    for target in item['destinations']:
        check_target(target, item['source_file'])
for identifier in audit.get('original_definitions', []):
    check(identifier in definitions, f'Dropped original ID {identifier}')
for name, digest in audit['protected_files'].items():
    check((ROOT / name).exists() and hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
          f'Protected artifact changed: {name}')

coverage = texts['REQUIREMENTS.md'].split('## Acceptance Coverage', 1)[1].split('## Resolved Decisions', 1)[0]
covered = set(re.findall(r'\b(?:FR|NFR)-\d+(?:\.\d+)?\b', coverage))
for identifier in definitions:
    if identifier.startswith(('FR-', 'NFR-')):
        check(identifier in covered, f'No acceptance coverage for {identifier}')
control_coverage = texts['SECURITY.md'].split('## Control Coverage', 1)[1]
for identifier in definitions:
    if identifier.startswith('SC-'):
        check(identifier in control_coverage, f'No coverage disposition for {identifier}')
# A domain owner may reference another file but must not copy a normative sentence.
seen = {}
for name, text in texts.items():
    for line in text.splitlines():
        norm = re.sub(r'\s+', ' ', line.strip())
        if len(norm) > 100 and re.search(r'\b(must|never|require|prohibit)\b', norm, re.I):
            check(norm not in seen or seen[norm] == name, f'Duplicated normative line: {name}, {seen.get(norm)}')
            seen[norm] = name

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(FILES)} specifications, {len(definitions)} IDs, {len(register["queue"])} decisions, '
      f'{len(audit["inventory"])} source inventory entries; coverage and protected artifacts checked.')
print('Scope: documentation integrity only; application/security/accessibility tests are not implemented.')
