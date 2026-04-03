UNISYS Copilot Synchronization Kit
Canonical Operator Context — Cross-Platform Deployment Guide

Author: Kyle Breneman   |   Date: 2026-04-03

Classification: DOCSYS   |   Status: Canonical Reference

1   Architecture Overview
This document establishes a single canonical understanding of Kyle's work, environment, and experiences across three Microsoft Copilot surfaces:

Surface	Context Mechanism	Format	Deployment
Copilot Chat (this surface)	Memory facts	Individual stored facts	Already active — 40+ facts stored
Microsoft 365 Copilot	Custom Instructions + Copilot Memory	Free-form text (Settings → Personalization)	Manual paste into settings
GitHub Copilot	Repository instruction file	Markdown file at .github/copilot-instructions.md	Commit to repository root
Synchronization model: The three surfaces cannot directly communicate with each other. Instead, this kit provides a hub-and-spoke architecture:

Hub: The Canonical Context Document (Section 4) is the single source of truth
Spokes: Platform-specific instruction files (Sections 5 and 6) are derived from the hub, optimized for each platform's constraints
Updates: When UNISYS changes, update the Canonical Context first, then propagate to each spoke
2   Deployment — Microsoft 365 Copilot
DESTINATION
M365 Copilot → Settings (⋯ menu, top right) → Personalization → Custom Instructions → Edit Instructions
Steps
Open Microsoft 365 Copilot Chat (copilot.microsoft.com or the M365 app)
Click the three-dot menu (⋯) at the top right
Select Settings
In the left menu, select Personalization
Ensure the Custom Instructions toggle is ON
Click Edit Instructions
Paste the full text from Section 5 of this document
Click Save Instructions
Notes
Custom instructions have a character limit (~1500 chars). The provided text is optimized to fit.
M365 Copilot also has Copilot Memory which learns from conversations over time. The custom instructions give it a head start on UNISYS context.
Custom instructions apply to all future M365 Copilot Chat conversations automatically.
You can also tell M365 Copilot to "remember" specific facts in conversation to build its memory over time.
3   Deployment — GitHub Copilot
DESTINATION
.github/copilot-instructions.md in the root of each repository
Steps
In your repository root, create the .github/ directory if it doesn't exist
Create a file named copilot-instructions.md inside .github/
Paste the full text from Section 6 of this document
Commit and push
Advanced Options
Path-specific instructions: Create .github/instructions/NAME.instructions.md files with applyTo frontmatter for file-type-specific rules (e.g., Python conventions, Excel macro patterns)
Agent instructions: Create AGENTS.md in any directory for AI agent-specific behavior
VS Code setting: Ensure "Code Generation: Use Instruction Files" is enabled in VS Code settings (it's on by default)
Recommended Per-Repository Additions
Repository Type	Recommendation
ACCTSYS repos	Add path-specific instructions for financial calculation conventions
DOCSYS repos	Add path-specific instructions for document template generation patterns
DEVICEOPS repos	Add path-specific instructions for hardware configuration schemas
4   Canonical Context Document (Master Reference)
AUTHORITY NOTICE
This is the authoritative source. All platform-specific files (Sections 5 and 6) are derived from this section. When UNISYS changes, update this section first.
Kyle Breneman — Canonical Operator Context
Purpose: Single source of truth for all Copilot surfaces (Microsoft 365 Copilot, GitHub Copilot, Copilot Chat). Maintain this document as the authoritative reference; derive platform-specific instruction files from it.

4.1   Identity & Environment
Field	Value
Name	Kyle Breneman (kabreneman)
Location	Salina, Kansas, United States
Education	Bachelor of Business Administration, Washburn University
Potential Company Name	Nine Displaced (noun TBD)
Vehicle	2013 Ford Edge SEL — 3.5L V6 Ti-VCT, SAE 5W-20, 6.0 qt capacity, Motorcraft FL-500-S filter
4.2   Communication & Style
Structured, operator-centric communication
Prefers explicit rules and audit-ready clarity
Corrects terminology proactively for future-proofing
Values canonical placement and minimal ambiguity
Modifier "All New" means never created before — not a revision, edition, or version of any current element
Temperature/environmental observations should include optimal and tolerated values alongside Fahrenheit and inHg conversions
4.3   UNISYS — Unified Information System
UNISYS is Kyle's personal canonical information architecture spanning documents, assets, finances, devices, and life operations.

4.3.1   Systems & Class Letters
System-scoped class letters:

Letter	System	Full Name
P	DOCSYS	Document System
S / J / L	ACCTSYS	Account System
A	ANALYTICS	Analytics
D	DOCCTRL	Document Control
T	TRUSTSYS	Trust System
H	HOUSESYS	House System
U	UTILSYS	Utility System
R	REDOREPO	Redo Repository
E	ERRSYS	Error System
V	DEVICEOPS	Device Operations
B	BRANDREG	Brand Registry
K	FOODSYS	Food System
O	LIFEOPS	Life Operations
F	CLEANAPT	Deprecated — absorbed into HOUSESYS / ENVAPT
Available letters: C, G, I, M, N, Q, W, X, Y, Z

A-LAUN-01: Laundry Antimicrobial Authority (Life System, parallel to CLEANAPT)

4.3.2   Filename Convention (Pre-UNISYS)
FORMAT
[System] [Endeavor] Document [yyyy-mm-dd] yyyy-mm-dd.ext
Brackets denote optional parameters. Parentheses do not inherently appear in filenames; they only exist when specifically requested.
Parentheticals are optional. First date = date created. Second date = date saved/modified (only included if different from created).

4.3.3   Identity Schema
Identifier	Purpose	Assignment Rule
TSN	Global event identifier	Assigned first
AUID	Published or archivable intellectual property	Assigned after TSN
Document ID	Reproducible, versioned files	Identifies files, not events
Narrative ID	Creative prose	Metadata-driven, not chronological
UDIS	Serial numbers for artifacts only	Never merged with external numbering
Templates and artifacts are separate identity layers. Templates never receive AUIDs; completed artifacts always do. External numbering schemes identify templates and must never merge with artifact identity.

4.3.4   NDS Scope System
Scope	Definition
PANORAMA	Broadest scope
MONOGRAPH	Single-subject deep dive
MONORAMA	Single-subject overview
OLIGORAMA	Few-subject overview
POLYGRAPH	Multi-subject deep dive
PANOGRAPH	Multi-subject broad stroke
4.3.5   Acquisition Workflow
When the prompt "Acquisition" is issued, automatically execute:

Generate Acquisition Record (CL-Class)
Generate Asset Intake Form (F-INTAKE-01)
Generate Cataloging Entry
Each with proper TSN, UDIS, and AUID identifiers.

4.3.6   Dependency Architecture
Dynamic metadata is a prequel to DOCSYS
WORKCAP parsing and DOCSYS normalization are canonical workflow steps
The system aims to economize and consolidate document classes into a unified minimal architecture
TSN.LOG generator provides deterministic asset identity assignment
4.4   Financial Systems
WORKCAP: Working capital restoration project starting June 1, 2025. Goal: 90-day reserve. AY-LIQ = Analysis: Liquidity.

Federal student loan (Nelnet):

Field	Value
Balance	$20,119.61
Unpaid accrued interest	$635.80
Daily interest accrual	$2.28
Amount due	$0 due until 11/04/2028
Excess payment strategy	Applied lowest-balance-first (snowball)
Debt payments allocated via DDS-style priority: interest → fees → principal. Crypto FIFO ledger: UNISYS-compliant.

4.5   Technology & Hardware
Prioritizes RAM and graphics
Required ports/features: CD/DVD burner, Ethernet, Bluetooth, USB-A, USB-C, HDMI, 3.5mm audio
Portability: couch, bed, table, backpack
Prefers Logitech peripherals
"Hard drive" includes NVMe and any permanent storage
Unified modular kits; no redundancy
Audit-ready device architecture
Material-aware, aesthetic-aligned device naming
4.6   Personal & Lifestyle
Unicycle proficiency in progress
Emergency preparedness (indoor-safe power, clear-bag kit with mini NOAA radio)
Natural time/position determination (solar, lunar, stellar)
Inclusive travel and LGBTQ-friendly events
Values parks for romantic outings
Fond of Chicago (2010s), Salina, Manhattan, Wichita, and heated pool property near Salida/Cañon City, CO
4.7   Workflow & Operational Principles
Apartment maintained as operator-grade environment with repeatable, auditable workflows
No identity inflation for low-value assets
No namespace collisions
Lifecycle closure via acquisition/disposal event tracking
Check Pages for information during interactions
Outstanding Pages Index: create Page, then generate each one by one with proper IDs
4.8   Document Formatting
UNISYS formatting examples and style corpus stored as reference
Asset intake form chart stored
Debt extinguishment timelines enforce WC01 boundary integrity
Tax refund integrated as WC01 inflow with Net Cumulative Economic Effect boundary rules
Last updated: 2026-04-03

5   M365 Copilot Custom Instructions (Ready to Paste)
INSTRUCTIONS
Copy everything inside the box below and paste it into M365 Copilot Settings → Personalization → Custom Instructions.
I'm Kyle Breneman, based in Salina, Kansas. BBA from Washburn University. I maintain a personal information architecture called UNISYS (Unified Information System) that governs my documents, assets, finances, devices, and life operations.

Communication style: Structured, operator-centric. I prefer explicit rules, audit-ready clarity, canonical placement, and minimal ambiguity. I correct terminology proactively for future-proofing.

UNISYS uses system-scoped class letters: P=DOCSYS, S/J/L=ACCTSYS, A=ANALYTICS, D=DOCCTRL, T=TRUSTSYS, H=HOUSESYS, U=UTILSYS, R=REDOREPO, E=ERRSYS, V=DEVICEOPS, B=BRANDREG, K=FOODSYS, O=LIFEOPS. F=CLEANAPT is deprecated.

Identity schema: TSN (global event ID, assigned first), AUID (for published/archivable IP, assigned after TSN), Document IDs (reproducible versioned files), Narrative IDs (creative prose, metadata-driven). UDIS serial numbers are for artifacts only. Templates never receive AUIDs; completed artifacts always do.

Filename convention: System Endeavor Document yyyy-mm-dd yyyy-mm-dd.ext — System, Endeavor, and first date (date created) are optional; second date is modified (only if different). Parentheses do not inherently appear in filenames; they only exist when specifically requested.

WORKCAP is my working capital restoration project (started June 2025, goal: 90-day reserve). AY-LIQ = Analysis: Liquidity. Debt payments use a DDS-style priority algorithm (interest > fees > principal).

"All New" means never created before — not a revision of anything existing. My apartment is maintained as an operator-grade environment with repeatable, auditable workflows. I value unified modular systems with no identity inflation for low-value assets and no namespace collisions.

When I say "Acquisition," execute the full workflow: Acquisition Record (CL-Class), Asset Intake Form (F-INTAKE-01), Cataloging Entry — each with proper TSN, UDIS, and AUID.
6   GitHub Copilot Instructions (Ready to Commit)
INSTRUCTIONS
Save everything inside the box below as .github/copilot-instructions.md in your repository root.
# GitHub Copilot Instructions — Kyle Breneman (UNISYS)

## Operator Context

This repository is part of UNISYS (Unified Information System), a personal canonical information architecture governing documents, assets, finances, devices, and life operations. All code, scripts, and tooling produced here must align with UNISYS principles.

## Naming & Identity Conventions

- TSN (Transaction Serial Number): Global event identifier, always assigned first.
- AUID (Artifact Unique Identifier): Assigned after TSN for published or archivable intellectual property.
- UDIS (Universal Document Identity Serial): Serial numbers for artifacts only — never merge with external numbering schemes.
- Document IDs: Identify reproducible, versioned files.
- Narrative IDs: Identify creative prose; metadata-driven, not chronological.
- Templates and artifacts are separate identity layers. Templates never receive AUIDs; completed artifacts always do.

## System Class Letters

System-scoped prefixes used throughout the codebase and file taxonomy:
P = DOCSYS, S/J/L = ACCTSYS, A = ANALYTICS, D = DOCCTRL, T = TRUSTSYS, H = HOUSESYS, U = UTILSYS, R = REDOREPO, E = ERRSYS, V = DEVICEOPS, B = BRANDREG, K = FOODSYS, O = LIFEOPS. F = CLEANAPT (deprecated — absorbed into HOUSESYS/ENVAPT). Available: C, G, I, M, N, Q, W, X, Y, Z.

## Filename Convention

Format: System Endeavor Document yyyy-mm-dd yyyy-mm-dd.ext — System, Endeavor, and first date (date created) are optional. Second date = modified (only if different from created). Parentheses do not inherently appear in filenames; they only exist when specifically requested.

## Coding Preferences

- Prefer explicit, deterministic logic over implicit behavior.
- Variable and function names should reflect UNISYS terminology where applicable.
- No identity inflation: do not assign heavyweight identifiers to trivial elements.
- No namespace collisions: every identifier must be unambiguous within its scope.
- Audit-ready: code should produce traceable, reproducible outputs.
- When generating asset-related code, support the full identity stack: TSN → AUID → UDIS.

## Financial Domain

- WORKCAP: Working capital restoration project (FY-WC01 boundaries enforced).
- AY-LIQ: Analysis: Liquidity module.
- Debt payments use a DDS-style priority algorithm: interest → fees → principal.
- Crypto uses FIFO accounting; ledger must be UNISYS-compliant.
- Snowball method for excess loan payments (lowest-balance-first).

## NDS Scope System

PANORAMA (broadest scope), MONOGRAPH (single-subject deep dive), MONORAMA (single-subject overview), OLIGORAMA (few-subject overview), POLYGRAPH (multi-subject deep dive), PANOGRAPH (multi-subject broad stroke).

## Acquisition Workflow

The command "Acquisition" triggers a three-artifact generation: (1) Acquisition Record (CL-Class), (2) Asset Intake Form (F-INTAKE-01), (3) Cataloging Entry — each must include proper TSN, UDIS, and AUID identifiers.

## General Principles

- Modifier "All New" = never created before, not a revision of any current element.
- Dynamic metadata is a prequel to DOCSYS.
- The system aims to economize and consolidate document classes into a unified minimal architecture.
- TSN.LOG generator provides deterministic asset identity assignment.
- Lifecycle closure via acquisition/disposal event tracking.
7   Maintenance Protocol
When to Update
Any change to UNISYS class letters, identity schema, or system architecture
New financial projects or debt milestones
New hardware configurations or device acquisitions
Changes to workflow principles or operational standards
Update Sequence
Update this document (the Canonical Context, Section 4) first
Regenerate the M365 Custom Instructions (Section 5) and re-paste into settings
Regenerate the GitHub instructions (Section 6) and commit to all active repositories
Tell Copilot Chat (this surface) about the change — it will update its memory automatically
VERSION CONTROL
Keep this document in a UNISYS-compliant location.
Recommended filename: DOCSYS Copilot Synchronization Kit 2026-04-03.docx
— End of Document —