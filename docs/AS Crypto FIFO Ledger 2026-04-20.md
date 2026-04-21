# L-1400C -- Crypto FIFO Ledger

**DOC ID:** L-1400C.01 R1
**AUID:** PENDING REDOREPO
**TSN:** PENDING
**Created:** 2026-04-20
**Governing System:** AS (Accounting System) under FINSYS
**Parent Ledger:** L-1400_ (General Asset Ledger)
**Method:** First In, First Out (FIFO)

---

## Purpose

UNISYS-compliant subsidiary asset ledger for tracking all cryptocurrency holdings. Implements FIFO lot-matching for cost basis determination, gain/loss calculation, and tax reporting.

---

## Section 1 -- Lot Registry (Acquisitions)

| Lot # | Date Acquired | Asset | Quantity | Unit Cost (USD) | Total Cost Basis (USD) | Source | Remaining Qty | Status |
|-------|--------------|-------|----------|----------------|----------------------|--------|---------------|--------|
| LOT-001 | | | | | | | | OPEN |
| LOT-002 | | | | | | | | OPEN |
| LOT-003 | | | | | | | | OPEN |

---

## Section 2 -- Disposition Log

| Disp # | Date Disposed | Asset | Qty Disposed | Proceeds (USD) | Matched Lots | Cost Basis Consumed (USD) | Gain/Loss (USD) | Holding Period | SGE Ref |
|--------|--------------|-------|-------------|----------------|-------------|--------------------------|----------------|---------------|---------|
| DISP-001 | | | | | | | | | |
| DISP-002 | | | | | | | | | |

---

## Section 3 -- FIFO Matching Procedure

1. Identify asset being disposed
2. Sort OPEN/PARTIAL lots by Date Acquired ascending
3. Consume from oldest lot first
4. Calculate Cost Basis Consumed and Holding Period per lot
5. Sum all Cost Basis Consumed for total disposition basis
6. Gain/Loss = Proceeds minus Total Cost Basis Consumed
7. Split SHORT-TERM and LONG-TERM if spanning lots
8. Update Remaining Qty and Status in Section 1

---

## Section 4 -- Running Balance by Asset

| Asset | Total Qty Held | Total Cost Basis (USD) | Avg Unit Cost (USD) | Oldest Open Lot | Lots Open |
|-------|---------------|----------------------|--------------------|--------------------|-----------|
| BTC | | | | | |
| ETH | | | | | |
| SOL | | | | | |

---

## Section 5 -- Annual Tax Summary

| Tax Year | ST Gains | ST Losses | LT Gains | LT Losses | Net Gain/Loss | Dispositions |
|----------|----------|-----------|----------|-----------|---------------|--------------|
| 2024 | | | | | | |
| 2025 | | | | | | |
| 2026 | | | | | | |

---

## Section 6 -- Fee Tracking

| Date | Asset | Fee Amount (USD) | Fee Type | Associated Lot or Disp | Notes |
|------|-------|-----------------|----------|------------------------|-------|
| | | | Trading Fee | | |
| | | | Gas/Network Fee | | |
| | | | Withdrawal Fee | | |

**Fee Treatment:** Acquisition fees added to cost basis. Disposition fees subtracted from proceeds. Transfer fees recorded but not taxable unless paid in crypto.

---

## Section 7 -- Reconciliation Log

| Date | Action | Before Balance | After Balance | Discrepancy | Resolution | TSN |
|------|--------|---------------|--------------|-------------|------------|-----|
| | | | | | | |

---

## Cross-References

- **Parent Ledger**: L-1400_ (General Asset Ledger)
- **Sibling Ledgers**: L-1400W (Wardrobe), L-1400E (Electronics)
- **Governing System**: AS -- FINSYS
- **Audit Authority**: REDOREPO via Weekly Audit-Sweep

---

*Living document governed by AS under FINSYS. All entries append-only. Corrections in Section 7 with TSN references.*
