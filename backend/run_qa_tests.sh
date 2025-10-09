#!/bin/bash
# Simple QA Test Runner

WORKSPACE_ID="9d75665c-cd01-40f1-82df-a52d56b6d749"
API_URL="http://localhost:8000/qa/?workspace_id=$WORKSPACE_ID"
COOKIE_FILE="../cookies.txt"
TEST_RESULTS_DIR="test-results"
OUTPUT_FILE="$TEST_RESULTS_DIR/qa_test_results-phase-5-6.md"

# Create test-results directory if it doesn't exist
mkdir -p "$TEST_RESULTS_DIR"

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
    "How much profit did I make last week?"
    "How many leads did I generate this month?"
    "What is my cost per lead this month?"
    "Which campaign had the highest ROAS last week?"
    "What's my ROAS for Google campaigns only?"
    "Which campaign spent the most yesterday?"
    "List all active campaigns"
    "Which ad has the highest CTR?"
    "Show me campaigns with ROAS above 4"
    "Which campaign generated the most leads?"
    "Rank platforms by cost per conversion"
    "give me a breakdown of holiday campaign performance"
    "what is my average order value?"
    "give me a list of the top 5 adsets last week by revenue"
   
    
    # Comparisons
    "How does this week compare to last week?"
    "Compare Google vs Meta performance"
    "Is my ROAS improving or declining?"
    
    # Breakdowns
    "Which campaign had the highest ROAS last week?"
    "Show me top 5 campaigns by revenue"
    "List all active campaigns"
    "Which adset had the highest cpc last week?"
    "Which adset had the lowest ctr last week?"
    "Which adset had the highest ctr last week?"
    "Which adset had the lowest cpc last week?"
    "Which adset had the highest cpc last week?"
    "Which adset had the lowest ctr last week?"
    "what is my total CVR last month?"
        
    # Filters
    "What's my ROAS for active campaigns?"
    "How much did I spend on Meta ads?"
    
    # Edge Cases
    "How much revenue on Google last week?"
    "What's my cost per install?"
    "How many leads did I generate today?"

    # User generated Questions
    "wich ad had the lowest cpc last week?"
    "What time on average do i get the best cpc?"
    "how much revenue would i have last week if my cpc was 0.20?"
    ""
    
    # NEW Phase 5: Named Entity Filtering Tests
    "How is the Summer Sale campaign performing?"
    "Show me all lead gen campaigns"
    "What's the CPA for Morning Audience adsets?"
    "What's the revenue for Black Friday campaign?"
    "Give me ROAS for App Install campaigns"
    "Show me Weekend Audience adsets"
    "What's the CTR for Evening Audience adsets?"
    "How much did Holiday Sale campaign spend last week?"

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

