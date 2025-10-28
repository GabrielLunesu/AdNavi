#!/bin/bash
# Simple QA Test Runner

WORKSPACE_ID="4e0fcdf8-cd09-46f9-ae6a-5bcbc68b0199"
API_URL="http://localhost:8000/qa/?workspace_id=$WORKSPACE_ID"
COOKIE_FILE="../cookies.txt"
TEST_RESULTS_DIR="test-results"
OUTPUT_FILE="$TEST_RESULTS_DIR/qa_test_results-phase-6-2.md"
LOG_FILE="qa_logs.txt"

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

# Check if API is already running
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} API server is already running"
    echo ""
    echo "⚠️  IMPORTANT: For logs to appear in test results, the API must be"
    echo "   running with output redirected to the log file."
    echo ""
    echo "   Please restart your API server with:"
    echo "   ${BLUE}python start_api.py 2>&1 | tee qa_logs.txt${NC}"
    echo ""
    echo "   Or run the API in the test directory and use tee:"
    echo "   ${BLUE}cd backend && python start_api.py 2>&1 | tee qa_logs.txt${NC}"
    echo ""
    echo "Press Enter to continue with tests (logs may be empty)..."
    read
    echo ""
else
    echo -e "${RED}✗${NC} API server is not running"
    echo "Starting API server in background with logs..."
    python start_api.py > "$LOG_FILE" 2>&1 &
    API_PID=$!
    echo "API server started with PID: $API_PID"
    echo "Waiting for API to be ready..."
    sleep 5
    
    # Wait for API to be ready
    for i in {1..30}; do
        if curl -s http://localhost:8000/health > /dev/null 2>&1; then
            echo -e "${GREEN}✓${NC} API server is ready"
            break
        fi
        sleep 1
    done
    echo ""
fi

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

# Extract cookie value from cookie file
COOKIE_VALUE=$(grep "access_token" "$COOKIE_FILE" | awk -F'\t' '{print $7}' | tr -d '"')

echo -e "${GREEN}✓${NC} Logged in as: $user_email"
echo -e "${GREEN}✓${NC} Workspace ID: $WORKSPACE_ID"
echo -e "${GREEN}✓${NC} Cookie extracted"
echo ""

# Truncate log file to start fresh (avoids growing too large)
if [ -f "$LOG_FILE" ]; then
    > "$LOG_FILE"
fi

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

    # follow up questions
    "how much did i spent last month?"
    "wich campaign had the highest spend?"
    "wich ads in that campaign performed best?"
    "how many conversions did that campaign deliver?"
    "how much revenue in the last week?"
    "wich campaign brought in the most?"
    "how many conversions did that campaign deliver?"


        
    # Filters
    "What's my ROAS for active campaigns?"
    "How much did I spend on Meta ads?"
    
    # Edge Cases
    "How much revenue on Google last week?"
    "What's my cost per install?"
    "How many leads did I generate today?"

    # User generated Questions
    "wich ad had the lowest cpc last week?"
    "how much revenue would i have last week if my cpc was 0.20?"
    "best performing ad set in Holiday Sale campaign yesterday?"
    "all ad sets above roas 4 in the last 3 days"
    "which campaign has the highest ctr?"
    "show me adsets with cpc below 1 dollar"
    "worst performing ad in App Install campaign?"
    "all campaigns with conversion rate above 5%"
    "which adset spent the most money?"
    "show me ads with revenue above 1000"
    "best performing campaign by profit margin"
    "all adsets with clicks above 500"
    "which ad has the lowest cost per conversion?"
    "show me campaigns with impressions over 10000"
    "worst performing adset by roas"
    "all ads with ctr above 3%"
    "which campaign generated the most leads?"
    "show me adsets with spend below 50 dollars"
    "best performing ad by revenue per click"
    "all campaigns with cpm under 10 dollars"
    "which adset has the highest conversion rate?"
    "show me ads with conversions above 20"
    "worst performing campaign by cost per lead"
    "all adsets with revenue above 5000"
    "which ad has the best profit margin?"
    "show me campaigns with clicks over 1000"
    "best performing adset by average order value"
    "all ads with spend above 200 dollars"
    "which campaign has the lowest cost per acquisition?"
    "show me adsets with impressions over 5000"

    
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
    
    # Capture current log file size BEFORE making the API call
    # This way we know where to start reading from after the API call
    log_start_size=""
    if [ -f "$LOG_FILE" ]; then
        log_start_size=$(wc -l < "$LOG_FILE" | tr -d ' ')
    fi
    
    # Make a single API call and capture both response body and HTTP status code
    # The -w "\\n%{http_code}" appends the status code on a new line to the response
    response_with_code=$(curl -s -w "\\n%{http_code}" -X 'POST' "$API_URL" \
        -H 'Content-Type: application/json' \
        -H "Cookie: access_token=$COOKIE_VALUE" \
        -d "{\"question\": \"$question\"}")
    
    # Extract the HTTP status code (last line)
    http_code=$(echo "$response_with_code" | tail -n1)
    # Extract the response body (everything except the last line)
    response=$(echo "$response_with_code" | sed '$d')
    
    # Extract answer and DSL
    answer=$(echo "$response" | jq -r '.answer // "ERROR"')
    dsl=$(echo "$response" | jq -c '.executed_dsl // {}')
    
    # Small delay to ensure logs are flushed to disk
    sleep 0.3
    
    # Capture logs for this test (ONLY new logs added after API call)
    test_logs=""
    if [ -f "$LOG_FILE" ] && [ -n "$log_start_size" ]; then
        # Read from the log_start_size+1 line onwards (new logs only)
        total_lines=$(wc -l < "$LOG_FILE" | tr -d ' ')
        if [ "$total_lines" -gt "$log_start_size" ]; then
            lines_to_read=$((total_lines - log_start_size))
            # Get only the new lines and filter for relevant markers
            # Add debug output for first 3 tests
            if [ "$current" -le 3 ]; then
                echo "  Debug: Reading $lines_to_read new lines from log file"
            fi
            test_logs=$(tail -n "$lines_to_read" "$LOG_FILE" | grep -E "\[QA_PIPELINE\]|\[COMPARISON\]|\[UNIFIED_METRICS\]|\[ENTITY_CATALOG\]")
        else
            if [ "$current" -le 3 ]; then
                echo "  Debug: No new log lines (start: $log_start_size, total: $total_lines)"
            fi
        fi
    fi
    
    # Check if successful
    if [ "$answer" != "ERROR" ] && [ "$answer" != "null" ]; then
        echo -e "  ${GREEN}✓${NC} Got answer"
    else
        echo -e "  ${RED}✗${NC} Failed (HTTP $http_code)"
        echo "  Response: $response"
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

**Logs**:
\`\`\`
$test_logs
\`\`\`

---

EOF
    
    # Small delay to avoid rate limiting
    sleep 0.5
done

echo ""
echo "✅ Test run complete!"
echo "📄 Results saved to: $OUTPUT_FILE"
echo "📋 Logs available in: $LOG_FILE"
echo ""

# Clean up: Kill API server if we started it
if [ -n "$API_PID" ]; then
    echo "Stopping API server (PID: $API_PID)..."
    kill $API_PID 2>/dev/null
    echo "✓ API server stopped"
    echo ""
fi

echo "Summary:"
echo "  Total questions: $total"
echo "  Results file: $OUTPUT_FILE"
echo "  Log file: $LOG_FILE"
echo ""
echo "To view results: cat $OUTPUT_FILE"
echo "To view logs: tail -f $LOG_FILE"

