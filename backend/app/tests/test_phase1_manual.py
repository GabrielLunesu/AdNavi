"""
Manual test script for Phase 1 implementation.

Run this to test intent classification and answer generation
with real questions during development.

Usage:
    python -m app.tests.test_phase1_manual
"""

import asyncio
from app.services.qa_service import QAService
from app.database import SessionLocal
from app import models


async def test_phase1():
    """Test Phase 1: Intent classification + different answer depths."""
    
    # Find a workspace
    db = SessionLocal()
    workspace = db.query(models.Workspace).first()
    
    if not workspace:
        print("❌ No workspace found. Run seed_mock.py first")
        return
    
    print(f"✅ Using workspace: {workspace.name} ({workspace.id})")
    print("=" * 80)
    
    qa_service = QAService()
    
    # Test questions grouped by expected intent
    test_cases = [
        # SIMPLE intent
        ("what was my roas last month", "SIMPLE", "1 sentence"),
        ("how much did I spend yesterday", "SIMPLE", "1 sentence"),
        ("what's my cpc this week", "SIMPLE", "1 sentence"),
        
        # COMPARATIVE intent
        ("how does my roas compare to last month", "COMPARATIVE", "2-3 sentences with comparison"),
        ("which campaign had highest roas", "COMPARATIVE", "2-3 sentences with top performer"),
        ("compare google vs meta performance", "COMPARATIVE", "2-3 sentences comparing platforms"),
        
        # ANALYTICAL intent
        ("why is my roas so volatile", "ANALYTICAL", "3-4 sentences with trends and insights"),
        ("explain the trend in my cpc", "ANALYTICAL", "3-4 sentences with analysis"),
        ("analyze my campaign performance", "ANALYTICAL", "3-4 sentences with full context"),
    ]
    
    results = []
    
    for question, expected_intent, expected_answer_style in test_cases:
        print(f"\n📝 Question: {question}")
        print(f"   Expected: {expected_intent} intent → {expected_answer_style}")
        print("-" * 80)
        
        try:
            result = await qa_service.answer(
                question=question,
                workspace_id=str(workspace.id),
                user_id="test_user"
            )
            
            answer = result["answer"]
            executed_dsl = result["executed_dsl"]
            
            # Count sentences (rough approximation)
            sentence_count = answer.count('.') + answer.count('!') + answer.count('?')
            
            print(f"✅ Answer ({sentence_count} sentences): {answer}")
            print(f"   DSL: {executed_dsl.get('metric')} over {executed_dsl.get('time_range', {}).get('last_n_days', '?')} days")
            
            # Quality check
            quality = "✅ PASS"
            if expected_intent == "SIMPLE" and sentence_count > 1:
                quality = "⚠️  WARNING: Too verbose for SIMPLE intent"
            elif expected_intent == "COMPARATIVE" and sentence_count > 3:
                quality = "⚠️  WARNING: Too verbose for COMPARATIVE intent"
            elif expected_intent == "ANALYTICAL" and sentence_count > 4:
                quality = "⚠️  WARNING: Too verbose for ANALYTICAL intent"
            
            print(f"   Quality: {quality}")
            
            results.append({
                "question": question,
                "expected_intent": expected_intent,
                "answer": answer,
                "sentence_count": sentence_count,
                "quality": quality
            })
            
        except Exception as e:
            print(f"❌ Error: {e}")
            results.append({
                "question": question,
                "expected_intent": expected_intent,
                "error": str(e),
                "quality": "❌ FAIL"
            })
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    passed = sum(1 for r in results if "✅" in r.get("quality", ""))
    total = len(results)
    
    print(f"\nResults: {passed}/{total} passed")
    
    for r in results:
        status = "✅" if "✅" in r.get("quality", "") else "⚠️" if "⚠️" in r.get("quality", "") else "❌"
        print(f"{status} {r['question'][:50]}")
    
    db.close()


if __name__ == "__main__":
    asyncio.run(test_phase1())

