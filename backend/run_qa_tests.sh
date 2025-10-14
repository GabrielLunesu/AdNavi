#!/bin/bash
# Simple QA Test Runner

WORKSPACE_ID="9c76b246-faf1-42d6-9a5a-f564f7801b4e"
API_URL="http://localhost:8000/qa/?workspace_id=$WORKSPACE_ID"
COOKIE_FILE="../cookies.txt"
TEST_RESULTS_DIR="test-results"
OUTPUT_FILE="$TEST_RESULTS_DIR/qa_test_results-phase-5-9.md"

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

# Login and get cookies
echo -e "${BLUE}→${NC} Logging in..."
login_response=$(curl -s -X 'POST' 'http://localhost:8000/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"email": "owner@defanglabs.com", "password": "password123"}' \
  -c "$COOKIE_FILE")

# Check if login was successful
user_email=$(echo "$login_response" | jq -r '.user.email // empty')
if [ -z "$user_email" ]; then
    echo -e "${RED}✗${NC} Login failed"
    echo "Response: $login_response"
    exit 1
fi

echo -e "${GREEN}✓${NC} Logged in as: $user_email"
echo -e "${GREEN}✓${NC} Workspace ID: $WORKSPACE_ID"
echo ""

# Create output file with header
cat > $OUTPUT_FILE << EOF
# QA Test Results

**Test Run**: $(date)
**Workspace**: Defang Labs ($WORKSPACE_ID)
**System Version**: Phase 5 (v2.1.3)

---

EOF

# Test questions array (add more here!)
QUESTIONS=(
    # Basic Metrics
    "What's my CPC this month?"
    "How much did I spend this month?"
    "What's my ROAS this week?"
    "How much revenue did I generate yesterday?"
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
    "What was the revenue for the Holiday Sale campaign last week?"
    "wich day had the lowest cpc on holiday sale campaign?"
    "roas last month for holiday sale campaign?"
    "wich had highest cpc, holiday campaign or app install campaign?"
    "wich google campaigns are live?"
    "what is my revenue this month?"
    "what was my revenue last month?"
    "what is my revenue this year?"

   
    
    # Comparisons
    "How does this week compare to last week?"
    "Compare Google vs Meta performance"
    "Is my ROAS improving or declining?"
    "compare holiday campaign performance to app install campaign performance"

    
    # Breakdowns
    "Which campaign had the highest ROAS last week?"
    "Show me top 5 campaigns by revenue"
    "List all active campaigns"
    "Which adset had the highest cpc last week?"
    "Which adset had the highest cpc last week?"
    "Which adset had the lowest ctr last week?"
    "what is my total CVR last month?"
    "what is my cvr on google last month?"

        
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

    # Multi-Entity + Multi-Metric + Time Range Tests
    "Compare CPC, CTR, and ROAS for Holiday Sale and App Install campaigns last week"
    "What's the spend, revenue, and ROAS for all Google campaigns in September?"
    "Show me clicks, conversions, and cost per conversion for Meta campaigns last 5 days"
    "Give me CTR, CPC, and conversion rate for Summer Sale campaign last month"
    "Compare spend and revenue between Morning Audience and Evening Audience adsets this month to date"
    "What's the ROAS, revenue, and profit for Black Friday campaign last week?"
    "Show me CPC, clicks, and spend for all active campaigns last 5 days"
    "Compare CTR and conversion rate for Google vs Meta campaigns in September"
    "What's the revenue, ROAS, and cost per lead for lead gen campaigns this month to date?"
    "Give me spend, clicks, and CPC for Holiday Sale and Summer Sale campaigns last month"
    "Show me conversion rate, revenue, and profit for all campaigns last week"
    "Compare CPA, ROAS, and revenue for App Install campaign vs Holiday Sale campaign last 5 days"
    "What's the CTR, CPC, and conversions for Weekend Audience adsets in September?"
    "Give me spend, revenue, ROAS, and profit for all Meta campaigns this month to date"
    "Compare clicks, CTR, and cost per click for Morning vs Evening Audience adsets last month"

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

