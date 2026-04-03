---
last_updated: 2026-04-03
version: 1.0.0
file_status: protocol
docsys_scope: UNISYS
---

# TRANSFER CHECKLIST — kabreneman.us Repository Audit

**Audit Date:** 2026-04-03  
**Auditor:** Copilot  
**Scope:** Full repository audit for accuracy, completeness, and REDOREPO sync readiness  
**Related Issues:** #50, #52

---

## Audit Summary

| Category | Total Files | ✅ Accurate | ⚠️ Needs Fix | ❌ Issues Found |
|----------|-------------|------------|--------------|----------------|
| Root-level files | 14 | 7 | 5 | 2 |
| `.github/` | 4 | 3 | 1 | 0 |
| `archive/` | 5 | 4 | 1 | 0 |
| `configs/` | 4 | 4 | 0 | 0 |
| `data/` | 2 | 1 | 1 | 0 |
| `docs/` | 8 | 5 | 2 | 1 |
| `logs/` | 5 | 4 | 1 | 0 |
| `procedures/` | 5 | 5 | 0 | 0 |
| `projects/` | 2 | 2 | 0 | 0 |
| `reports/` | 7 | 7 | 0 | 0 |
| `reviews/` | 8 | 8 | 0 | 0 |
| `scripts/` | 4 | 4 | 0 | 0 |
| `shared/` | 7 | 5 | 2 | 0 |
| `templates/` | 16 | 14 | 2 | 0 |
| `utilities/` | 5 | 5 | 0 | 0 |

---

## REDOREPO Sync Status

These nodes must receive all canonized files per `docs/project_support/copilot/README.md`:

| Node | Path | Sync Status |
|------|------|-------------|
| OneDrive | `KABDMSV2/` | ⬜ Pending |
| iCloud Drive | `KABDMSV2/` | ⬜ Pending |
| Google Drive | `KABDMSV2/` | ⬜ Pending |
| NAS | `KABDMSV2/` | ⬜ Pending |
| dev.kabreneman.us | (GitHub repo) | ⬜ Pending |

---

## File Inventory & Audit

### Root Level

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `README_KABDMSV2.md` | ✅ | None | — |
| `WorkingCapital.md` | ⚠️ | References `review.md`, `accounts.md`, `matrix.md`, `changeover.md` without full paths | Update cross-references |
| `allocation.md` | ⚠️ | Missing frontmatter; `[DATE]` placeholders unfilled | Add frontmatter; fill placeholders |
| `cashflowsfy26.md` | ⚠️ | Missing frontmatter; references `./allocations.md` (file is `allocation.md`) | Add frontmatter; fix reference |
| `debts.csv` | ✅ | None | — |
| `expenses.md` | ⚠️ | Contains actual June 2025 financial data; suitable for data repo only | Verify not sensitive before keeping |
| `obligations.md` | ⚠️ | Missing frontmatter; `[DATE]` placeholders unfilled | Add frontmatter; fill placeholders |
| `obligationadherence.md` | ✅ | Contains historical tracking data | — |
| `OPERCAP1.xlsm` | ✅ | Excel workbook; archived/reference | — |
| `progress.md` | ✅ | Complete with frontmatter | — |
| `review.md` | ✅ | Complete with frontmatter | — |
| `standards.md` | ⚠️ | Template index section references non-existent subdirectories (`/templates/review/`, `/templates/report/`, etc.); actual template locations differ | Fix template path references |
| `topics.json` | ❌ | `dataRepository` field value is `"kabreneman.us"` (same as this repo); should reference external data repo | Update to reflect actual data repo name |

### `.github/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `copilot-instructions.md` | ✅ | Current UNISYS-aligned instructions | — |
| `PULL_REQUEST_TEMPLATE.md` | ✅ | Covers documentation and sensitive data checks | — |
| `ISSUE_TEMPLATE/config.yml` | ✅ | — | — |
| `ISSUE_TEMPLATE/work-documentation.md` | ✅ | — | — |
| `DOCSYS Copilot Synchronization Kit 2026-04-06.md` | ⚠️ | Filename uses spaces (violates naming convention); dated 2026-04-06 but creation date is 2026-04-03 | Rename to `docsys_copilot-sync-kit_2026-04-03.md` |

### `archive/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `abandoned-projects/README.md` | ✅ | None | — |
| `2025/Q2/folder-audit.md` | ✅ | Archived correctly | — |
| `2025/Q4/2025-11-25_file-review.md` | ✅ | None | — |
| `2025/Q4/misc/2025-11-25_accordion-decision-flowchart.md` | ✅ | None | — |
| `2025/Q4/misc/2025-11-25_accordion-decision-flowchart.txt` | ⚠️ | `.txt` duplicate of `.md`; likely redundant | Confirm and remove if duplicate |

### `configs/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `config_NODE-ARC-003_CustomArchival.xml` | ✅ | None | — |
| `config_NODE-OPS-001_Legion5Gen10.xml` | ✅ | None | — |
| `config_NODE-VR-002_LegionPro5Gen10.xml` | ✅ | None | — |

### `data/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | Explains gitignored sensitive data | — |
| `subscriptions.md` | ⚠️ | Contains actual personal subscription data with agreement numbers; sensitive | Verify appropriate for public repo or move to data repo |

### `docs/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `canonical-context.md` | ⚠️ | Repository structure section is incomplete (missing `allocation.md`, `cashflowsfy26.md`, `data/`, `logs/`, `projects/`, `reports/`, `reviews/`, `shared/`, `utilities/`, `debts.csv`, `obligations.md`, etc.) | Update structure section |
| `filename.md` | ✅ | Accurate naming convention definitions | — |
| `folder-audit.md` | ⚠️ | References `/WORKCAP/` root structure which does not match actual repo layout | Update to reflect actual structure |
| `history.md` | ✅ | Accurate terminology history | — |
| `metadata-wizard.md` | ✅ | Complete documentation | — |
| `automation-guide.md` | ⚠️ | Missing frontmatter | Add frontmatter |
| `report-standards.md` | ✅ | Accurate report naming patterns | — |
| `project_support/copilot/README.md` | ✅ | DOCSYS/UNISYS canonized; REDOREPO sync pending | Sync to REDOREPO nodes |
| `project_support/copilot/2025-08_copilot-activity-history.md` | ✅ | Companion intake record | Sync to REDOREPO nodes |
| `project_support/copilot/2025-08_copilot-chat-activity.md` | ✅ | Companion intake record | Sync to REDOREPO nodes |

### `logs/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `accounts.md` | ✅ | None | — |
| `bills.md` | ✅ | None | — |
| `debt.md` | ✅ | None | — |
| `journal.md` | ⚠️ | Check for actual financial transaction data | Verify no sensitive committed data |

### `procedures/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `changeover.md` | ✅ | Phase transition plans accurate | — |
| `changes.md` | ✅ | None | — |
| `emergency.md` | ✅ | Emergency protocols current | — |
| `matrix.md` | ✅ | Distribution matrix current | — |
| `schedule.md` | ✅ | Review schedule accurate | — |

### `projects/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `workcap/README.md` | ✅ | Accurately documents root-level WORKCAP files | — |

### `reports/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `analysis/2025-06-06_workcap_analysis.md` | ✅ | None | — |
| `analysis/archive/2025-06-06_workcap_analysis_224407.md` | ✅ | Archived analysis | — |
| `analysis/archive/2025-06-06_workcap_analysis_224435.md` | ✅ | Archived analysis | — |
| `analysis/archive/2025-06-06_workcap_analysis_224712.md` | ✅ | Archived analysis | — |
| `analysis/archive/2025-06-06_workcap_analysis_224725.md` | ✅ | Archived analysis | — |
| `analysis/archive/2025-06-06_workcap_analysis_225154.md` | ✅ | Archived analysis | — |
| `analysis/archive/2025-06-06_workcap_analysis_225352.md` | ✅ | Archived analysis | — |

### `reviews/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `accounts/2025-06/2025-06-06_daily.md` | ✅ | None | — |
| `adherence/2025-06-06_adherence.md` | ✅ | None | — |
| `obligations/2025-06-06_obligations.md` | ✅ | None | — |
| `status/2025-06-06_status.md` | ✅ | None | — |
| `utilities/2025-06/2025-06-06_evergy.md` | ✅ | None | — |
| `utilities/2025-06/2025-06-06_gas.md` | ✅ | None | — |
| `utilities/2025-06/2025-06-06_water.md` | ✅ | None | — |
| `variance/2025-06/2025-06-06_variance.md` | ✅ | None | — |
| `variance/2025-06/2025-06-21_variance.md` | ✅ | None | — |

### `scripts/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `fix_filenames.py` | ✅ | None | — |
| `metadata_wizard.py` | ✅ | None | — |
| `workcap_analyzer.py` | ✅ | None | — |

### `shared/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `README.md` | ✅ | None | — |
| `data/README.md` | ✅ | None | — |
| `scripts/README.md` | ✅ | None | — |
| `scripts/fix_filenames.py` | ⚠️ | Duplicate of `scripts/fix_filenames.py`; may diverge | Verify sync or consolidate |
| `scripts/workcap_analyzer.py` | ⚠️ | Duplicate of `scripts/workcap_analyzer.py`; may diverge | Verify sync or consolidate |
| `utilities/README.md` | ✅ | None | — |

### `templates/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `index.md` | ⚠️ | References non-existent subdirectories (`/review/`, `/report/`, `/data/`, `/invest/`); actual templates are mostly flat | Update to reflect actual template locations |
| `accounts.md` | ✅ | None | — |
| `daily.md` | ✅ | None | — |
| `data/subscriptions.md` | ✅ | Template for subscription tracking | — |
| `distribution.md` | ✅ | None | — |
| `investment.md` | ✅ | None | — |
| `monthly.md` | ✅ | None | — |
| `obligations.md` | ✅ | None | — |
| `opercap1.md` | ✅ | Archived OPERCAP1 template | — |
| `quarterly.md` | ✅ | None | — |
| `report/weekly.md` | ✅ | None | — |
| `reports.md` | ⚠️ | Contains older report format reference; may be superseded by `docs/report-standards.md` | Verify or archive |
| `sidu.md` | ✅ | None | — |
| `status.md` | ✅ | None | — |
| `utilities.md` | ✅ | None | — |
| `variance.md` | ✅ | None | — |
| `weekly.md` | ✅ | None | — |

### `utilities/`

| File | Status | Issues | Action |
|------|--------|--------|--------|
| `2025-06/consolidated.md` | ✅ | None | — |
| `2025-06/evergy-2025-06.md` | ✅ | None | — |
| `2025-06/evergy.md` | ✅ | None | — |
| `2025-06/gas-2025-06.md` | ✅ | None | — |
| `2025-06/kansas-gas.md` | ✅ | None | — |
| `2025-06/water.md` | ✅ | None | — |

---

## Priority Action Items

### P1 — Critical

- [ ] **Fix `topics.json`**: `dataRepository` field is `"kabreneman.us"` (self-referential); should reference actual private data repository name
- [ ] **Rename `.github/DOCSYS Copilot Synchronization Kit 2026-04-06.md`**: Violates filename convention (spaces); rename to a compliant filename

### P2 — High

- [ ] **Add frontmatter to `allocation.md`**: Missing `last_updated`, `version`, `file_status`
- [ ] **Add frontmatter to `cashflowsfy26.md`**: Missing `last_updated`, `version`, `file_status`
- [ ] **Add frontmatter to `obligations.md`**: Missing `last_updated`, `version`, `file_status`
- [ ] **Add frontmatter to `docs/automation-guide.md`**: Missing `last_updated`, `version`, `file_status`
- [ ] **Fix `cashflowsfy26.md` cross-reference**: References `./allocations.md`; actual file is `allocation.md`
- [ ] **Fill `[DATE]` placeholders** in `allocation.md` and `obligations.md`
- [ ] **Update `standards.md` template index**: References `/templates/review/`, `/templates/report/`, `/templates/data/`, `/templates/invest/` which don't exist as described; actual templates are mostly at `templates/*.md`
- [ ] **Update `templates/index.md`**: Same issue as `standards.md` — references non-existent subdirectory structure

### P3 — Medium

- [ ] **Update `docs/canonical-context.md`** repository structure section to include all current files and directories (`allocation.md`, `cashflowsfy26.md`, `data/`, `logs/`, `projects/`, `reports/`, `reviews/`, `shared/`, `utilities/`, `debts.csv`, `obligations.md`, `expenses.md`, `obligationadherence.md`, `progress.md`, `review.md`, `standards.md`, `WorkingCapital.md`)
- [ ] **Update `docs/folder-audit.md`**: References `/WORKCAP/` root path structure that doesn't match actual layout
- [ ] **Fix `WorkingCapital.md` cross-references**: `[See: accounts.md]` should be `[See: logs/accounts.md]`; `[See: changeover.md]` should be `[See: procedures/changeover.md]`; `[See: matrix.md]` should be `[See: procedures/matrix.md]`
- [ ] **Verify `data/subscriptions.md`**: Contains Apple agreement numbers and personal subscription details — confirm it is appropriate for a public repository
- [ ] **Verify `shared/scripts/` duplicates**: `shared/scripts/fix_filenames.py` and `shared/scripts/workcap_analyzer.py` appear to duplicate `scripts/`; confirm which is canonical and consolidate if possible

### P4 — Low

- [ ] **Initiate REDOREPO sync**: Push all canonized files to OneDrive, iCloud Drive, Google Drive, and NAS nodes
- [ ] **Review `archive/2025/Q4/misc/2025-11-25_accordion-decision-flowchart.txt`**: `.txt` duplicate of `.md` version; remove if redundant
- [ ] **Review `templates/reports.md`**: Assess whether superseded by `docs/report-standards.md`
- [ ] **Address open GitHub issues**: #25 (naming conventions), #26 (frontmatter), #28 (report folders), #29 (XSD validation), #31 (security), #32 (dependencies), #33 (analyzer docs), #34 (PR checklist), #35 (link validation), #36 (topics.json), #37 (upload files), #39 (off-repo files)

---

## Transfer Targets — dev.kabreneman.us

The following files are designated for transfer/sync to `dev.kabreneman.us`:

- [ ] All `docs/` files (canonical documentation)
- [ ] All `procedures/` files (operational procedures)
- [ ] All `templates/` files (standardized templates)
- [ ] `docs/project_support/copilot/` directory (DOCSYS artifacts, TSN:0001–TSN:0003)
- [ ] `configs/` directory (node configurations)
- [ ] `scripts/` directory (utilities)
- [ ] `standards.md`, `WorkingCapital.md` (core reference files)
- [ ] `TRANSFER_CHECKLIST.md` (this file)

The following files should **NOT** transfer to dev.kabreneman.us (sensitive or environment-specific):

- ❌ `expenses.md` — contains actual financial transaction data
- ❌ `obligationadherence.md` — contains actual debt/account data
- ❌ `data/subscriptions.md` — contains Apple agreement number (sensitive)
- ❌ `debts.csv` — financial data
- ❌ `OPERCAP1.xlsm` — binary spreadsheet with financial data
- ❌ `logs/` files — transactional data

---

## Accuracy Issues by File

### `topics.json`
```json
{
  "dataRepository": "kabreneman.us"  // ← INCORRECT: Self-referential
}
```
Should reference the external private data repository name.

### `cashflowsfy26.md`
```markdown
- Income Allocations: [allocations.md](./allocations.md)  // ← INCORRECT: file is allocation.md
```

### `standards.md` Template Index
```
/templates/review/daily.md    // ← Does NOT exist at this path
/templates/report/variance.md // ← Does NOT exist at this path
/templates/data/accounts.md   // ← Does NOT exist at this path
/templates/invest/sidu.md     // ← Does NOT exist at this path
```
Actual template locations:
```
templates/daily.md            ← correct
templates/variance.md         ← correct
templates/accounts.md         ← correct
templates/sidu.md             ← correct
```

### `WorkingCapital.md` Cross-References
```markdown
[See: accounts.md ...]         // ← Should be: logs/accounts.md
[See: changeover.md ...]       // ← Should be: procedures/changeover.md
[See: matrix.md ...]           // ← Should be: procedures/matrix.md
```

---

## Compliance Checklist

### Naming Conventions (`docs/filename.md`)
- [x] All `docs/` files follow lowercase, underscore, hyphenated-date convention
- [x] All `templates/` files follow convention
- [x] All `procedures/` files follow convention
- [x] All `reviews/` files follow YYYY-MM-DD prefix convention
- [ ] `.github/DOCSYS Copilot Synchronization Kit 2026-04-06.md` — spaces in name (violation)

### Frontmatter Completeness
- [x] `WorkingCapital.md` — ✅
- [x] `progress.md` — ✅
- [x] `standards.md` — ✅
- [x] `review.md` — ✅
- [x] `expenses.md` — ✅
- [x] `obligationadherence.md` — ✅
- [ ] `allocation.md` — ❌ missing
- [ ] `cashflowsfy26.md` — ❌ missing
- [ ] `obligations.md` — ❌ missing
- [ ] `docs/automation-guide.md` — ❌ missing

### Security Boundaries
- [x] `.gitignore` exists and covers sensitive data patterns
- [x] `data/README.md` explicitly states all contents are gitignored
- [ ] `data/subscriptions.md` is committed with Apple agreement number — review
- [ ] `expenses.md` is committed with actual June 2025 transaction data — review
- [ ] `obligationadherence.md` is committed with account balances and collections — review

---

*Generated: 2026-04-03 | DOCSYS | UNISYS | TRANSFER_AUDIT*
