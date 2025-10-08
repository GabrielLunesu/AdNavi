# QA Testing Guide - Simple & Expandable

## Quick Start

### 1. Login (one time)
```bash
cd /Users/gabriellunesu/Git/AdNavi
curl -X 'POST' 'http://localhost:8000/auth/login' \
  -H 'Content-Type: application/json' \
  -d '{"email": "owner@defanglabs.com", "password": "password123"}' \
  -c cookies.txt
```

### 2. Run Tests
```bash
cd backend
./run_qa_tests.sh
```

### 3. View Results
```bash
cat test-results/qa_test_results.md
```

---

## How It Works

1. **Questions**: Edit `qa_test_suite.md` to add/remove questions
2. **Script**: `run_qa_tests.sh` reads questions and calls API
3. **Results**: `test-results/qa_test_results.md` logs answers + DSL for each question
4. **Repeat**: Run script anytime to test changes

---

## Adding Your Own Questions

**Edit `qa_test_suite.md`**:

```markdown
### Custom Questions

41. How is my Holiday Sale campaign doing?
42. What's my profit this month?
43. Show me campaigns with low ROAS
```

Then run `./run_qa_tests.sh` again!

---

## What You'll See in Results

For each question, you get:

**Answer** (what the AI said):
> "Your ROAS was 4.36× last week."

**DSL** (how it was translated):
```json
{
  "metric": "roas",
  "time_range": {"last_n_days": 7},
  "timeframe_description": "last week"
}
```

This helps you:
- Verify answer quality
- Check DSL translation accuracy
- Track improvements over time
- Debug issues

---

## Use Cases

### Testing New Features
Add questions for new features, run tests, verify they work

### Regression Testing
Keep old questions, re-run after changes, ensure nothing broke

### Quality Review
Review all answers at once, identify patterns in good/bad answers

### Incremental Expansion
Add 1-2 questions at a time as you think of them

---

## Tips

**Start Small**: Test with 5-10 questions first  
**Be Specific**: Add questions that represent real user needs  
**Track Changes**: Git commit results file to see improvements over time  
**Iterate**: Add questions when you find edge cases

---

## Example Workflow

```bash
# Day 1: Initial test
cd backend
./run_qa_tests.sh
git add qa_test_results.md
git commit -m "test: baseline QA results"

# Day 2: Add new feature, re-test
vim qa_test_suite.md  # Add questions for new feature
./run_qa_tests.sh
git diff qa_test_results.md  # See what changed!

# Day 3: Found edge case, add test
echo "45. What if I have no campaigns?" >> qa_test_suite.md
./run_qa_tests.sh
# Check if it handles edge case gracefully
```

---

**That's it!** Super simple, infinitely expandable, no complex test infrastructure needed.

