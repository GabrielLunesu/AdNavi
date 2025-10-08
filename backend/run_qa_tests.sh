#!/bin/bash
# Simple QA Test Runner
# Reads questions from qa_test_suite.md and logs results

WORKSPACE_ID="914019de-2190-4fcc-855a-d1e719d05cdc"
API_URL="http://localhost:8000/qa/?workspace_id=$WORKSPACE_ID"
COOKIE_FILE="../cookies.txt"
OUTPUT_FILE="qa_test_results.md"

# Colors for terminal output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "🧪 QA Test Suite Runner"
echo "======================="
echo ""

# Check if logged in
if [ ! -f "$COOKIE_FILE" ]; then
    echo "⚠️  Cookie file not found. Please login first:"
    echo "   curl -X 'POST' 'http://localhost:8000/auth/login' \\"
    echo "     -H 'Content-Type: application/json' \\"
    echo "     -d '{\"email\": \"owner@defanglabs.com\", \"password\": \"password123\"}' \\"
    echo "     -c cookies.txt"
    exit 1
fi

# Create output file with header
cat > $OUTPUT_FILE << EOF
# QA Test Results

**Test Run**: $(date)
**Workspace**: Defang Labs ($WORKSPACE_ID)
**System Version**: Phase 3 (v2.1.3)

---

EOF

# Test questions array (add more here!)
QUESTIONS=(
    # Basic Metrics
    "What's my CPC today?"
    "How much did I spend yesterday?"
    "What's my ROAS this week?"
    "How much revenue did I generate today?"
    "What's my conversion rate?"
    "How many clicks did I get last week?"
    
    # Comparisons
    "How does this week compare to last week?"
    "Compare Google vs Meta performance"
    "Is my ROAS improving or declining?"
    
    # Breakdowns
    "Which campaign had the highest ROAS last week?"
    "Show me top 5 campaigns by revenue"
    "List all active campaigns"
    
    # Analytical
    "Why is my ROAS volatile?"
    "Explain my spend trend"
    
    # Filters
    "What's my ROAS for active campaigns?"
    "How much did I spend on Meta ads?"
    
    # Edge Cases
    "How much revenue on Google last week?"
    "What's my cost per install?"
    "How many leads did I generate today?"
)

total=${#QUESTIONS[@]}
current=0

# Run each question
for question in "${QUESTIONS[@]}"; do
    current=$((current + 1))
    
    echo -e "${BLUE}[$current/$total]${NC} Testing: $question"
    
    # Make API call
    response=$(curl -s -X 'POST' "$API_URL" \
        -H 'Content-Type: application/json' \
        -b "$COOKIE_FILE" \
        -d "{\"question\": \"$question\"}")
    
    # Extract answer and DSL
    answer=$(echo "$response" | jq -r '.answer // "ERROR"')
    dsl=$(echo "$response" | jq -c '.executed_dsl // {}')
    
    # Check if successful
    if [ "$answer" != "ERROR" ] && [ "$answer" != "null" ]; then
        echo -e "  ${GREEN}✓${NC} Got answer"
    else
        echo -e "  ${RED}✗${NC} Failed"
    fi
    
    # Append to output file
    cat >> $OUTPUT_FILE << EOF
## Test $current: $question

**Answer**:
> $answer

**DSL**:
\`\`\`json
$(echo "$dsl" | jq '.')
\`\`\`

---

EOF
    
    # Small delay to avoid rate limiting
    sleep 0.5
done

echo ""
echo "✅ Test run complete!"
echo "📄 Results saved to: $OUTPUT_FILE"
echo ""
echo "Summary:"
echo "  Total questions: $total"
echo "  Results file: $OUTPUT_FILE"
echo ""
echo "To view results: cat $OUTPUT_FILE"

