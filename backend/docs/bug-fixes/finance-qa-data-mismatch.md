# Finance vs QA Data Mismatch Bug Fix

**Date**: October 14, 2025  
**Severity**: Critical  
**Status**: Fixed ✅

## What Went Wrong

The Finance page was showing different revenue numbers than the Copilot QA system for the same time period.

### Example Problem
- **Finance page shows**: $725,481.04 total revenue for October 2025
- **Copilot QA answers**: $654,019.32 revenue for October 1-14, 2025
- **Problem**: Different revenue calculations for overlapping periods! 

## Why This Happened

The QA system was incorrectly filtering to active entities only, while Finance correctly included ALL entities (active + inactive).

### Root Cause
- **Finance P&L endpoint**: Correctly includes ALL entities (active + inactive/paused campaigns)
- **QA system**: Was incorrectly filtering to active entities only (after our previous "fix")
- **Impact**: QA showed lower revenue because it excluded inactive campaigns that still generated revenue

### Technical Details
The QA system was applying `E.status == "active"` filter by default, while Finance correctly includes all entities because inactive campaigns still generated revenue during their active period.

## How We Fixed It

**File**: `backend/app/dsl/executor.py`

**Before**:
```python
# QA system - incorrectly filtering to active entities only
if plan.filters.get("status"):
    base_query = base_query.filter(E.status == plan.filters["status"])
else:
    # WRONG: Default to active entities only
    base_query = base_query.filter(E.status == "active")
```

**After**:
```python
# QA system - now includes ALL entities by default
if plan.filters.get("status"):
    base_query = base_query.filter(E.status == plan.filters["status"])
# CORRECT: No default status filter - include all entities unless explicitly filtered
```

**Fixed in**: 6 locations in executor.py
- Main summary query, previous period comparison, timeseries query, breakdown query, multi-metric queries

## Testing Results

After the fix:
- **Finance P&L endpoint**: $725,481.04 revenue (unchanged - was correct)
- **QA system**: $725,481.04 revenue (now matches Finance)
- **Both systems**: Now return identical values for same time periods ✅

## Key Lessons

1. **Business Logic First**: Inactive campaigns still generated revenue and should be included in financial analysis
2. **Finance is the Source of Truth**: Finance page correctly includes all entities, QA should match this behavior
3. **Don't Filter by Default**: Only apply status filters when explicitly requested by the user
4. **Cross-System Testing**: Always test that different systems return consistent values for the same queries

## Files Changed

- `backend/app/dsl/executor.py` - Removed default active entity filter from QA system
- `backend/docs/bug-fixes/finance-qa-data-mismatch.md` - This documentation

## Prevention

To prevent similar bugs in the future:
1. **Don't filter by default**: Only apply status filters when explicitly requested
2. **Finance is the source of truth**: Use Finance page behavior as the reference for financial data
3. **Test cross-system consistency**: Always verify that different systems return consistent values
4. **Document business logic**: Clearly document why inactive campaigns should be included in financial analysis

---

*This bug fix ensures users get consistent, trustworthy financial data from both the Finance page and the Copilot QA system.*
