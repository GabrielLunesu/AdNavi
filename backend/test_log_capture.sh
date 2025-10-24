#!/bin/bash
LOG_FILE="qa_logs.txt"

# Simulate the script logic
log_start_size=$(wc -l < "$LOG_FILE")
echo "Log start size: $log_start_size"

# Simulate API call delay
sleep 0.2

total_lines=$(wc -l < "$LOG_FILE")
echo "Total lines: $total_lines"

if [ "$total_lines" -gt "$log_start_size" ]; then
    lines_to_read=$((total_lines - log_start_size))
    echo "Lines to read: $lines_to_read"
    echo "Captured logs:"
    tail -n "$lines_to_read" "$LOG_FILE" | grep -E "\[QA_PIPELINE\]|\[COMPARISON\]|\[UNIFIED_METRICS\]|\[ENTITY_CATALOG\]" | head -n 10
fi
