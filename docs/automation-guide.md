# Automation Guide for Work Documentation

This document describes how to automatically document work in this repository.

## Principles

**All work should be tracked** - whether planned in advance or completed ad-hoc.

## Workflows

### 1. Planned Work (Recommended)
```
Create Issue → Do Work → Create PR → Link to Issue → Merge
```

**Benefits**: Clear tracking, discussion space, automatic closure

### 2. Ad-Hoc Work (Acceptable)
```
Do Work → Commit → Create "[DONE]" Documentation Issue
```

**Use the Work Documentation template** to record:
- What was done and when
- Why it was done
- Who did it
- Related commits
- Follow-up actions needed

## Using Issue Templates

### Work Documentation Template
Located at: `.github/ISSUE_TEMPLATE/work-documentation.md`

**When to use**:
- Work completed without a prior issue
- Discoveries made during other work
- Quick fixes or improvements
- Documenting historical changes

**How to use**:
1. Go to Issues → New Issue
2. Select "Work Documentation" template
3. Fill in all sections
4. Title format: `[DONE] Brief description`
5. Assign to whoever did the work
6. Add relevant labels

## Commit Message Conventions

### Linking to Issues
- `Fixes #123` - Closes issue when merged
- `Closes #123` - Closes issue when merged
- `Resolves #123` - Closes issue when merged
- `Related to #123` - Links without closing

### For Ad-Hoc Work
Include in commit message:
```
Brief description of changes

- Detail 1
- Detail 2

[NOTE: Will document in issue post-commit]
```

Then immediately create documentation issue.

## Pull Request Template

The PR template includes:
- Checklist for documentation
- Reminder to create "[DONE]" issue if needed
- Post-merge action section

## GitHub Actions Automation

### Recommended Workflows (see #15)

1. **Commit Analyzer**
   - Detect commits without linked issues
   - Auto-create reminder comment
   - Suggest creating documentation issue

2. **PR Documentation Check**
   - Verify all PRs link to issues OR have documentation plan
   - Block merge if documentation missing

3. **Monthly Documentation Audit**
   - Scan recent commits
   - List undocumented work
   - Create audit issue

## Best Practices

### For Individual Contributors
✅ **Do**:
- Create issues before starting work when possible
- Document completed work immediately
- Use descriptive commit messages
- Link commits to issues

❌ **Don't**:
- Let undocumented work accumulate
- Assume "it's too small to document"
- Skip documentation for "obvious" changes

### For AI Assistants (Copilot, etc.)
✅ **Do**:
- Create issues for planned work
- Document completed work immediately after
- Use "[DONE]" prefix for after-the-fact documentation
- Assign to appropriate person
- Include commit hashes

❌ **Don't**:
- Complete work without creating documentation
- Bundle multiple unrelated changes in one issue
- Skip rationale sections

### For Repository Maintainers
✅ **Do**:
- Review undocumented commits regularly
- Enforce documentation requirements
- Keep templates up to date
- Set up GitHub Actions for automation

## Examples

### Good Documentation Issue
```
Title: [DONE] Fix duplicate imports in workcap_analyzer.py
Date: 2025-11-25
Completed by: @copilot
Changes:
- Removed duplicate shutil import (line 7)
- Removed duplicate time import (line 8)
Commit: 07be8a4
Related: Part of repository cleanup effort
```

### Good Commit Message
```
Fix duplicate imports in workcap_analyzer.py

- Remove duplicate shutil import
- Remove duplicate time import

Fixes #8
```

## Automation Setup (Future)

See issue #15 for implementing:
- GitHub Actions workflows
- Automatic documentation reminders
- Commit analysis
- Documentation audit reports

## Quick Reference

| Scenario | Action |
|----------|--------|
| Planning new work | Create issue first |
| Quick fix done | Create "[DONE]" issue immediately |
| Multiple commits | Create one issue for the feature |
| Historical work | Use work documentation template |
| Unsure if needed | Document it (better safe than sorry) |

## Contact

Questions about documentation? Comment on issue #5 (meta issue) or create a new issue.
