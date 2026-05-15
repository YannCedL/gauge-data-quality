# test du validateur de qualité de données Gauge
from gauge_data_quality.validator import evaluate_quality, validate_result

def test_evaluate_quality():
    contract = evaluate_quality("flux_test")
    assert contract is not None
    assert contract.result["quality_score"] > 0.8
    assert len(contract.evidence) >= 1

def test_validate_result():
    res = validate_result({"result": "ok", "evidence": [], "sources": [], "confidence": 0.9})
    assert res.is_valid is True
