"""
Integration tests for Unified Metrics refactor.

Tests consistency between QA and KPI endpoints after refactoring to use UnifiedMetricService.
"""

import pytest
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

from app.services.unified_metric_service import UnifiedMetricService, MetricFilters
from app.dsl.schema import TimeRange
from app.dsl.executor import execute_plan
from app.dsl.planner import build_plan
from app.dsl.schema import MetricQuery

load_dotenv()

@pytest.fixture
def db_session():
    """Create a database session for testing."""
    engine = create_engine(os.getenv('DATABASE_URL'))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture
def workspace_id():
    """Use the workspace ID from the seeded data."""
    return "9c76b246-faf1-42d6-9a5a-f564f7801b4e"


class TestUnifiedMetricsConsistency:
    """Test consistency between UnifiedMetricService and refactored endpoints."""
    
    def test_revenue_all_entities_consistency(self, db_session, workspace_id):
        """Test that UnifiedMetricService and KPI endpoint return same revenue for all entities."""
        # Test UnifiedMetricService directly
        service = UnifiedMetricService(db_session)
        time_range = TimeRange(last_n_days=7)
        filters = MetricFilters()  # No filters = all entities
        
        service_result = service.get_summary(
            workspace_id=workspace_id,
            metrics=["revenue"],
            time_range=time_range,
            filters=filters,
            compare_to_previous=False
        )
        
        # Test QA endpoint via DSL executor
        query = MetricQuery(
            query_type="metrics",
            metric="revenue",
            time_range=time_range,
            compare_to_previous=False,
            group_by="none",
            breakdown=None,
            top_n=5,
            sort_order="desc",
            filters={}
        )
        
        plan = build_plan(query)
        qa_result = execute_plan(db_session, workspace_id, plan, query)
        
        # Both should return the same revenue value
        service_revenue = service_result.metrics["revenue"].value
        qa_revenue = qa_result.summary
        
        assert abs(service_revenue - qa_revenue) < 0.01, f"Service: {service_revenue}, QA: {qa_revenue}"
    
    def test_revenue_active_entities_consistency(self, db_session, workspace_id):
        """Test that UnifiedMetricService and KPI endpoint return same revenue for active entities only."""
        # Test UnifiedMetricService with active filter
        service = UnifiedMetricService(db_session)
        time_range = TimeRange(last_n_days=7)
        filters = MetricFilters(status="active")
        
        service_result = service.get_summary(
            workspace_id=workspace_id,
            metrics=["revenue"],
            time_range=time_range,
            filters=filters,
            compare_to_previous=False
        )
        
        # Test QA endpoint with active filter
        query = MetricQuery(
            query_type="metrics",
            metric="revenue",
            time_range=time_range,
            compare_to_previous=False,
            group_by="none",
            breakdown=None,
            top_n=5,
            sort_order="desc",
            filters={"status": "active"}
        )
        
        plan = build_plan(query)
        qa_result = execute_plan(db_session, workspace_id, plan, query)
        
        # Both should return the same revenue value
        service_revenue = service_result.metrics["revenue"].value
        qa_revenue = qa_result.summary
        
        assert abs(service_revenue - qa_revenue) < 0.01, f"Service: {service_revenue}, QA: {qa_revenue}"
    
    def test_multiple_metrics_consistency(self, db_session, workspace_id):
        """Test consistency for multiple metrics."""
        service = UnifiedMetricService(db_session)
        time_range = TimeRange(last_n_days=7)
        filters = MetricFilters()
        
        metrics = ["revenue", "spend", "roas"]
        
        # Test UnifiedMetricService
        service_result = service.get_summary(
            workspace_id=workspace_id,
            metrics=metrics,
            time_range=time_range,
            filters=filters,
            compare_to_previous=False
        )
        
        # Test QA endpoint with multi-metric query
        query = MetricQuery(
            query_type="metrics",
            metric=metrics,
            time_range=time_range,
            compare_to_previous=False,
            group_by="none",
            breakdown=None,
            top_n=5,
            sort_order="desc",
            filters={}
        )
        
        plan = build_plan(query)
        qa_result = execute_plan(db_session, workspace_id, plan, query)
        
        # Compare each metric
        for metric in metrics:
            service_value = service_result.metrics[metric].value
            qa_value = qa_result["metrics"][metric]["summary"]
            
            assert abs(service_value - qa_value) < 0.01, f"Metric {metric}: Service: {service_value}, QA: {qa_value}"
    
    def test_provider_filter_consistency(self, db_session, workspace_id):
        """Test consistency with provider filter."""
        service = UnifiedMetricService(db_session)
        time_range = TimeRange(last_n_days=7)
        filters = MetricFilters(provider="meta")
        
        # Test UnifiedMetricService
        service_result = service.get_summary(
            workspace_id=workspace_id,
            metrics=["revenue"],
            time_range=time_range,
            filters=filters,
            compare_to_previous=False
        )
        
        # Test QA endpoint with provider filter
        query = MetricQuery(
            query_type="metrics",
            metric="revenue",
            time_range=time_range,
            compare_to_previous=False,
            group_by="none",
            breakdown=None,
            top_n=5,
            sort_order="desc",
            filters={"provider": "meta"}
        )
        
        plan = build_plan(query)
        qa_result = execute_plan(db_session, workspace_id, plan, query)
        
        # Both should return the same revenue value
        service_revenue = service_result.metrics["revenue"].value
        qa_revenue = qa_result.summary
        
        assert abs(service_revenue - qa_revenue) < 0.01, f"Service: {service_revenue}, QA: {qa_revenue}"
    
    def test_timeseries_consistency(self, db_session, workspace_id):
        """Test consistency for timeseries data."""
        service = UnifiedMetricService(db_session)
        time_range = TimeRange(last_n_days=7)
        filters = MetricFilters()
        
        # Test UnifiedMetricService timeseries
        service_timeseries = service.get_timeseries(
            workspace_id=workspace_id,
            metrics=["revenue"],
            time_range=time_range,
            filters=filters
        )
        
        # Test QA endpoint with timeseries
        query = MetricQuery(
            query_type="metrics",
            metric="revenue",
            time_range=time_range,
            compare_to_previous=False,
            group_by="none",
            breakdown=None,
            top_n=5,
            sort_order="desc",
            filters={},
            need_timeseries=True
        )
        
        plan = build_plan(query)
        qa_result = execute_plan(db_session, workspace_id, plan, query)
        
        # Compare timeseries data
        assert len(service_timeseries) == len(qa_result.timeseries), "Timeseries length mismatch"
        
        for i, (service_point, qa_point) in enumerate(zip(service_timeseries, qa_result.timeseries)):
            assert service_point.date == qa_point["date"], f"Date mismatch at index {i}"
            assert abs(service_point.value - qa_point["value"]) < 0.01, f"Value mismatch at index {i}"
    
    def test_breakdown_consistency(self, db_session, workspace_id):
        """Test consistency for breakdown data."""
        service = UnifiedMetricService(db_session)
        time_range = TimeRange(last_n_days=7)
        filters = MetricFilters()
        
        # Test UnifiedMetricService breakdown
        service_breakdown = service.get_breakdown(
            workspace_id=workspace_id,
            metric="revenue",
            time_range=time_range,
            filters=filters,
            breakdown_dimension="provider",
            top_n=5,
            sort_order="desc"
        )
        
        # Test QA endpoint with breakdown
        query = MetricQuery(
            query_type="metrics",
            metric="revenue",
            time_range=time_range,
            compare_to_previous=False,
            group_by="none",
            breakdown="provider",
            top_n=5,
            sort_order="desc",
            filters={}
        )
        
        plan = build_plan(query)
        qa_result = execute_plan(db_session, workspace_id, plan, query)
        
        # Compare breakdown data
        assert len(service_breakdown) == len(qa_result.breakdown), "Breakdown length mismatch"
        
        for i, (service_item, qa_item) in enumerate(zip(service_breakdown, qa_result.breakdown)):
            assert service_item.label == qa_item["label"], f"Label mismatch at index {i}"
            assert abs(service_item.value - qa_item["value"]) < 0.01, f"Value mismatch at index {i}"
