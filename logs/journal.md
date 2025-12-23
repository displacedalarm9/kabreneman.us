---
last_updated: 2025-06-06
version: 1.0.0
file_status: log
---

# Double-Entry Journal Log

## References
- progress.md: Project adherence tracking
- accounts.md: Account positions
- matrix.md: Payment scheduling

## Journal Entries
| Date       | Description        | Debit Account | Credit Account | Debit | Credit | CSH Bal | SAV Bal | CR Bal |
|------------|-------------------|---------------|----------------|-------|---------|---------|---------|---------|
| 2024-06-01 | Interest Income   | SAV          | Interest Inc   | 0.04  | 0.04    | -       | 2.03    | -       |
// ...existing entries from progress.md...
Appendix A: Double-Entry Journal
| Date       | Description        | Debit Account | Credit Account | Debit | Credit | CSH Bal | SAV Bal | CR Bal |
|------------|-------------------|---------------|----------------|-------|---------|---------|---------|---------|
| 2024-06-01 | Interest Income   | SAV          | Interest Inc   | 0.04  | 0.04    | -       | 2.03    | -       |
| 2024-06-01 | Paycheck          | CSH          | Income         | 425.89| 425.89  | 425.89  | 2.03    | -       |
| 2024-06-01 | Short-term Debt 1 | Debt Expense | CSH           | 37.59 | 37.59   | 388.30  | 2.03    | -       |
| 2024-06-01 | Short-term Debt 2 | Debt Expense | CSH           | 89.14 | 89.14   | 299.16  | 2.03    | -       |
| 2024-06-01 | Short-term Debt 3 | Debt Expense | CSH           | 11.94 | 11.94   | 287.22  | 2.03    | -       |
| 2024-06-01 | Short-term Debt 4 | Debt Expense | CSH           | 42.58 | 42.58   | 244.64  | 2.03    | -       |
| 2024-06-01 | Pay Advance 1     | CSH          | Advance Liab   | 190.00| 190.00  | 434.64  | 2.03    | -       |
| 2024-06-01 | Short-term Loan   | CSH          | Loan Liab      | 175.00| 175.00  | 609.64  | 2.03    | -       |
| 2024-06-01 | CR MCC Payment 1  | CR Expense   | CSH           | 47.34 | 47.34   | 562.30  | 2.03    | -47.34  |
| 2024-06-01 | CR MCC Payment 2  | CR Expense   | CSH           | 200.00| 200.00  | 362.30  | 2.03    | -247.34 |
| 2024-06-01 | Pay Advance 2     | CSH          | Advance Liab   | 50.00 | 50.00   | 412.30  | 2.03    | -247.34 |
| 2024-06-01 | Rent Payment      | Rent Expense | CSH           | 550.00| 550.00  | 18.23   | 2.03    | -247.34 |
| 2024-06-01 | Dad Loan Adj      | NP Dad       | CSH           | -165.00| -165.00  | 18.23   | 2.03    | -423.04 |
| 2024-06-01 | CR MCC Balance Adj| CR Expense   | CSH           | -27.07 | -27.07   | 18.23   | 2.03    | -423.04 |
| 2024-06-01 | CR MCC Payment    | CR Expense   | CSH           | 200.00 | 200.00  | -181.77 | 2.03    | -223.04 |
| 2024-06-08 | CD Loan Payment   | Loan Expense | CSH           | 55.00  | 55.00   | -36.77  | 2.03    | -223.04 |
| 2024-06-08 | McDonalds         | Food/Drink   | CR MCC        | 1.52   | 1.52    | -36.77  | 2.03    | -224.56 |
| 2024-06-08 | Gas               | Transport    | CR MCC        | 42.44  | 42.44   | -36.77  | 2.03    | -267.00 |
| 2024-06-08 | Dad Payment       | Debt Expense | CSH           | 165.00 | 165.00  | -201.77 | 2.03    | -267.00 |

[See: ../procedures/matrix.md for payment protocols]
