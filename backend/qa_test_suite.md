# QA Test Suite - Incremental Testing Log

**Purpose**: Simple test file to track question → answer quality over time  
**Usage**: Run `./run_qa_tests.sh` to execute all questions and log results  
**How to expand**: Just add new questions under any category

---

## Test Questions

### Basic Metrics (1-10)

1. What's my CPC today?
2. How much did I spend yesterday?
3. What's my ROAS this week?
4. How much revenue did I generate today?
5. What's my conversion rate?
6. How many clicks did I get last week?
7. What's my CTR?
8. What's my cost per acquisition last month?
9. How many conversions this week?
10. What's my spend this month?

### Comparisons (11-15)

11. How does this week compare to last week?
12. Compare Google vs Meta performance
13. Is my ROAS improving or declining?
14. How does my CTR this month compare to last month?
15. Compare my CPC from this week to last week

### Breakdowns & Rankings (16-25)

16. Which campaign had the highest ROAS last week?
17. Show me top 5 campaigns by revenue
18. Which ad set has the lowest CPC?
19. Rank my campaigns by conversion rate
20. List all active campaigns
21. Which campaign spent the most yesterday?
22. Show me campaigns with ROAS above 4
23. Which platform gives me the best ROAS?
24. Which campaign generated the most leads?
25. Show me top 3 campaigns by clicks

### Analytical Questions (26-30)

26. Why is my ROAS volatile?
27. Explain my spend trend
28. Why did my CPC increase?
29. Analyze my campaign performance
30. What's happening with my conversion rate?

### Filter Queries (31-35)

31. What's my ROAS for active campaigns?
32. How much did I spend on Meta ads?
33. Show me revenue from TikTok
34. What's my Google campaign performance?
35. How are paused campaigns performing?

### Edge Cases (36-40)

36. How much revenue on Google last week? (missing platform)
37. What's my cost per install? (might be zero)
38. Show me campaigns with zero conversions
39. What's my ROAS for campaign "Holiday Sale"?
40. How many leads did I generate today? (no data yet)

---

## Add Your Own Questions Here

### Custom Questions

41. [Add your question here]
42. [Add your question here]
43. [Add your question here]

---

**Instructions**:
1. Add questions to any category above
2. Run `./run_qa_tests.sh` to test all questions
3. Results will be appended to this file with timestamp
4. Review answers and DSL to track improvements

