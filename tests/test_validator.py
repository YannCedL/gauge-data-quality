"""
Tests for gauge data quality validator
"""

from gauge_data_quality import validate_result, check_freshness

def test_validate_result_success():
    data = {
        "result": {"id": "123"},
        "evidence": [],
        "sources": ["http://example.com"],
        "confidence": 0.9
    }
    report = validate_result(data)
    assert report.is_valid is True
    assert len(report.missing_fields) == 0

def test_validate_result_missing_field():
    data = {
        "result": {"id": "123"},
        "confidence": 0.9
    }
    report = validate_result(data)
    assert report.is_valid is False
    assert "evidence" in report.missing_fields
    assert "sources" in report.missing_fields

def test_check_freshness():
    assert check_freshness("2026-04-01T10:00:00Z", max_age_days=365) is True
