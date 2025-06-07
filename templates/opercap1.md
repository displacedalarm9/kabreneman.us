---
last_updated: 2025-06-06
version: 1.2.0
file_status: archive
---

# OPERCAP1 Report Templates

## References
- review.md: Daily report updates
- matrix.md: Weekly report updates
- WorkingCapital.md: Monthly report updates
- emergency.md: Emergency protocols
- procedures/matrix.md: Variance tolerances

## Instructions
1. Copy appropriate template
2. Fill all fields marked [REQUIRED]
3. Store completed reports in `/reports/[year]/[month]/`
4. Update reference documents after completion:
   - Daily reports update review.md
   - Weekly reports update matrix.md
   - Monthly reports update WorkingCapital.md
   - Emergency reports update emergency.md

## Weekly Status Report Template
| Category | Metric | Value | Status |
|----------|--------|--------|--------|
| **Header** [REQUIRED] | Week of | [DATE] | - |
| | Phase | [PHASE] | - |
| **Cash Position** | Starting Balance | $______ | [OK/WATCH/ALERT] |
| | Ending Balance | $______ | [OK/WATCH/ALERT] |
| | Net Change | $______ | [OK/WATCH/ALERT] |
| **Distribution** | Planned | $______ | [OK/WATCH/ALERT] |
| | Executed | $______ | [OK/WATCH/ALERT] |
| | Variance | $______ | [OK/WATCH/ALERT] |
| **Credit Status** | CR MCC Utilization | ___% | [OK/WATCH/ALERT] |
| | CR VFB Utilization | ___% | [OK/WATCH/ALERT] |

## Monthly Progress Report Template
| Category | Metric | Value | Status |
|----------|--------|--------|--------|
| **Header** [REQUIRED] | Month | [MONTH] 2025 | - |
| | Phase | [PHASE] | - |
| **Financial Position** | Starting Net Worth | $______ | [OK/WATCH/ALERT] |
| | Ending Net Worth | $______ | [OK/WATCH/ALERT] |
| | Change | ______% | [OK/WATCH/ALERT] |
| **Key Metrics** | Debt Reduction | ______% | [OK/WATCH/ALERT] |
| | Buffer Status | $______ | [OK/WATCH/ALERT] |
| | Credit Score | ______ | [OK/WATCH/ALERT] |

## Emergency Response Template
| Category | Metric | Value | Priority |
|----------|--------|--------|----------|
| **Header** [REQUIRED] | Date | [DATE] | - |
| | Trigger | [EVENT] | - |
| **Resources** | Available Cash | $______ | HIGH |
| | Next Income | $______ | HIGH |
| | Required Funds | $______ | HIGH |
| **Response** | Action Taken | [ACTION] | HIGH |
| | Response Made | [RESPONSE] | HIGH |
| | Result | [RESULT] | HIGH |

## Status Definitions
| Status | Definition | Required Action |
|--------|------------|----------------|
| OK | Within tolerance | Continue monitoring |
| WATCH | Near tolerance limit | Increase monitoring |
| ALERT | Outside tolerance | Immediate action required |

[See: procedures/matrix.md for variance tolerances]
[See: procedures/emergency.md for emergency protocols]
