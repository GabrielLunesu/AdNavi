#!/usr/bin/env python3
"""
Debug QA Script
===============

A focused debugging script to test individual QA questions and trace the execution pipeline.
This helps identify where failures occur in the translation and execution process.

Usage:
    python3 debug_qa.py "What are my spend and revenue this month?"
"""

import sys
import json
from datetime import datetime
from typing import Dict, Any

# Add the app directory to the Python path
sys.path.append('.')

from app.services.qa_service import QAService
from app.database import get_db
from app.dsl.schema import MetricQuery
from app.dsl.planner import build_plan
from app.dsl.executor import execute_plan
from app.nlp.translator import Translator


def debug_question(question: str, workspace_id: str = "9c76b246-faf1-42d6-9a5a-f564f7801b4e"):
    """
    Debug a single question through the entire QA pipeline.
    
    Args:
        question: The natural language question to debug
        workspace_id: The workspace ID to use for the query
    """
    print(f"🔍 Debugging Question: '{question}'")
    print("=" * 80)
    
    # Get database session
    db = next(get_db())
    
    try:
        # Step 1: Test the translator
        print("\n📝 Step 1: Testing Translator")
        print("-" * 40)
        
        translator = Translator()
        dsl, error = translator.to_dsl(question)
        
        if error:
            print(f"❌ Translation Error: {error}")
            return
        
        print(f"✅ DSL Generated:")
        print(json.dumps(dsl.model_dump(mode='json'), indent=2))
        
        # Step 2: Test the planner
        print("\n📋 Step 2: Testing Planner")
        print("-" * 40)
        
        plan = build_plan(dsl)
        if plan is None:
            print("❌ Plan generation failed")
            return
        
        print(f"✅ Plan Generated:")
        print(f"  - Query Type: {plan.query.query_type}")
        print(f"  - Metric: {plan.query.metric}")
        print(f"  - Base Measures: {plan.base_measures}")
        print(f"  - Time Range: {plan.start} to {plan.end}")
        print(f"  - Breakdown: {plan.breakdown}")
        print(f"  - Derived: {plan.derived}")
        print(f"  - Filters: {plan.filters}")
        
        # Step 3: Test the executor
        print("\n⚙️  Step 3: Testing Executor")
        print("-" * 40)
        
        result = execute_plan(db, workspace_id, plan, dsl)
        
        if result is None:
            print("❌ Execution failed")
            return
        
        print(f"✅ Execution Result:")
        if isinstance(result, dict):
            print(f"  - Result Type: {result.get('query_type', 'unknown')}")
            if result.get('query_type') == 'multi_metrics':
                print(f"  - Metrics Count: {len(result.get('metrics', {}))}")
                metrics_data = result.get('metrics', {})
                print(f"  - Metrics Keys: {list(metrics_data.keys())}")
                for metric_name, metric_data in metrics_data.items():
                    print(f"    - {metric_name} (type: {type(metric_name)}): {metric_data}")
            else:
                print(f"  - Summary: {result.summary}")
                print(f"  - Previous: {result.previous}")
                print(f"  - Delta Pct: {result.delta_pct}")
        else:
            print(f"  - Summary: {result.summary}")
            print(f"  - Previous: {result.previous}")
            print(f"  - Delta Pct: {result.delta_pct}")
        
        # Step 4: Test the full QA service
        print("\n🤖 Step 4: Testing Full QA Service")
        print("-" * 40)
        
        service = QAService(db)
        qa_result = service.answer(
            question=question,
            workspace_id=workspace_id,
            user_id="test-user"
        )
        
        print(f"✅ QA Service Result:")
        if isinstance(qa_result, dict):
            print(f"  - Answer: {qa_result.get('answer', 'No answer')[:200]}...")
            print(f"  - DSL: {qa_result.get('executed_dsl', 'No DSL')}")
        else:
            print(f"  - Answer: {qa_result.answer[:200]}...")
            print(f"  - DSL: {qa_result.executed_dsl}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        db.close()


def main():
    """Main function to run the debug script."""
    if len(sys.argv) != 2:
        print("Usage: python3 debug_qa.py \"Your question here\"")
        print("\nExample:")
        print("  python3 debug_qa.py \"What are my spend and revenue this month?\"")
        print("  python3 debug_qa.py \"Which day had the lowest CPC?\"")
        sys.exit(1)
    
    question = sys.argv[1]
    debug_question(question)


if __name__ == "__main__":
    main()
