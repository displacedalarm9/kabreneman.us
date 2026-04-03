---
last_updated: 2025-06-05
version: 1.2.0
file_status: template
---

# Variance Report Templates

## References
[See: ../procedures/matrix.md for tolerance ranges]
[See: ../procedures/emergency.md for alert thresholds]
[See: ../standards.md for report requirements]

## Instructions
1. Copy appropriate template
2. Fill all fields marked [REQUIRED]
3. Store reports in `/reviews/variance/[year]/[month]/`
4. Update reference documents after completion:
   - Daily variances update procedures/matrix.md
   - Weekly variances update procedures/schedule.md
   - Monthly variances update WorkingCapital.md

## Daily Variance Report
| Category | Metric | Value | Status |
|----------|--------|-------|--------|
| **Header** [REQUIRED] | Date | [DATE] | - |
| | Reviewer | [NAME] | - |
| **Cash Position** | Target | $______ | [G/Y/R] |
| | Actual | $______ | [G/Y/R] |
| | Variance | $______ | [G/Y/R] |
| **Credit Status** | Target Usage | ___% | [G/Y/R] |
| | Actual Usage | ___% | [G/Y/R] |
| | Variance | ___% | [G/Y/R] |
| **Buffer Status** | Required | $110 | [G/Y/R] |
| | Current | $______ | [G/Y/R] |
| | Variance | $______ | [G/Y/R] |

## Weekly/Monthly Reports
| Category | Target | Actual | Variance | Status |
|----------|--------|--------|----------|--------|
| Distribution | $______ | $______ | $______ | [G/Y/R] |
| Buffer | $______ | $______ | $______ | [G/Y/R] |
| Debt Reduction | $______ | $______ | ___% | [G/Y/R] |
| Credit Score | ______ | ______ | ±______ | [G/Y/R] |

## Status Definitions
| Color | Range | Required Action |
|-------|-------|----------------|
| GREEN | Within ±5% | Continue monitoring |
| YELLOW | ±5-10% | Review needed |
| RED | Beyond ±10% | Immediate action |

[See: procedures/matrix.md for tolerance ranges]
[See: procedures/emergency.md for recovery protocols]
