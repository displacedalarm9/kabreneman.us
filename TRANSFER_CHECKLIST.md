---
last_updated: 2026-04-03
version: 1.0.0
file_status: protocol
---

# Transfer Checklist — dev.kabreneman.us

[See: docs/filename.md for naming conventions]
[See: standards.md for documentation standards]
[See: procedures/changes.md for change management steps]
[See: .gitignore for sensitive data exclusion patterns]

## Purpose

Checklist for transferring repository content from `kabreneman.us` into the `dev.kabreneman.us` environment. Complete all items in order before marking the transfer done.

---

## 1. Pre-Transfer Verification

### 1.1 Sensitive Data Check
- [ ] Confirm no personal financial records are staged for transfer
- [ ] Confirm no credentials, tokens, or secrets are present in any file
- [ ] Run `.gitignore` review — verify all exclusion patterns are current
- [ ] Confirm all data files remain in `~/secure-kabreneman-backup/` only

### 1.2 Naming Convention Compliance
- [ ] All filenames are lowercase with hyphens for dates (`YYYY-MM-DD`) and underscores for word separators
- [ ] No spaces in any filename
- [ ] All new files follow the `[Type]_[ID/Date]_[Description].[ext]` pattern
- [ ] Run `scripts/fix_filenames.py` against any modified directories if needed

### 1.3 Metadata & Frontmatter
- [ ] All modified markdown files include valid YAML frontmatter (`last_updated`, `version`, `file_status`)
- [ ] `last_updated` reflects the actual date of last modification
- [ ] `file_status` is one of: `template`, `active`, `protocol`, `archive`

### 1.4 Cross-Reference Integrity
- [ ] All `[See: ...]` references point to files that exist in the repository
- [ ] No broken internal links

---

## 2. Content Inventory

### 2.1 Core Files
| File | Status | Transfer? |
|------|--------|-----------|
| `README.md` | active | [✓/-] |
| `standards.md` | active | [✓/-] |
| `topics.json` | active | [✓/-] |

### 2.2 Directories
| Directory | Status | Transfer? |
|-----------|--------|-----------|
| `configs/` | active | [✓/-] |
| `docs/` | active | [✓/-] |
| `procedures/` | active | [✓/-] |
| `scripts/` | active | [✓/-] |
| `templates/` | active | [✓/-] |
| `logs/` | active | [✓/-] |
| `archive/` | archive | [✓/-] |

### 2.3 Exclusions — Never Transfer
- [ ] `~/secure-kabreneman-backup/` contents
- [ ] Any `*.csv` with real financial data
- [ ] Any `.env` files beyond `.env.example`
- [ ] `OPERCAP1.xlsm` or any workbook with live financial data
- [ ] Any file matching `.gitignore` patterns

---

## 3. Transfer Steps

1. [ ] Checkout or pull the target branch to be transferred
2. [ ] Verify the working tree is clean (`git status`)
3. [ ] Confirm the destination environment (`dev.kabreneman.us`) is accessible
4. [ ] Push/deploy only non-sensitive content to `dev.kabreneman.us`
5. [ ] Log the transfer date and branch in the deployment record

---

## 4. Post-Transfer Verification

### 4.1 Content Check
- [ ] All expected directories are present on `dev.kabreneman.us`
- [ ] All template files render correctly
- [ ] All cross-references resolve

### 4.2 Security Check
- [ ] Confirm no sensitive data is visible on `dev.kabreneman.us`
- [ ] Confirm `.gitignore` exclusions were respected during transfer

### 4.3 Sign-Off
- [ ] Transfer reviewed and confirmed complete
- [ ] Date logged: ___________
- [ ] Operator: ___________
